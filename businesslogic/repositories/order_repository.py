from typing import Any
from django.core.exceptions import ObjectDoesNotExist
from businesslogic.domain.order import Order
from .repository_base import RepositoryBase


class OrderRepository(RepositoryBase):
    def _get(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            raise e
        except Exception as e:
            raise e

    def get_all(self) -> Any:
        return Order.objects.all()

    def filter_data(self, **kwargs) -> Any:
        return Order.objects.filter(**kwargs)