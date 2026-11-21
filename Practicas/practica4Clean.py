fila = 3
column = fila
est = []
for _ in range(fila):
    est.append([None] * column)
registrado = False


def imprimir_matriz():
    for f in range(fila):
        for c in range(column):
            if est[f][c] is not None:
                print(f"{est[f][c]:.2f}	", end="") 
            else:
                print("-	", end="")
        print()


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
    op = input("Elige una opcion (1-8): ")

    match op:
        case "1":
            for f in range(fila):
                for c in range(column):
                    est[f][c] = float(input(f"Ingrese estatura [{f+1}][{c+1}]: "))
            registrado = True
            imprimir_matriz()

        case "2":
            if not registrado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                a = int(input("Fila a eliminar (1-3): ")) - 1
                b = int(input("Columna a eliminar (1-3): ")) - 1
                if 0 <= a < fila and 0 <= b < column:
                    print(f"Eliminando: {est[a][b]:.2f}")
                    est[a][b] = None
                    imprimir_matriz()
                else:
                    print("Posicion invalida.")

        case "3":
            if not registrado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                a = int(input("Fila a modificar (1-3): ")) - 1
                b = int(input("Columna a modificar (1-3): ")) - 1
                if 0 <= a < fila and 0 <= b < column:
                    print(f"Valor actual: {est[a][b]}")
                    est[a][b] = float(input("Nueva estatura: "))
                    imprimir_matriz()
                else:
                    print("Posicion invalida.")

        case "4":
            if not registrado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                suma = 0
                for f in range(fila):
                    if est[f][f] is not None:
                        suma += est[f][f]
                print(f"Suma de la diagonal principal: {suma:.2f}")

        case "5":
            if not registrado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                l = len(est)
                if l % 2 == 1:
                    medio = l // 2
                    print(f"Posicion central: fila {medio + 1}, columna {medio + 1}")
                    if est[medio][medio] is not None:
                        print(f"Estatura central: {est[medio][medio]:.2f}")
                    else:
                        print("Estatura central no registrada.")
                else:
                    print("La matriz no tiene centro unico (dimension par).")

        case "6":
            if not registrado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                vector = []
                for f in range(fila):
                    for c in range(column):
                        vector.append(est[f][c])
                print(f"Vector: {vector}")

        case "7":
            if not registrado:
                print("Primero registre las estaturas (opcion 1).")
            else:
                vector = []
                for f in range(fila):
                    for c in range(column):
                        vector.append(est[f][c])
                valores = [v for v in vector if v is not None]
                if valores:
                    alto = max(valores)
                    bajo = min(valores)
                    print(f"Mayor: {alto:.2f}\nMenor: {bajo:.2f}")
                else:
                    print("No hay estaturas registradas.")

        case "8":
            print("Saliendo...")
            break

        case _:
            print("Opcion invalida. Intente de nuevo.")