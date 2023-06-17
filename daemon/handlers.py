import asyncio
from channels_redis.core import RedisChannelLayer
from aioredis import ConnectionPool, Redis

class RedisStreamHandler:

    def __init__(
        self, stream_name: str, 
        channel_layer: RedisChannelLayer, 
        redis: Redis
    ):
        self.stream_name = stream_name,
        self.channel_layer: RedisChannelLayer = channel_layer,
        self.redis: Redis = redis

    async def listen_to_stream(self):
        # Создание итератора для чтения Redis Stream
        stream_iterator = await self.redis.xread([self.stream_name], latest_ids=["$"])

        async for stream_messages in stream_iterator:

            for message in stream_messages:
                message_id = message[0]  # Идентификатор сообщения
                message_data = message[1]  # Данные сообщения (словарь)
            
            await self.channel_layer.group_send(
                self.stream_name, message = {
                    'type': 'stream_sender',
                    'stream_data': message_data
                }
            )

    def start_listening(self):
        asyncio.ensure_future(self.listen_to_stream())

