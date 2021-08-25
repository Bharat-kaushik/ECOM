from django.db import models


class Product(models.Model):
    """
        creating product table.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="products")
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title
