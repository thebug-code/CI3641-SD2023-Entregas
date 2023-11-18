import sys
import ast

# Conjuntos de partes crecientes de un conjunto

def sublists_crecientes(p):
    """
    Calcula el conjunto de sublistas crecientes de una lista
    """
    if p == []:
        yield []
    else:
        for x in sublists_crecientes(p[1:]):
            yield x
            if es_creciente([p[0], *x]):
                yield [p[0], *x]


def es_creciente(p):
    """
    Determina si una lista es creciente
    """
    if len(p) < 2:
        return True
    else:
        return p[0] < p[1] and es_creciente(p[1:])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 sublists_crecientes.py <list>")
        sys.exit(1)

    l = ast.literal_eval(sys.argv[1])
    for x in sublists_crecientes(l):
        print(x)
