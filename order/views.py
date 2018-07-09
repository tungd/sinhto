from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import generics

from . import models, serializers


class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CreateOrderItemView(generics.CreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.CreateOrderItemSerializer

    def create(self, *args, **kwargs):
        response = super().create(*args, **kwargs)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'order_2', {'type': 'order.update', 'order_id': 2}
        )

        return response
