from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/data/', consumers.ChatConsumer.as_asgi()),
]