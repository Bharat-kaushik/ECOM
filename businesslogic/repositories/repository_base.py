from typing import TypeVar, Generic, NewType, Set, Any, Tuple, NoReturn
from django.db import models
from abc import abstractmethod
from django.db import transaction

T = TypeVar('T', bound=models.Model)


class RepositoryBase:
    def __init__(self):
        """

        :rtype: object
        """
        self.seen = set()  # type: Set[T]

    @staticmethod
    def add(domain: T) -> T:
        domain.save()
        return domain

    def delete_by_pk(self, pk: Any) -> NoReturn:
        p = self._get(pk)
        if p:
            p.delete()

    def get_by_pk(self, pk) -> T:
        p = self._get(pk)
        if p:
            self.seen.add(p)
        return p

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def _get(self, pk) -> T:
        raise NotImplementedError

    @abstractmethod
    def filter_data(self, **kwargs) -> Any:
        raise NotImplementedError

