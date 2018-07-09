from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import generics, renderers

from . import models, serializers


class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CreateOrderItemView(generics.CreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.CreateOrderItemSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)

        channel_layer = get_channel_layer()
        order = serializer.instance.order
        serializer = serializers.OrderSerializer(order)
        renderer = renderers.JSONRenderer()

        async_to_sync(channel_layer.group_send)(
            'order_{}'.format(order.pk), {
                'type': 'order.update',
                'data': str(renderer.render(serializer.data), 'utf-8')
            }
        )
