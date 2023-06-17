import asyncio
from aioredis import Redis, ConnectionPool
from channels.layers import get_channel_layer
from typing import List, TypeVar
from . import settings, Location
from .handlers import RedisStreamHandler
from .filler import maps_filler
from .actions import ActionsDaemon

C = TypeVar("C", bound="Controller")

class Controller():

    def __init__(self) -> None:
        self.redis: Redis
        self.stream_names: List[str]
        self.stream_handlers: List[RedisStreamHandler] = list()
        self.daemons: List[ActionsDaemon]
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

        def redis_handler():
            channel_layer = get_channel_layer()
            for map in maps:
                stream_handler = RedisStreamHandler(map.id, channel_layer, self.redis)
                stream_handler.start_listening()
                self.stream_handlers.append(stream_handler)

        def daemon_actions():
            for map in maps:
                daemon = ActionsDaemon(self.redis, map)
                daemon.start_daemon()
                self.daemons.append(daemon)

        maps = Location.objects.all()
        redis_handler()
        daemon_actions()
        return self

def main_service():
    
    controller = (Controller()
                .redis_connect()
                .open_redis_db()
                .add_handlers())