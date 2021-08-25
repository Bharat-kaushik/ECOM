from django.contrib import admin

from businesslogic.domain.user import User
from businesslogic.domain.product import Product
from businesslogic.domain.order import Order
from businesslogic.domain.address import Address

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Address)
