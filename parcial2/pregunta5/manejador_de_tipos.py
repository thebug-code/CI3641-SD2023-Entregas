class ManejadorDeTipos:
    def __init__(self):
        self.atomics = {}
        self.unions = {}
        self.structs = {}

    def run_program(self):
        while True:
            action = input("Ingrese una acción: ")
            param = action.split(" ")
            type_action = param.pop(0).lower()

            if type_action == "atomico":
                if len(param) != 3:
                    print("Error: Numero de parametros invalido.")
                    continue
                if not param[1].isdigit() or not param[2].isdigit():
                    print("Error: <representacion> y <alineacion> deben ser enteros positivos.")
                    continue
                self.crear_atomico(param[0], int(param[1]), int(param[2]))

            elif type_action == "struct":
                if len(param) < 2:
                    print("Error: Numero de parametros invalido.")
                    continue
                nombre = param.pop(0)
                self.crear_struct(nombre, param)

            elif type_action == "union":
                if len(param) < 2:
                    print("Error: Numero de parametros invalido.")
                    continue
                nombre = param.pop(0)
                self.crear_union(nombre, param)

            elif type_action == "describir":
                if len(param) != 1:
                    print("Error: Numero de parametros invalido.")
                    continue
                self.describir_tipo(param[0])

            elif type_action == "salir":
                break

            else:
                print("Accion invalida")

    def crear_atomico(self, nombre, representacion, alineacion):
        if nombre in self.atomics or nombre in self.structs or nombre in self.unions:
            print("Error: El nombre del tipo ya existe.")
            return

        self.atomics[nombre] = self.Atomic(nombre, representacion, alineacion)
        print("Tipo atomico creado exitosamente.")

    def crear_struct(self, nombre, tipos):
        if nombre in self.structs or nombre in self.unions or nombre in self.atomics:
            print("Error: El nombre del tipo ya existe.")
            return

        packaging_tamanio = 0
        wasted_bytes = 0
        unpackaging_tamanio = 0
        max_align = 0

        for nombre_tipo in tipos:
            if nombre_tipo in self.atomics:
                packaging_tamanio += self.atomics[nombre_tipo].representation
                packaging_tamanio += self.atomics[nombre_tipo].alineacion
                if self.atomics[nombre_tipo].alineacion > max_align:
                    max_align = self.atomics[nombre_tipo].alineacion
                if unpackaging_tamanio % self.atomics[nombre_tipo].alineacion == 0:
                    unpackaging_tamanio += self.atomics[nombre_tipo].representation
                else:
                    wasted_bytes += unpackaging_tamanio % self.atomics[nombre_tipo].alineacion
                    unpackaging_tamanio += unpackaging_tamanio % self.atomics[nombre_tipo].alineacion
                    unpackaging_tamanio += self.atomics[nombre_tipo].representation

            elif nombre_tipo in self.structs:
                packaging_tamanio += self.structs[nombre_tipo].tamanio
                if self.structs[nombre_tipo].alineacion > max_align:
                    max_align = self.structs[nombre_tipo].alineacion
                if unpackaging_tamanio % self.structs[nombre_tipo].alineacion == 0:
                    unpackaging_tamanio += self.structs[nombre_tipo].tamanio
                else:
                    wasted_bytes += unpackaging_tamanio % self.structs[nombre_tipo].alineacion
                    unpackaging_tamanio += unpackaging_tamanio % self.structs[nombre_tipo].alineacion
                    unpackaging_tamanio += self.structs[nombre_tipo].tamanio

            elif nombre_tipo in self.unions:
                packaging_tamanio += self.unions[nombre_tipo].tamanio
                if self.unions[nombre_tipo].alineacion > max_align:
                    max_align = self.unions[nombre_tipo].alineacion
                if unpackaging_tamanio % self.unions[nombre_tipo].alineacion == 0:
                    unpackaging_tamanio += self.unions[nombre_tipo].tamanio
                else:
                    wasted_bytes += unpackaging_tamanio % self.unions[nombre_tipo].alineacion
                    unpackaging_tamanio += unpackaging_tamanio % self.unions[nombre_tipo].alineacion
                    unpackaging_tamanio += self.unions[nombre_tipo].tamanio

            else:
                print("Error: El nombre del tipo no existe.")
                return

        self.structs[nombre] = self.Struct(nombre, tipos, [unpackaging_tamanio, packaging_tamanio], [max_align, 1], wasted_bytes)
        print("Tipo struct creado exitosamente.")

    def crear_union(self, nombre, tipos):
        if nombre in self.unions or nombre in self.structs or nombre in self.atomics:
            print("Error: El nombre del tipo ya existe.")
            return
        max_tamanio = 0
        max_align = 0
        for nombre_tipo in tipos:
            if nombre_tipo in self.atomics:
                if self.atomics[nombre_tipo].representation > max_tamanio:
                    max_tamanio = self.atomics[nombre_tipo].representation
                    max_align = self.atomics[nombre_tipo].alineacion
            elif nombre_tipo in self.structs:
                if self.structs[nombre_tipo].tamanio[1] > max_tamanio:
                    max_tamanio = self.structs[nombre_tipo].tamanio[1]
                    max_align = self.structs[nombre_tipo].alineacion[1]
            elif nombre_tipo in self.unions:
                if self.unions[nombre_tipo].tamanio > max_tamanio:
                    max_tamanio = self.unions[nombre_tipo].tamanio
                    max_align = self.unions[nombre_tipo].alineacion
            else:
                print("Error: El nombre del tipo no existe.")
                return

        self.unions[nombre] = self.Union(nombre, tipos, max_tamanio, max_align)
        print("Tipo union creado exitosamente.")

    def describir_tipo(self, nombre):
        if nombre in self.atomics:
            print(self.atomics[nombre].describe())
        elif nombre in self.structs:
            print(self.structs[nombre].describe())
        elif nombre in self.unions:
            print(self.unions[nombre].describe())
        else:
            print("Error: El nombre del tipo no existe.")

    class Atomic:

        def __init__(self, nombre: str, representation: int, alineacion: int):
            self.nombre = nombre
            self.representation = representation
            self.alineacion = alineacion

        def describe(self):
            str_to_prt = ""
            str_to_prt += "Nombre: " + self.nombre + "\n"
            str_to_prt += "Tamanio: " + str(self.representation) + "\n"
            str_to_prt += "Alineacion: " + str(self.alineacion) + "\n"
            str_to_prt += "Bytes desperdiciados: " + str(self.representation % self.alineacion) + "\n"
            return str_to_prt

    class Union:

        def __init__(self, nombre: str, tipos: list, tamanio: int, alineacion: int):
            self.nombre = nombre
            self.tipos = tipos
            self.tamanio = tamanio
            self.alineacion = alineacion

        def describe(self):

            str_to_prt = ""
            str_to_prt += "Nombre: " + self.nombre + "\n"
            str_to_prt += "Tamanio: " + str(self.tamanio) + "\n"
            str_to_prt += "Alineacion: " + str(self.alineacion) + "\n"
            str_to_prt += "Bytes desperdiciados: " + str(self.tamanio % self.alineacion) + "\n"

            return str_to_prt
    class Struct:

        def __init__(self, nombre: str, tipos: list, tamanio: list, alineacion: list, wasted_bytes: int):
            self.nombre = nombre
            self.tipos = tipos
            self.tamanio = tamanio
            self.alineacion = alineacion
            self.wasted_bytes = wasted_bytes

        def describe(self):
            str_to_prt = ""
            str_to_prt += "Nombre: " + self.nombre + "\n" \
                        + "UnPackaging\n" \
                        + "     Tamanio: " + str(self.tamanio[0]) + "\n" \
                        + "     Alineacion: " + str(self.alineacion[0]) + "\n" \
                        + "     Bytes desperdiciados: " + str(self.wasted_bytes) + "\n" \
                        + "Packaging\n" \
                        + "     Tamanio: " + str(self.tamanio[1]) + "\n" \
                        + "     Alineacion: 1\n" \
                        + "     Bytes desperdiciados: 0\n"
            return str_to_prt
