from secuencia import Secuencia
from secuencia import T

class Pila(Secuencia[T]):
    def __init__(self):
        super().__init__()

    def agregar(self, elemento: T):
        self._secuencia.append(elemento)

    def remover(self):
        return self._secuencia.pop()

    def vacio(self):
        return len(self._secuencia) == 0

    def __str__(self):
        return str(self._secuencia)
