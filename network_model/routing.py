from django.urls import path
from channels.routing import URLRouter
from .consumers import MapUpdatesConsumer

websocket_urlpatterns = [
    path('ws/updates/<int:map_id>', MapUpdatesConsumer.as_asgi()),
]