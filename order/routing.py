from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<int:order_id>', consumers.OrderConsumer),
]
