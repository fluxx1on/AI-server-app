from channels.generic.websocket import AsyncWebsocketConsumer
from . import redis_conn

class MapUpdatesConsumer(AsyncWebsocketConsumer):
    """
    AsyncWebsocket for providing info about Map objects updates
    """

    def __init__(self, *args, **kwargs):
        self.map_id: int
        self.user_id: int
        super().__init__(*args, **kwargs)

    # Create a connection. group_name received from client JS script
    async def connect(self):
        try:
            self.map_id = int(self.scope['url_route']['kwargs']['map_id'])
            self.user_id = int(self.scope['url_route']['kwargs']['user_id'])
        except Exception as exc:
            raise RuntimeError("Something went wrong with connect on MapUpdatesConsumer") from exc
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        self.accept()

    # Shutting down the connection
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        super().disconnect(code)

    # Gets user response
    async def receive(self, content):
        response = {'message': 'Сообщение получено', 'data': content}
        await self.send(response)

    # Send Stream to users
    async def stream_sender(self, stream_data):
        await self.send(stream_data)
