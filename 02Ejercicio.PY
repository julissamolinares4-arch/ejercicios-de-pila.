# Cear un programa en python que permita guardar el primer nombre de las personas.
# EJERCICIO 2: PILA DE NOMBRES


# 1. Función para agregar un nombre
def agregar_nombre(pila):
    nombre = input("Ingrese el primer nombre: ")

    pila.append(nombre)

    print("Nombre agregado correctamente.")


# 2. Función para eliminar un nombre
def eliminar_nombre(pila):
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        nombre = pila.pop()
        print("Nombre eliminado:", nombre)


# 3. Función para mostrar el último elemento
def mostrar_cima(pila):
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elemento en la cima:", pila[-1])


# 4. Función para buscar un elemento
def buscar_nombre(pila):
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in pila:
        print("El nombre sí se encuentra en la pila.")
    else:
        print("El nombre no se encuentra en la pila.")


# 5. Función para contar elementos
def contar_elementos(pila):
    cantidad = len(pila)

    print("La pila tiene", cantidad, "elemento(s).")


# 6. Función para mostrar todos los elementos
def mostrar_pila(pila):
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("\nElementos de la pila:")

        for nombre in reversed(pila):
            print(nombre)


# 7. Función para limpiar la pila
def limpiar_pila(pila):
    pila.clear()

    print("La pila ha sido limpiada.")


# Crear la pila
pila = []


# Menú principal
while True:

    print("\n***** MENU DE OPCIONES *****")
    print("1. Agregar un nombre a la Pila")
    print("2. Eliminar un nombre a la Pila")
    print("3. Mostrar el último elemento en la Cima")
    print("4. Buscar un elemento en la Pila")
    print("5. Contar cuantos elementos tiene la Pila")
    print("6. Mostrar todos los elementos de la Pila")
    print("7. Limpiar la Pila")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_nombre(pila)

    elif opcion == "2":
        eliminar_nombre(pila)

    elif opcion == "3":
        mostrar_cima(pila)

    elif opcion == "4":
        buscar_nombre(pila)

    elif opcion == "5":
        contar_elementos(pila)

    elif opcion == "6":
        mostrar_pila(pila)

    elif opcion == "7":
        limpiar_pila(pila)

    elif opcion == "8":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")