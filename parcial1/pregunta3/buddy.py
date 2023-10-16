# Implementacion del algoritmo Buddy System para la asignacion de memoria

from math import ceil, floor, log2


class Buddy:
    def __init__(self, memory_block_num: int):
        # Verifica que la cantidad de bloques de memoria sea un entero positivo
        # y que sea una potencia de dos
        if not isinstance(memory_block_num, int) or memory_block_num < 1:
            raise ValueError(
                "El numero de bloques de memoria debe ser un entero positivo"
            )
        elif not (memory_block_num & (memory_block_num - 1) == 0):
            raise ValueError(
                "El numero de bloques de memoria debe ser una potencia de dos"
            )

        max_pow_of_two = ceil(log2(memory_block_num))

        # Lista de listas de tuplas para trackear los bloques de memoria libres
        block_list = [[] for _ in range(max_pow_of_two + 1)]

        # El primer bloque de memoria libre es el bloque completo
        block_list[max_pow_of_two].append((0, memory_block_num - 1))

        # Propiedades de la clase
        self.block_list = block_list
        self.memory_block_num = memory_block_num
        self.name_list = {}

    def run_simulation(self):
        print("Manejador de memoria con el algoritmo Buddy System\n")
        print("Hay {} bloques de memoria\n".format(self.memory_block_num))

        # Inicia el ciclo de simulacion
        while True:
            action = input("Ingrese una accion: ")
            param = action.split(" ")
            first_param = param[0].upper()

            match first_param:
                case "LIBERAR":
                    if len(param) == 2:
                        # Si el nombre existe, se libera el espacio
                        if param[1] in self.name_list:
                            self.buddy_free(param[1])
                        else:
                            print("Error: El nombre no existe")
                    else:
                        print(
                            "Error: Los parametros no son validos, debe ser LIBERAR <nombre>"
                        )

                case "RESERVAR":
                    if len(param) == 3 and param[1].isdigit():
                        # Si el nombre no existe, se reserva el espacio
                        if param[1] not in self.name_list:
                            self.buddy_alloc((int(param[1]), param[2]))
                        else:
                            print("Error: El nombre ya existe")
                    else:
                        print(
                            "Error: Los parametros no son validos, debe ser RESERVAR <cantidad> <nombre>"
                        )

                case "MOSTRAR":
                    self.display()

                case "SALIR":
                    break

                case _:
                    print("Error: La accion no es valida")

    def buddy_alloc(self, cnt: int, name: str):
        # Verifica que cnt sea un entero
        if not isinstance(cnt, int) or cnt < 1:
            print("Error: Cantidad debe ser un entero positivo")
            return

        # Busca el indice del primer bloque libre del tamaño correcto
        n = floor(ceil(log2(cnt)))

        # Si hay un bloque libre del tamaño correcto, se reserva el espacio
        if len(self.block_list[n]) != 0:
            # Elimina el bloque de la lista de bloques libres
            avail_block = self.block_list[n].pop(0)
            # Agrega el bloque a la lista de bloques reservados con el nombre
            self.name_list[name] = avail_block
            print("\nEl bloque {} fue reservado en {}\n".format(name, avail_block))
            return

        i = n + 1

        # Si no hay un bloque libre del tamaño correcto, busca un bloque mas grande
        while i < len(self.block_list) and len(self.block_list[i]) == 0:
            i += 1

        if i == len(self.block_list):
            print("No hay bloques libres del tamaño correcto")
            return

        # Elimina el bloque de la lista de bloques libres
        block_to_split = self.block_list[i].pop(0)
        i -= 1

        # Separa el bloque en dos partes y las agrega a la lista de bloques
        # libres. La primera parte es el bloque a dividir o a reservar y la
        # segunda parte es el nuevo bloque libre
        while i >= n:
            lb = block_to_split[0]
            rb = block_to_split[1]

            new_block1 = (lb, lb + (rb - lb) // 2)
            new_block2 = (lb + (rb - lb + 1) // 2, rb)

            self.block_list[i].append(new_block1)
            self.block_list[i].append(new_block2)

            block_to_split = self.block_list[i].pop(0)
            i -= 1

        print("\nEl bloque {} fue reservado en {}\n".format(name, block_to_split))

        self.name_list[name] = block_to_split

    def buddy_free(self, name: str):
        # Verifica que el nombre exista
        if name not in self.name_list:
            print(
                "Error: Solicitud de liberacion invalida, el nombre: {} no esta reservado".format(
                    name
                )
            )
            return

        lb = self.name_list[name][0]
        rb = self.name_list[name][1]
        block_size = rb - lb + 1

        # Obtiene la lista que trackea los bloques libres de este tamaño
        list_to_free = int(ceil(log2(block_size)))
        self.block_list[list_to_free].append((lb, lb + (int(2**list_to_free) - 1)))

        print("\nBloque {} liberado\n".format(name))

        # buddyNumber and buddyAddrs
        buddy_num = lb / block_size

        if buddy_num % 2 != 0:
            buddy_addr = lb - int(2**list_to_free)
        else:
            buddy_addr = lb + int(2**list_to_free)

        # Busca el buddy en la lista de bloques libres
        i = 0
        while i < len(self.block_list[list_to_free]):
            # Si el buddy esta en la lista de bloques libres
            if self.block_list[list_to_free][i][0] == buddy_addr:
                # Buddy esta despues del bloque con esta direccion base
                if buddy_num % 2 == 0:
                    # Agrega el bloque a la lista de bloques libres
                    self.block_list[list_to_free + 1].append(
                        (lb, lb + (int(2**list_to_free) - 1))
                    )
                    print(
                        "Se realizo la fusion de bloques que comienzan en "
                        + str(lb)
                        + " y "
                        + str(buddy_addr)
                        + "\n"
                    )

                # Buddy es el bloque antes del bloque con esta direccion base
                else:
                    # Agrega el bloque a la lista de bloques libres
                    self.block_list[list_to_free + 1].append(
                        (buddy_addr, buddy_addr + 2 * int(2**list_to_free) - 1)
                    )
                    print(
                        "Se realizo la fusion de bloques que comienzan en {} y {}\n".format(
                            buddy_addr, lb
                        )
                    )

                # Elimina el bloque de la lista de bloques libres
                self.block_list[list_to_free].pop(i)
                self.block_list[list_to_free].pop()
                break
            i += 1

        self.name_list.pop(name)

    # Muestra una representacion grafica de la memoria
    def display(self):
        print("\nMemoria:")
        print("\nBloques de memoria permitidos:")
        print("Lista de bloques: {}".format(self.block_list))
        print("Nombre de bloques reservados, direccion base, direccion final:")
        print("Lista de nombres: {}".format(self.name_list))
