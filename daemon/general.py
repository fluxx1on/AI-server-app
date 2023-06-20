import asyncio
from aioredis import Redis, ConnectionPool
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
        self.daemons: List[ActionsDaemon] = list()
        self.queue: asyncio.Queue = asyncio.Queue()

    async def redis_connect(self: C):

        async def try_to_connect() -> None:
            try:
                connection_pool = ConnectionPool.from_url(settings.REDIS_DB)
                self.redis = await Redis(connection_pool=connection_pool)
            except Exception as exc:
                raise RuntimeError('Redis crashed') from exc      
        
        await try_to_connect()
    
    async def open_redis_db(self: C):
        await maps_filler(redis=self.redis)

    async def add_handlers(self: C):

        async def redis_handler():
            async for map in maps:
                stream_handler = RedisStreamHandler(str(map.id), self.redis)
                await stream_handler.start_listening()
                self.stream_handlers.append(stream_handler)

        async def daemon_actions():
            async for map in maps:
                daemon = ActionsDaemon(self.redis, map)
                await daemon.start_daemon()
                self.daemons.append(daemon)

        maps = Location.objects.all()
        await asyncio.gather(redis_handler(), daemon_actions())


def main_service():
    async def run_tasks():
        controller = Controller()
        await controller.redis_connect()
        await controller.open_redis_db()
        await controller.add_handlers()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_tasks())
    loop.close()
