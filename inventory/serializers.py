from rest_framework import serializers

from . import models


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drink
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    drinks = DrinkSerializer(many=True)

    class Meta:
        model = models.Shop
        fields = '__all__'
        depth = 2
