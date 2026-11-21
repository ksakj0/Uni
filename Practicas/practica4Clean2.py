tam = 3
matriz = []
for i in range(tam):
    fila = []
    for j in range(tam):
        fila.append(None)
    matriz.append(fila)

capturado = False

while True:
    print(f"\n{'===':^25}MENU DE ESTATURAS{'===':^25}\n")
    print(f"{'':^12}1. Registrar estaturas")
    print(f"{'':^12}2. Eliminar una estatura")
    print(f"{'':^12}3. Modificar una estatura")
    print(f"{'':^12}4. Sumar diagonal principal")
    print(f"{'':^12}5. Mostrar estatura central")
    print(f"{'':^12}6. Convertir a vector")
    print(f"{'':^12}7. Mayor y menor estatura")
    print(f"{'':^12}8. Salir\n")
    opcion = input("Elige una opcion (1-8): ")

    match opcion:
        case "1":
            for f in range(tam):
                for c in range(tam):
                    matriz[f][c] = float(input(f"Ingresa la estatura de la posicion [{f + 1}][{c + 1}]: "))
            capturado = True

            print("\nMatriz de estaturas:")
            for f in range(tam):
                for c in range(tam):
                    if matriz[f][c] is not None:
                        print(f"{matriz[f][c]:.2f}\t", end="")
                    else:
                        print("-\t", end="")
                print()

        case "2":
            if not capturado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                f_elim = int(input("Fila a eliminar (1-3): ")) - 1
                c_elim = int(input("Columna a eliminar (1-3): ")) - 1

                if f_elim >= 0 and f_elim < tam and c_elim >= 0 and c_elim < tam:
                    if matriz[f_elim][c_elim] is not None:
                        print(f"Eliminando: {matriz[f_elim][c_elim]:.2f}")
                        matriz[f_elim][c_elim] = None
                    else:
                        print("Esa casilla ya estaba vacia.")

                    print("\nMatriz actual:")
                    for f in range(tam):
                        for c in range(tam):
                            if matriz[f][c] is not None:
                                print(f"{matriz[f][c]:.2f}\t", end="")
                            else:
                                print("-\t", end="")
                        print()
                else:
                    print("Posicion invalida.")

        case "3":
            if not capturado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                f_mod = int(input("Fila a modificar (1-3): ")) - 1
                c_mod = int(input("Columna a modificar (1-3): ")) - 1

                if f_mod >= 0 and f_mod < tam and c_mod >= 0 and c_mod < tam:
                    print(f"Valor actual: {matriz[f_mod][c_mod]}")
                    matriz[f_mod][c_mod] = float(input("Nueva estatura: "))

                    print("\nMatriz actualizada:")
                    for f in range(tam):
                        for c in range(tam):
                            if matriz[f][c] is not None:
                                print(f"{matriz[f][c]:.2f}\t", end="")
                            else:
                                print("-\t", end="")
                        print()
                else:
                    print("Posicion invalida.")

        case "4":
            if not capturado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                suma_diag = 0
                for i in range(tam):
                    if matriz[i][i] is not None:
                        suma_diag += matriz[i][i]
                print(f"Suma de la diagonal principal: {suma_diag:.2f}")

        case "5":
            if not capturado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                if tam % 2 == 1:
                    medio = tam // 2
                    print(f"Posicion central: fila {medio + 1}, columna {medio + 1}")
                    if matriz[medio][medio] is not None:
                        print(f"Estatura central: {matriz[medio][medio]:.2f}")
                    else:
                        print("Estatura central no registrada.")
                else:
                    print("La matriz no tiene centro unico (dimension par).")

        case "6":
            if not capturado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                vector_resultado = []
                for f in range(tam):
                    for c in range(tam):
                        vector_resultado.append(matriz[f][c])
                print(f"Vector: {vector_resultado}")

        case "7":
            if not capturado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                valores = []
                for f in range(tam):
                    for c in range(tam):
                        if matriz[f][c] is not None:
                            valores.append(matriz[f][c])

                if len(valores) > 0:
                    alto = valores[0]
                    bajo = valores[0]
                    for v in valores:
                        if v > alto:
                            alto = v
                        if v < bajo:
                            bajo = v
                    print(f"Mayor: {alto:.2f}\nMenor: {bajo:.2f}")
                else:
                    print("No hay estaturas registradas.")

        case "8":
            print("Saliendo...")
            break

        case _:
            print("Opcion invalida. Intente de nuevo.")
