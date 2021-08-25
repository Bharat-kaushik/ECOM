from django.db import IntegrityError

from businesslogic.domain.address import Address
from businesslogic.domain.product import Product
from businesslogic.domain.order import Order


def add_order(product: Product,
              address: Address,
              ):

    """
    Add New Order.
    """
    order = Order()
    order.product = product
    order.address = address

    try:
        order.save()
    except IntegrityError as e:
        raise e
    except Exception as e:
        raise e

    return order
