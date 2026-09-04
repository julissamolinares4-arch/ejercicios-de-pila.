
# SISTEMA DE ATENCION DE PEDIDOS EN UN RESTAURANTE

pila = []

producto_eliminado = ""

while True:

    print("\n================================================")
    print("     SISTEMA DE ATENCION DE PEDIDOS")
    print("================================================")
    print("1. Ver menu")
    print("2. Agregar producto (PUSH)")
    print("3. Eliminar producto (POP)")
    print("4. Ver pedido")
    print("5. Ver ultimo producto agregado")
    print("6. Ver producto eliminado")
    print("7. Salir")
    print("================================================")

    opcion = input("Seleccione una opcion: ")


    if opcion == "1":

        print("\n================ MENU =================")
        print("1. Papas fritas")
        print("2. Tacos")
        print("3. Enchilada")
        print("4. Tajada con queso")
        print("5. Gaseosa")
        print("6. Jugo natural")
        print("7. Raptor")
        print("8. Fury")
       
    elif opcion == "2":

        print("\nSeleccione un producto:")
        print("1. Papas fritas")
        print("2. Tacos")
        print("3. Enchilada")
        print("4. Tajada con queso")
        print("5. Gaseosa")
        print("6. Jugo natural")
        print("7. Raptor")
        print("8. Fury")

        producto = input("Producto: ")

        if producto == "1":
            pila.append("Papas fritas")
            print("Producto agregado.")

        elif producto == "2":
            pila.append("Tacos")
            print("Producto agregado.")

        elif producto == "3":
            pila.append("Enchilada")
            print("Producto agregado.")

        elif producto == "4":
            pila.append("Tajada con queso")
            print("Producto agregado.")

        elif producto == "5":
            pila.append("Gaseosa")
            print("Producto agregado.")

        elif producto == "6":
            pila.append("Jugo natural")
            print("Producto agregado.")

        elif producto == "7":
            pila.append("Raptor")
            print("Producto agregado.")

        elif producto == "8":
            pila.append("Fury")
            print("Producto agregado.")

        else:
            print("Opcion incorrecta.")

    elif opcion == "3":

        if len(pila) > 0:

            producto_eliminado = pila.pop()

            print("\nProducto eliminado:", producto_eliminado)

        else:
            print("\nNo hay productos para eliminar.")

    elif opcion == "4":

        if len(pila) > 0:

            print("\n============== MI PEDIDO ==============")

            for producto in reversed(pila):
                print("-", producto)
                
        else:
            print("\nEl pedido esta vacio.")

    elif opcion == "5":

        if len(pila) > 0:

            print("\nUltimo producto agregado:", pila[-1])

        else:
            print("\nNo hay productos agregados.")

    elif opcion == "6":

        if producto_eliminado != "":
            print("\nProducto eliminado:", producto_eliminado)

        else:
            print("\nTodavia no se ha eliminado ningun producto.")

    
    elif opcion == "7":

        print("\n================================================")
        print("     GRACIAS POR VISITAR NUESTRO RESTAURANTE")
        print("================================================")

        break

    else:
        print("\nOpcion incorrecta.")


 