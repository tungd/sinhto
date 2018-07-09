from rest_framework import serializers

from . import models


class CreateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    drink = serializers.StringRelatedField()

    class Meta:
        model = models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = '__all__'
        depth = 1

    def get_total(self, order):
        return sum([item.drink.price for item in order.items.all()])
