#  Defina un tipo de datos que represente grafos como listas de adyacencias y cada
# nodo sea representado por un número entero (puede usar todas las librerías a su
# disposición en el lenguaje).
# Además, defina una clase abstracta Busqueda que debe tener un método buscar.
# Este método debe recibir dos enteros: D y H, y debe devolver la cantidad de nodos
# explorados, partiendo desde el nodo D hasta llegar al nodo H. En caso de que H no
# sea alcanzable desde D, debe devolver el valor -1 (menos uno).
# Esta clase debe estar parcialmente implementada, dejando solamente abstraído el
# orden en el que se han de explorar los nodos.
# Defina dos clases concretas DFS y BFS que sean subtipo de Busqueda.
# • Para DFS el orden de selección de nodos es a profundidad (usando un pila).
# •  Para BFS el orden de selección de nodos es a amplitud (usando un cola).

from collections import defaultdict
from abc import ABC, abstractmethod

# Grafo dirigido usando lista de adyacencia

class Grafo:
    def __init__(self, nodos: int):
        self.adj_list = defaultdict(list)
        self.nodos = nodos

    def agregar_arista(self, origen: int, destino: int):
        self.adj_list[origen].append(destino)


# Clase abstracta Busqueda
class Busqueda(ABC):
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    @abstractmethod
    def buscar(self, D: int, H: int) -> int:
        pass




