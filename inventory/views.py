from rest_framework import generics

from . import models, serializers


class ShopDetailView(generics.RetrieveAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
