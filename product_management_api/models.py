from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through="ProductQuantity")

    def __str__(self):
        return self.name


class ProductQuantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Order(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    discount_applied = models.BooleanField(default=False)

    def calculate_discount(self):
        total_members = self.users.count()
        discount_percentage = 2
        total_discount = total_members * discount_percentage
        return min(total_discount, 40)

    def apply_discount(self):
        discount = self.calculate_discount()
        if discount > 0:
            self.discount_applied = True
            self.save()
            return discount
        return 0
