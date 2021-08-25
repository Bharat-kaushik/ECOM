from django.db import models
from businesslogic.domain.product import Product
from businesslogic.domain.address import Address


class Order(models.Model):
    """
        creating Order table.
    """
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.manager

    def __str__(self):
        return self.product.title

