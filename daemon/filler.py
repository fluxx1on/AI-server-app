import asyncio
from aioredis import Redis
from . import Location, Creature
from .utils.structure import MAX_ON_MAP
from .creation import _xadd, manual_creation

# Initialize Streams and Mobs 
async def maps_filler(redis: Redis):
    maps = Location.objects.all()
    tasks = []
    async for map in maps:
        count = len(redis.keys(f'map:{map.id}:mob:*'))
        related_mobs = map.allowed_creatures.all()
        await manual_creation(
            amount=MAX_ON_MAP-count,
            redis=redis,
            location=map,
            related_mobs=related_mobs
        )
