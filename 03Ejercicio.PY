from collections import deque


class PilaDeque:

    def __init__(self):
        self._items = deque()

    def push(self, departamento):
        self._items.append(departamento)

    
    def pop(self):
        if len(self._items) > 0:
            return self._items.pop()
        else:
            return None

    def mostrar(self):
        if len(self._items) == 0:
            print("La pila está vacía.")
        else:
            print("\nDepartamentos en la pila:")
            for departamento in reversed(self._items):
                print(departamento)

pila = PilaDeque()

departamentos_nicaragua = [
    "Boaco",
    "Carazo",
    "Chinandega",
    "Chontales",
    "Estelí",
    "Granada",
    "Jinotega",
    "León",
    "Madriz",
    "Managua",
    "Masaya",
    "Matagalpa",
    "Nueva Segovia",
    "Río San Juan",
    "Rivas"
]

while True:

    print("\n===== MENÚ DE PILA =====")
    print("1. Agregar departamento")
    print("2. Remover departamento")
    print("3. Imprimir pila")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        departamento = input("Ingrese el nombre del departamento: ")

        if departamento in departamentos_nicaragua:
            pila.push(departamento)
            print("Departamento agregado correctamente.")
        else:
            print("Ese nombre no corresponde a un departamento de Nicaragua.")

    elif opcion == "2":

        departamento = pila.pop()

        if departamento is not None:
            print("Departamento removido:", departamento)
        else:
            print("La pila está vacía.")

    elif opcion == "3":

        pila.mostrar()

    elif opcion == "4":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida.")