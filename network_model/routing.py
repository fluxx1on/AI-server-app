from django.urls import path, re_path
from channels.routing import URLRouter
from .consumers import MapUpdatesConsumer
import re

websocket_urlpatterns = [
   # re_path(r'^ws/updates/(?P<map_id>\d+)$', MapUpdatesConsumer.as_asgi()),
    path('ws/updates/<int:map_id>', MapUpdatesConsumer.as_asgi()),
]