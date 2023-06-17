from django.urls import path
from channels.routing import URLRouter
from .consumers import MapUpdatesConsumer

websocket_urlpatterns = [
    path('ws/updates/map', MapUpdatesConsumer.as_asgi()),
]