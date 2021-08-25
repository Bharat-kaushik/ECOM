from typing import Any
from django.core.exceptions import ObjectDoesNotExist

from businesslogic.domain.user import User
from .repository_base import RepositoryBase


class UserRepository(RepositoryBase):
    """
    class methods to perform db queries for user table
    """
    def _get(self, pk):
        try:
            return User.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            raise e
        except Exception as e:
            raise e

    def get_all(self) -> Any:
        return User.objects.all()

    def filter_data(self, **kwargs) -> Any:
        return User.objects.filter(**kwargs)
