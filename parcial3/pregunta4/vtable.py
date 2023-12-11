#  Manejador de tablas de tablas de metodos virtuales
# para un sistema orientado a objetos con herencia simple
# y despacho dinamico de metodos

class VTable:
    def __init__(self):
        self.vtables = {}      # { "clase" : { "metodo" : "clase que lo define" } }
        self.inherit_hier = {} # { "clase" : "clase base" }

    def add(self, class_base, class_derived, methods):
        # Verica que la clase base exista (si aplica)
        if class_base != None and class_base not in self.vtables.keys():
            raise Exception("La clase base no existe")
        
        # Verifica que la clase derivada no exista
        if class_derived in self.vtables.keys():
            raise Exception("La clase derivada ya existe")

        # Verifica que la clase derivada no sea la clase base
        if class_base == class_derived:
            raise Exception("La clase derivada no puede ser la clase base")

        # Verifica que todos los metodos dados son distintos
        if len(methods) != len(set(methods)):
            raise Exception("Los metodos no son distintos")


        # Crea la tabla de metodos virtuales
        self.vtables[class_derived] = {}

        # Agrega la clase base a la jerarquia de herencia
        self.inherit_hier[class_derived] = class_base

        # Define la tabla de metodos virtuales para la clase derivada
        for method in methods:
            self.vtables[class_derived][method] = class_derived

        # Copia los metodos de la clase base y de sus clases base (si aplica)
        if class_base != None:
            curr_class = class_base
            while curr_class != None:
                for method in self.vtables[curr_class].keys():
                    # Verifica que el metodo no haya sido definido en la clase
                    if method not in self.vtables[class_derived].keys():
                        self.vtables[class_derived][method] = self.vtables[curr_class][method]
                # Continua con la clase base
                curr_class = self.inherit_hier[curr_class]


        # Copia los metodos 
        #if class_base != None:
        #    for method in methods:
        #        # Verifica si el metodo existe en la clase base y en la clase
        #        # de la que se hereda (si aplica)
        #        curr_class = class_base
        #        found = False
        #        while curr_class != None:
        #            if method not in self.vtables[curr_class].keys():
        #                # curr_class no define el metodo, se continua con su
        #                # clase base
        #                curr_class = self.inherit_hier[curr_class]
        #            else:
        #                # curr_class define el metodo, se agrega a la tabla
        #                # de metodos virtuales
        #                self.vtables[class_derived][method] = curr_class
        #                found = True
        #                break

        #        if not found:
        #            # La clase derivada es la primera en definir el metodo
        #            self.vtables[class_derived][method] = class_derived
        #else:
        #    # La clase derivada es la clase base
        #    for method in methods:
        #        self.vtables[class_derived][method] = class_derived

        print(f"La tabla de metodos virtuales de {class_derived} fue creada con exito")

# Ejejmplo
vtable = VTable()
vtable.add(None, "A", ["foo", "baz"])
vtable.add("A", "B", ["foo"])
vtable.add("B", "C", ["bar"])

print(vtable.vtables)







