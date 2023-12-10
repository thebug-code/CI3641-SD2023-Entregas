from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Secuencia(ABC, Generic[T]):
    def __init__(self):
        self._secuencia = []

    @abstractmethod
    def agregar(self, elemento: T):
        pass

    @abstractmethod
    def remover(self) -> T:
        pass

    @abstractmethod
    def vacio(self) -> bool:
        pass
