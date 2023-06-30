import asyncio
from channels_redis.core import RedisChannelLayer
from aioredis import ConnectionPool, Redis

from channels.layers import get_channel_layer

class RedisStreamHandler:

    def __init__(
        self, stream_name: str,
        redis: Redis
    ):
        self.stream_name: str = stream_name
        self.channel_layer = get_channel_layer()
        self.redis: Redis = redis
        self.fstream: str = f'map:{self.stream_name}'

    async def listen_to_stream(self):

        last_id = '0-0'
        
        while True:
            # Iterator creation from Redis Stream
            stream_iterator = await self.redis.xread(streams={self.fstream: last_id}, count=1)
            try:
                for message in stream_iterator[0][1]:
                    message_id = message[0]  # Unique Identificator
                    message_data = message[1][b'message']  # Data (protobuf-bytes)

                    await self.channel_layer.group_send(
                        self.stream_name, message = {
                            'type': 'stream_sender',
                            'stream_data': message_data
                        }
                    )
                    last_id = message_id.decode()
                    await self.redis.xtrim(self.fstream, 5)
            except IndexError:
                pass
            await asyncio.sleep(0.5)

    async def start_listening(self):
        print('handler starts')
        await self.listen_to_stream()

