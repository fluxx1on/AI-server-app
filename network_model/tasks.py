from aioredis import ConnectionPool, Redis
from django.conf import settings
from celery import shared_task
from . import celery_app as app
import json
import asyncio
import aiohttp
import logging

logger = logging.getLogger(__name__)

# From daemon
async def redis_connect() -> Redis:

    async def try_to_connect() -> Redis:
        try:
            connection_pool = ConnectionPool.from_url(settings.REDIS_DB)
            return await Redis(connection_pool=connection_pool)
        except Exception as exc:
            raise RuntimeError('Redis crashed') from exc      
    
    return await try_to_connect()

async def send_respond():
    chunk = asyncio.Semaphore(50)
    redis: Redis = await redis_connect()

    async def task(mark, user_id):
        json_data = json.dumps({
            "user_id": int(user_id),
            "mark": int(mark)
        })

        url = 'http://localhost:8080/responds'
        headers = {'Content-Type': 'application/json'}
        
        async with aiohttp.ClientSession() as session:
            async with session.put(url, data=json_data, headers=headers) as response:
                response_text = await response.text()
    
    async def semaphore(task):
        async with chunk:
            await task

    keys = await redis.keys("rates:*")
    tasks = list()

    pipeline = redis.pipeline()
    for key in keys:
        pipeline.get(key)

    responds = await pipeline.execute()
    for index, respond in enumerate(responds):
        tasks.append(
            asyncio.create_task(task(
                respond, keys[index].decode().split(":")[-1]
            ))
        )
    await asyncio.gather(*[semaphore(task) for task in tasks])
    await redis.delete(*keys)
    
@app.task
def goapi_responds():
    asyncio.run(send_respond())