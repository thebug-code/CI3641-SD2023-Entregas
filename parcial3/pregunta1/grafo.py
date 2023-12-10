from collections import defaultdict
from abc import ABC, abstractmethod

# Grafo dirigido usando lista de adyacencia

class Grafo:
    def __init__(self, nodos: int):
        self.adj_list = defaultdict(list)
        self.nodos = nodos

    def agregar_arista(self, origen: int, destino: int):
        self.adj_list[origen].append(destino)
