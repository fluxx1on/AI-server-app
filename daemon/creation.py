import random
import asyncio
from django.db.models import QuerySet
from typing import Coroutine, List
from aioredis import Redis
from asgiref.sync import sync_to_async
from .utils.redis import async_redis_method
from .utils.structure import BORDER
from . import Location, Creature

    # REDIS METHODS

@async_redis_method
async def _hset(
    redis: Redis, mapping: dict, 
    map_id: int, mob_id: int
) -> None: await redis.hset(name=f"map:{str(map_id)}:mob:{str(mob_id)}", mapping=mapping)

@async_redis_method
async def _hsetnx(
    redis: Redis, mapping: dict, 
    map_id: int, mob_id: int   
) -> None: 
    name = f"map:{str(map_id)}:mob:{str(mob_id)}"
    successed = await redis.hsetnx(name=name, mapping=mapping)
    if successed == 0:
        await _hsetnx(
            redis=redis, mapping=mapping,
            map_id=map_id, mob_id=mob_id+1
        )

@async_redis_method  
async def _xadd(redis: Redis, map_id: int) -> None:
    await redis.xadd(name=f"map:{str(map_id)}", fields={'message': ''})

    # UTILS

CHUNK = asyncio.Semaphore(100)

def hset_getattr(obj: object) -> dict:
    attributes = obj.__class__.redis_serializer()
    hasher = dict()
    for attr in attributes:
        hasher.update({ attr : getattr(obj, attr)})
    return hasher

def get_random_coords(x: int, y: int) -> dict:
    coords = {
        'position_x': random.randint(0+BORDER, x-BORDER),
        'position_y': random.randint(0+BORDER, y-BORDER)
    }
    return coords

def create_mob(mobs_range: QuerySet) -> dict:
    count_mobs = len(mobs_range)
    pick_random = mobs_range[random.randint(0, count_mobs-1)]
    mapping = hset_getattr(pick_random)
    x, y = Location.format()
    mapping.update(get_random_coords(x, y))
    mapping.update({
        'in_battle': int(False)
    })
    return mapping

async def limited_creation_coroutine(task: Coroutine):
    async with CHUNK:
        await task

# For unit auto-creating
async def manual_creation(amount: int, redis: Redis, location: Location, related_mobs: List[Creature]) -> None:
    tasks = list()
    hash_key = f'map:{str(location.id)}:mob:'
    keys = await redis.keys(f'{hash_key}*')

    count_mobs = await sync_to_async(len)(related_mobs)
    count = len(keys)
    for unit in range(amount):
        mapping = create_mob(related_mobs)
        task = asyncio.create_task(
            _hset(
                redis=redis, mapping=mapping,
                map_id=location.id, mob_id=unit+count
            )
        )
        tasks.append(task)
    await asyncio.gather(*[limited_creation_coroutine(task) for task in tasks])