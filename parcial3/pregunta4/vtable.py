#  Manejador de tablas de tablas de metodos virtuales
# para un sistema orientado a objetos con herencia simple
# y despacho dinamico de metodos


class VTable:
    def __init__(self):
        self.vtables = {}  # { "clase" : { "metodo" : "clase que lo define" } }

    def run_simulation(self):
        while True:
            # Pide al usuario una accion (SE ASUME QUE EL USUARIO INGRESA UNA
            # ACCION VALIDA)
            action = input("Ingrese una accion: ")
            params = action.split(" ")

            if params[0].lower() == "class":
                # Verifica que el <tipo> es una expresion de
                # la forma <nombre> : <superclase>
                if ":" in params:
                    class_base = params[3]
                    methods = params[4:]
                else:
                    class_base = None
                    methods = params[2:]

                class_derived = params[1]

                # Agrega la clase
                try:
                    self.add(class_base, class_derived, methods)
                except Exception as e:
                    print(f"Error: {e}")

            elif params[0].lower() == "describir":
                # Imprime la tabla de metodos virtuales de la clase
                # dada
                try:
                    self.describe(params[1])
                except Exception as e:
                    print(f"Error: {e}")

            elif params[0].lower() == "salir":
                break

    def add(self, class_base, class_derived, methods):
        # Verica que la clase base exista (si aplica)
        if class_base != None and class_base not in self.vtables.keys():
            raise Exception("La clase base no existe")

        # Verifica que la clase derivada no sea la clase base
        if class_base == class_derived:
            raise Exception("La clase derivada y la clase base son la misma")

        # Verifica que la clase derivada no exista
        if class_derived in self.vtables.keys():
            raise Exception("La clase derivada ya existe")

        # Verifica que todos los metodos dados son distintos
        if len(methods) != len(set(methods)):
            raise Exception("Los metodos no son distintos")

        # Crea la tabla de metodos virtuales
        self.vtables[class_derived] = {}

        # Define la tabla de metodos virtuales para la clase derivada
        for method in methods:
            self.vtables[class_derived][method] = class_derived

        if class_base != None:
            # Copia los metodos de la clase base
            for method in self.vtables[class_base].keys():
                # Verifica que el metodo no haya sido definido en la clase
                if method not in self.vtables[class_derived].keys():
                    self.vtables[class_derived][method] = self.vtables[class_base][
                        method
                    ]

        # Copia los metodos de la clase base y de sus clases base (si aplica)
        #if class_base != None:
        #    curr_class = class_base
        #    while curr_class != None:
        #        for method in self.vtables[curr_class].keys():
        #            # Verifica que el metodo no haya sido definido en la clase
        #            if method not in self.vtables[class_derived].keys():
        #                self.vtables[class_derived][method] = self.vtables[curr_class][
        #                    method
        #                ]
        #        # Continua con la clase base
        #        curr_class = self.inherit_hier[curr_class]

        print(f"La tabla de metodos virtuales de {class_derived} fue creada con exito")

    def describe(self, class_name):
        if class_name not in self.vtables.keys():
            raise Exception("La clase no existe")

        for method, class_def in self.vtables[class_name].items():
            print(f" {method} -> {class_def} :: {method}")


if __name__ == "__main__":
    vtable = VTable()
    vtable.run_simulation()
