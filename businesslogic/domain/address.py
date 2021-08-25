from django.db import models
from businesslogic.domain.user import User


class Address(models.Model):
    """
    creating address table fields
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=150, null=False, blank=False)
    state = models.CharField(max_length=150, null=False, blank=False)
    zip = models.CharField(max_length=6, null=False, blank=False)

    objects = models.Manager

    def __str__(self):
        return self.user.first_name
