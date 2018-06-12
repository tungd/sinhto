from rest_framework import generics

from . import models, serializers


class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CreateOrderItemView(generics.CreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.CreateOrderItemSerializer
