from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Product,
    ShoppingList,
    Order,
    ProductQuantity,
)
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    OrderSerializer,
    ShoppingListSerializer,
    ProductQuantitySerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductQuantityViewSet(viewsets.ModelViewSet):
    queryset = ProductQuantity.objects.all()
    serializer_class = ProductQuantitySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)

        users_data = request.data.get("users", [])
        if users_data:
            users = get_user_model().objects.filter(id__in=users_data)
            instance.users.set(users)

        self.perform_update(serializer)
        return Response(serializer.data)


class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]
