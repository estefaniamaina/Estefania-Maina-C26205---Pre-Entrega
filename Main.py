productos = []    # [[Nombre],[Categoria],[Precio]]
while True:
    print("="*31)  # ===============================
    print("Sistema de Gestion de Productos")
    print("="*31)  # ===============================
    print("1.Agregar producto\n2.Mostrar productos\n3.Buscar producto\n4.Eliminar producto\n5.Salir")

    opt = input("Elija una opcion (1-5): ").strip()    # Strip para quitar los espacios que pueda colocar el usuario

    if opt == "1":
        print(">>> Agregar producto <<<")
        # VALIDACION DE DATOS #
        nombre = input("Nombre del producto: ").strip()
        while nombre == "":   # Bucle While: solo se ejecuta el bucle cuando el dato ingresado es verdadero, no vacío
            print("Error: no ingreso el producto")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoria del producto: ").strip()
        while categoria == "":   
            print("Error: no ingreso la categoria")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio del producto (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: ingresar numero entero")
            precio_str = input("Precio del producto (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)


    elif opt == "2":
        print(">>> Lista de productos <<<")   # Lista con listas dentro - Con Indices
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            for i in range(len(productos)):   # 3: 0, 1, 2  --> i = 0, i = 1, i = 2
                print(f"{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
    
    
    elif opt == "3":
        print(">>> Buscar producto <<<")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            busqueda = input("Nombre del producto buscado: ").strip().lower()
            while busqueda == "":
                print("Error: No ingreso el producto")
                busqueda = input("Nombre del producto buscado: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    encontrado += 1
            if encontrado == 0:
                print("No se encontraron resultados")
            else:
                print(f"Productos encontrados {encontrado}")


    elif opt == "4":
        print(">>> Eliminar producto <<<")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            for i in range(len(productos)):
                print(f"{i+1}.{productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")

            id_eliminar = input("Numero de producto a eliminar: ").strip()
            while not id_eliminar.isdigit():
                print("Error: no ingreso un numero valido")
                id_eliminar = input("Numero de producto a eliminar: ").strip()
            posicion = int(id_eliminar) - 1
            eliminado = productos.pop(posicion)
            print(f"Eliminado correctamente: {eliminado[0]}")


    elif opt == "5":
        print("Gracias por utilizar nuestro sistema de gestion")
        break
    else:
        print("Error: opcion incorrecta")