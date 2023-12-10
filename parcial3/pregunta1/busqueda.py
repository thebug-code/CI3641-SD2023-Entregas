from abc import ABC, abstractmethod
from grafo import Grafo
from pila import Pila
from cola import Cola

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

#g = Grafo(5)
#g.agregar_arista(0, 1)
#g.agregar_arista(0, 2)
#g.agregar_arista(2, 1)
#g.agregar_arista(0, 3)
#g.agregar_arista(1, 4)
#
#bfs = BFS(g)
#print(bfs.buscar(0, 4))
#
#dfs = DFS(g)
#print(dfs.buscar(0, 4))
