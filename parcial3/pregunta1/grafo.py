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
from pila import Pila
from cola import Cola

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

# DFS para hallar camino entre dos nodos
class DFS(Busqueda):
    def __init__(self, grafo: Grafo):
        super().__init__(grafo)

    def buscar(self, D: int, H: int) -> int:
        visitados = [False] * self.grafo.nodos
        pila = Pila[int]()
        pila.agregar(D)
        visitados[D] = True
        contador = 0

        while not pila.vacio():
            nodo = pila.remover()
            visitados[nodo] = True
            
            if nodo == H:
                return contador

            for adyacente in self.grafo.adj_list[nodo]:
                if not visitados[adyacente]:
                    visitados[adyacente] = True
                    pila.agregar(adyacente)
            contador += 1
        
        return -1

# BFS para hallar camino entre dos nodos
class BFS(Busqueda):
    def __init__(self, grafo: Grafo):
        super().__init__(grafo)

    def buscar(self, D: int, H: int) -> int:
        visitados = [False] * self.grafo.nodos
        cola = Cola[int]()
        cola.agregar(D)
        visitados[D] = True
        contador = 0

        while not cola.vacio():
            nodo = cola.remover()
            visitados[nodo] = True
            
            if nodo == H:
                return contador

            for adyacente in self.grafo.adj_list[nodo]:
                if not visitados[adyacente]:
                    visitados[adyacente] = True
                    cola.agregar(adyacente)
            contador += 1
        
        return -1

g = Grafo(5)
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(2, 1)
g.agregar_arista(0, 3)
g.agregar_arista(1, 4)

dfs = DFS(g)
print(dfs.buscar(0, 4))

bfs = BFS(g)
print(bfs.buscar(0, 4))
