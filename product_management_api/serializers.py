from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import (
    Product,
    ShoppingList,
    Order,
    ProductQuantity,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price")


class ProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuantity
        fields = "__all__"


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username"]


class OrderSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), many=True, required=False
    )

    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["users"] = UserSerializer(
            instance.users.all(), many=True
        ).data
        representation["discount"] = f"{instance.calculate_discount()}-%"
        return representation

    def create(self, validated_data):
        users_data = validated_data.pop("users", [])
        order = Order.objects.create(**validated_data)
        order.users.set(users_data)
        order.apply_discount()
        return order
