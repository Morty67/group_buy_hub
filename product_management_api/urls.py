from django.urls import path, include
from rest_framework import routers

from product_management_api.views import (
    ProductViewSet,
    OrderViewSet,
    ShoppingListViewSet,
    ProductQuantityViewSet,
)

router = routers.DefaultRouter()
router.register("product", ProductViewSet)
router.register("order", OrderViewSet)
router.register("shopping_list", ShoppingListViewSet)
router.register("product_quantity", ProductQuantityViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "management"
