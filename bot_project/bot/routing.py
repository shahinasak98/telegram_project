
from django.urls import re_path

from bot import consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumer.Botconsumer.as_asgi()),
]