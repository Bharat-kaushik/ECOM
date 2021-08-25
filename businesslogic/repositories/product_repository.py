from typing import Any
from django.core.exceptions import ObjectDoesNotExist

from businesslogic.domain.product import Product
from .repository_base import RepositoryBase


class ProductRepository(RepositoryBase):
    """
    class to perform db queries
    """
    def _get(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            raise e
        except Exception as e:
            raise e

    def get_all(self) -> Any:
        return Product.objects.all()

    def filter_data(self, **kwargs) -> Any:
        return Product.objects.filter(**kwargs)
