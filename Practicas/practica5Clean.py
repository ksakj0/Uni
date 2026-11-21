clave = []
desc = []
price = []
vector_claves = []
matriz_datos = []

while True:
    print(f"\n{'===':^25}MENU DE ARTICULOS{'===':^25}\n")
    print(f"{'':^10}1. Ingresar articulos")
    print(f"{'':^10}2. Consultar articulo")
    print(f"{'':^10}3. Modificar articulo")
    print(f"{'':^10}4. Eliminar articulo")
    print(f"{'':^10}5. Mostrar resultados y estadisticas")
    print(f"{'':^10}6. Pasar claves a un vector")
    print(f"{'':^10}7. Pasar datos a una matriz")
    print(f"{'':^10}8. Salir")
    op = int(input("\n\nIngresa una opcion (1-8): "))

    match op:
        case 1:
            print(f"\n\n=={'REGISTRO DE ARTICULOS':^30}==\n")
            size = int(input("Cuantos articulos desea ingresar? "))
            clave.clear()
            desc.clear()
            price.clear()

            for i in range(size):
                print(f"\n--- Articulo {i + 1} ---")
                c = input(f"Ingresa la clave del articulo {i + 1}: ")
                d = input("Ingresa la descripcion: ")
                p = float(input("Ingresa el precio: "))
                clave.append(c)
                desc.append(d)
                price.append(p)

            print("\nArticulos registrados correctamente:")
            print(f"Claves: {clave}")
            print(f"Descripciones: {desc}")
            print(f"Precios: {price}")

            input("\nPresione ENTER para continuar...")

        case 2:
            if len(clave) == 0:
                print("\nPrimero registre articulos (opcion 1).")
            else:
                print(f"\n\n=={'CONSULTA DE ARTICULO':^30}==\n")
                search = input("Ingresa la clave que desea consultar: ")
                encontrado = False

                for i in range(len(clave)):
                    if search == clave[i]:
                        print(f"\nClave: {clave[i]}")
                        print(f"Descripcion: {desc[i]}")
                        print(f"Precio: ${price[i]:.2f}")
                        encontrado = True
                        break

                if not encontrado:
                    print("Clave no encontrada.")

            input("\nPresione ENTER para continuar...")

        case 3:
            if len(clave) == 0:
                print("\nPrimero registre articulos (opcion 1).")
            else:
                print(f"\n\n=={'MODIFICAR ARTICULO':^30}==\n")
                search = input("Ingresa la clave que desea modificar: ")
                encontrado = False

                for i in range(len(clave)):
                    if search == clave[i]:
                        clave[i] = input(f"Ingresa la nueva clave del articulo {search}: ")
                        desc[i] = input("Ingresa la nueva descripcion: ")
                        price[i] = float(input("Ingresa el nuevo precio: "))
                        encontrado = True
                        print("\nArticulo modificado exitosamente.")
                        break

                if not encontrado:
                    print("Clave no encontrada.")
                else:
                    print(f"\nClaves actualizadas: {clave}")
                    print(f"Descripciones actualizadas: {desc}")
                    print(f"Precios actualizados: {price}")

            input("\nPresione ENTER para continuar...")

        case 4:
            if len(clave) == 0:
                print("\nPrimero registre articulos (opcion 1).")
            else:
                print(f"\n\n=={'ELIMINAR ARTICULO':^30}==\n")
                search = input("Ingresa la clave que desea eliminar: ")
                encontrado = False

                for i in range(len(clave)):
                    if search == clave[i]:
                        clave.pop(i)
                        desc.pop(i)
                        price.pop(i)
                        encontrado = True
                        print("\nArticulo eliminado exitosamente.")
                        break

                if not encontrado:
                    print("Clave incorrecta o no encontrada.")
                else:
                    print(f"\nClaves restantes: {clave}")
                    print(f"Descripciones restantes: {desc}")
                    print(f"Precios restantes: {price}")

            input("\nPresione ENTER para continuar...")

        case 5:
            if len(clave) == 0:
                print("\nPrimero registre articulos (opcion 1).")
            else:
                print(f"\n\n=={'RESULTADOS Y ESTADISTICAS':^30}==\n")
                mayor = price[0]
                suma = 0
                total = len(price)

                for i in range(total):
                    if price[i] > mayor:
                        mayor = price[i]
                    suma += price[i]

                promedio = suma / total

                print(f"Precio mayor registrado: ${mayor:.2f}")
                print(f"Promedio de precios: ${promedio:.2f}")

            input("\nPresione ENTER para continuar...")

        case 6:
            if len(clave) == 0:
                print("\nPrimero registre articulos (opcion 1).")
            else:
                print(f"\n\n=={'CLAVES A VECTOR':^30}==\n")
                vector_claves.clear()
                for i in range(len(clave)):
                    vector_claves.append(clave[i])

                print(f"Vector de claves ({len(vector_claves)} elementos):")
                print(vector_claves)

            input("\nPresione ENTER para continuar...")

        case 7:
            if len(clave) == 0:
                print("\nPrimero registre articulos (opcion 1).")
            else:
                print(f"\n\n=={'TABLA DE ARTICULOS (MATRIZ)':^30}==\n")
                matriz_datos.clear()
                for i in range(len(clave)):
                    fila = [clave[i], desc[i], price[i]]
                    matriz_datos.append(fila)

                # Formato de tabla limpia sin corchetes
                print(f"{'No.':<6} {'CLAVE':<12} {'DESCRIPCION':<25} {'PRECIO':<10}")
                print("-" * 55)
                for f in range(len(matriz_datos)):
                    num = f + 1
                    c_art = matriz_datos[f][0]
                    d_art = matriz_datos[f][1]
                    p_art = matriz_datos[f][2]
                    print(f"{num:<6} {c_art:<12} {d_art:<25} ${p_art:<10.2f}")
                print("-" * 55)

            input("\nPresione ENTER para continuar...")

        case 8:
            print("\nSaliendo del programa...")
            break

        case _:
            print("Opcion no valida")
            input("\nPresione ENTER para continuar...")
