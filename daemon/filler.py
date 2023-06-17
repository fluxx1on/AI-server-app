import random
import asyncio
from typing import Coroutine
from aioredis import Redis
from . import Location, Creature

def hset_getattr(obj: object) -> dict:
    attributes = obj.__class__.redis_serializer()
    hasher = dict()
    for attr in attributes:
        hasher.update({ attr : getattr(obj, attr)})
    return hasher

MAX_ON_MAP = 20
CHUNK = asyncio.Semaphore(100)

async def _hset(
    redis: Redis, mapping: dict, 
    map_id: int, mob_id: int    
):
    try:
        await redis.hset(name=f"map:{str(map_id)}:mob:{str(mob_id)}", mapping=mapping)
    except Exception as exc:
        raise ConnectionError("Redis shutted down") from exc
    
async def _xadd(redis: Redis, map_id: int):
    try:
        await redis.xadd(name=f"map:{str(map_id)}", fields=dict())
    except Exception as exc:
        raise ConnectionError("Redis shutted down") from exc
    
async def limited_coroutine(task: Coroutine):
    async with CHUNK:
        await task()

# Initialize Streams and Mobs 
async def maps_filler(redis: Redis):
    maps = Location.objects.all()
    tasks = []
    for map in maps:
        task = asyncio.create_task(
            _xadd(redis, map.id)
        )
        mobs = map.allowed_creatures.all()
        count_mobs = len(mobs)
        if mobs is not None:
            for mob in range(MAX_ON_MAP):
                pick_random = mobs[random.randint(0, count_mobs)]
                mapping = hset_getattr(pick_random)
                task = asyncio.create_task(
                    _hset(redis, mapping, map.id, mob)
                )
                tasks.append(task)
    await asyncio.gather(*[limited_coroutine(task) for task in tasks])

