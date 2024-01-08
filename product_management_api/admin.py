from django.contrib import admin


from .models import (
    Product,
    ShoppingList,
    Order,
    ProductQuantity,
)

admin.site.register(Product)
admin.site.register(ShoppingList)
admin.site.register(Order)
admin.site.register(ProductQuantity)
