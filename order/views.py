from rest_framework import generics

from . import models, serializers


class OrderListView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
