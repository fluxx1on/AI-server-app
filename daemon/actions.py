import asyncio
import random
from aioredis import Redis
from asgiref.sync import sync_to_async
from typing import List, Literal
from . import Creature, Location
from .creation import manual_creation
from .utils.redis import async_redis_method
from .utils.structure import MAX_ON_MAP, BORDER
from network_model.compiled_proto.mobs_pb2 import *

class ActionsDaemon:

    def __init__(self, redis: Redis, map: Location) -> None:
        self.redis: Redis = redis
        self.creatures: List[Creature] = map.allowed_creatures.all()
        self.map: Location = map
        self.hash_key = f'map:{str(self.map.id)}:mob:'
        self.mobs_count: int | None = None

    async def vectorize_movement(self):

        offset = 25

        def get_new_coords(old_x: int, old_y: int) -> tuple[int, int]:
            
            def switch_coords(old_pos):
                if old_pos-offset > BORDER and old_pos+offset < MAX_ON_MAP-BORDER:
                    return old_pos+random.randint(-offset, offset)
                elif old_pos-offset > BORDER:
                    return old_pos-random.randint(int(offset*0.2), offset)
                else:
                    return old_pos+random.randint(int(offset*0.2), offset)

            return switch_coords(old_x), switch_coords(old_y)

        while True:
            ids, mobs = await self.check_mobs()

            pipeline = self.redis.pipeline()
            mob_list_message =  MobList()
            for index, id in  enumerate(ids):
                x = None
                y = None
                if bool(int(mobs[index][b'in_battle'])) == False:
                    position_x, position_y = int(mobs[index][b'position_x']), int(mobs[index][b'position_y'])
                    x, y = get_new_coords(position_x, position_y)
                    pipeline.hmset(id.decode(), {
                        'position_x': x, 'position_y': y
                    })

                mob_message = mob_list_message.mobs.add()
                mob_message.id = int(id.decode().split(':')[-1])     
                mob_message.health = int(mobs[index][b'health'])
                mob_message.position_x = x if x is not None else int(mobs[index][b'position_x'])
                mob_message.position_y = y if y is not None else int(mobs[index][b'position_y'])
                mob_message.in_battle = bool(mobs[index][b'in_battle'])
                mob_message.parent_id = int(mobs[index][b'id'])

            serialized_data = mob_list_message.SerializeToString()
            pipeline.xadd(f'map:{str(self.map.id)}', fields={'message': serialized_data})
            
            await pipeline.execute()
            await asyncio.sleep(5)

    async def mobs_respawn(self):
            
        while True:

            if (self.mobs_count is not None 
                and self.mobs_count < MAX_ON_MAP):

                await manual_creation(
                    amount = MAX_ON_MAP-self.mobs_count, 
                    redis = self.redis,
                    location = self.map,
                    related_mobs = self.creatures
                )
            
            await asyncio.sleep(60)
            

    @async_redis_method
    async def check_mobs(self) -> tuple[List[bytes], List[dict]]:
        keys = await self.redis.keys(f'{self.hash_key}*')

        self.mobs_count = len(keys)

        pipeline = self.redis.pipeline()
        for key in keys:
            pipeline.hgetall(key)
        
        mobs = await pipeline.execute()
        return keys, mobs

    async def start_daemon(self):
        print("daemon starts")
        await asyncio.gather(self.vectorize_movement(), self.mobs_respawn())