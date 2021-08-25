from datetime import datetime

from django.db import IntegrityError
from businesslogic.domain.address import Address
from businesslogic.domain.user import User


def add_address(user: User,
                local_address: str,
                city: str,
                state: str,
                zip: str
                ):

    """
    Add New address.
    """
    address = Address()
    address.user = user
    address.address = local_address
    address.state = state
    address.city = city
    address.zip = zip

    try:
        address.save()
    except IntegrityError as e:
        raise e
    except Exception as e:
        raise e

    return address
