from aioredis import Redis, ConnectionPool
from . import settings, Location
from .handlers import RedisStreamHandler
from typing import List, TypeVar
from .filler import maps_filler
from channels.layers import get_channel_layer
import asyncio
import time

C = TypeVar("C", bound="Controller")

class Controller():

    def __init__(self) -> None:
        self.redis: Redis
        self.stream_names: List[str]
        self.stream_handlers: List[RedisStreamHandler] = list()
        self.queue: asyncio.Queue = asyncio.Queue()

    def redis_connect(self: C) -> C:

        async def try_to_connect() -> None:
            try:
                connection_pool = await ConnectionPool.from_url(settings.REDIS_DB)
                self.redis = await Redis(connection_pool=connection_pool)
            except Exception as exc:
                raise RuntimeError('Redis crashed') from exc      
        
        self.queue.put(try_to_connect())
        return self
    
    def open_redis_db(self: C) -> C:

        async def inner():
            await maps_filler(redis=self.redis)

        self.queue.put(inner())
        return self

    def add_handlers(self: C) -> C:

        async def inner():
            for map in maps:
                stream_handler = RedisStreamHandler(map.id, channel_layer)
                self.stream_handlers.append(stream_handler)

        maps = Location.objects.all()
        channel_layer = get_channel_layer()
        self.queue.put(inner())
        return self

def main_service():
    
    controller = (Controller()
                .redis_connect()
                .open_redis_db()
                .add_handlers())