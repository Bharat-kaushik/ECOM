from datetime import datetime

from django.db import IntegrityError
from businesslogic.domain.product import Product


def add_products(title: str,
                 photo,
                 price: float,
                 description: str = ""
                 ):

    """
    Add New Product.
    """
    product = Product()
    product.title = title
    product.image = photo
    product.price = price
    product.description = description

    try:
        product.save()
    except IntegrityError as e:
        raise e
    except Exception as e:
        raise e

    return product
