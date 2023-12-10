from secuencia import Secuencia
from secuencia import T

class Cola(Secuencia[T]):
    def __init__(self):
        super().__init__()

    def agregar(self, elemento: T):
        self._secuencia.append(elemento)

    def remover(self):
        return self._secuencia.pop(0)

    def vacio(self):
        return len(self._secuencia) == 0

    def __str__(self):
        return str(self._secuencia)
