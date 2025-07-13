from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/$", consumers.ChatConsumer.as_asgi()),
]

from django.urls import re_path
from . import consumers
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]