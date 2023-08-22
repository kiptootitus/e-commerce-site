from django.db import models

class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Other fields and methods related to carts

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Other fields and methods related to cart items
