from typing import Any
from django.core.exceptions import ObjectDoesNotExist

from businesslogic.domain.address import Address
from .repository_base import RepositoryBase
from businesslogic.domain.user import User


class AddressRepository(RepositoryBase):
    """
    define methods to perform db queries
    """
    def get_address_for_user(self, user: User) -> Any:
        return self.filter_data(user=user)

    # override _get method of Repository Base class
    def _get(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            raise e
        except Exception as e:
            raise e

    def get_all(self) -> Any:
        return Address.objects.all()

    def filter_data(self, **kwargs) -> Any:
        return Address.objects.filter(**kwargs)
