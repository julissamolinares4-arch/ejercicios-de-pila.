#crear un proyecto en python que permita agregar numeros enteros a una pila y luego realice ;
#las siguientes operaciones:


numeros = []


def agregar_numeros():
    cantidad = int(input("¿Cuántos números desea agregar?: "))

    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    print("Números agregados correctamente.")


def contar_elementos():
    print("Cantidad de elementos:", len(numeros))


def mostrar_elementos():
    if len(numeros) == 0:
        print("No hay números en la lista.")
    else:
        print("Números registrados:")

        for numero in numeros:
            print(numero)


def promedio_numeros():
    if len(numeros) == 0:
        print("No hay números para calcular el promedio.")
    else:
        promedio = sum(numeros) / len(numeros)
        print("El promedio es:", promedio)


def menu():
    while True:
        print("\n***** MENÚ DE OPCIONES *****")
        print("1. Agregar números")
        print("2. Contar elementos")
        print("3. Mostrar todos los elementos")
        print("4. Promedio de todos los números")
        print("5. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_numeros()

        elif opcion == "2":
            contar_elementos()

        elif opcion == "3":
            mostrar_elementos()

        elif opcion == "4":
            promedio_numeros()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


menu()
