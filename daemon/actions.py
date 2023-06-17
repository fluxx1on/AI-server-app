import asyncio
from aioredis import Redis
from typing import List
from . import Creature, Location
from .filler import MAX_ON_MAP

class ActionsDaemon:

    def __init__(self, redis: Redis, map: Location) -> None:
        self.redis: Redis = redis
        self.mobs: List[Creature] = map.allowed_creatures.all()
        self.map: Location = map

    async def vectorize_movement(self):
        pass

    async def mobs_respawn(self):
        print(self.check_mobs())
        await asyncio.sleep(45)

    async def check_mobs(self):
        keys = await self.redis.keys(f'map:{self.map.id}:mob:*')
        return await self.redis.hgetall(keys)

    def start_daemon(self):
        asyncio.ensure_future(self.vectorize_movement())
        asyncio.ensure_future(self.mobs_respawn()) 