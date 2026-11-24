matriz = []
pago = []
vivienda = 0
mes = 0

while True:
    print(f"\n{'===':^25}MENU DE CONSUMO DE AGUA{'===':^25}\n")
    print(f"{'':^10}1. Ingresar cantidad de viviendas y meses")
    print(f"{'':^10}2. Capturar consumos de agua")
    print(f"{'':^10}3. Mostrar matriz de consumos")
    print(f"{'':^10}4. Calcular pagos y mayor consumo")
    print(f"{'':^10}5. Salir")
    op = int(input("\n\nIngresa una opcion (1-5): "))

    match op:
        case 1:
            print(f"\n\n=={'REGISTRO DE VIVIENDAS Y MESES':^30}==\n")
            vivienda = int(input("Ingresa la cantidad de viviendas: "))
            mes = int(input("Ingresa la cantidad de meses: "))
            matriz.clear()
            pago.clear()
            print(f"\nConfigurado: {vivienda} viviendas y {mes} meses.")
            print("Ahora use la opcion 2 para capturar los consumos.")

            input("\nPresione ENTER para continuar...")

        case 2:
            if vivienda <= 0 or mes <= 0:
                print("\nPrimero configure la cantidad de viviendas y meses (opcion 1).")
            else:
                print(f"\n\n=={'CAPTURA DE CONSUMOS':^30}==\n")
                matriz.clear()
                pago.clear()
                for f in range(vivienda):
                    fila = []
                    print(f"--- Vivienda {f + 1} ---")
                    for c in range(mes):
                        consumo = int(input(f"Consumo de la Vivienda {f + 1}, Mes {c + 1}: "))
                        fila.append(consumo)
                    matriz.append(fila)
                    print()
                print("Todos los consumos han sido capturados correctamente.")

            input("\nPresione ENTER para continuar...")

        case 3:
            if len(matriz) == 0:
                print("\nPrimero capture los consumos (opcion 2).")
            else:
                print(f"\n\n=={'TABLA DE CONSUMOS':^30}==\n")

                print(f"{'Vivienda':<12}", end="")
                for c in range(mes):
                    print(f"{'Mes ' + str(c + 1):^8}", end=" ")
                print()
                print("-" * (12 + (mes * 9)))

                for f in range(vivienda):
                    print(f"Vivienda {f + 1:<3} ", end="")
                    for c in range(mes):
                        print(f"{matriz[f][c]:^8}", end=" ")
                    print()
                print("-" * (12 + (mes * 9)))

            input("\nPresione ENTER para continuar...")

        case 4:
            if len(matriz) == 0:
                print("\nPrimero capture los consumos (opcion 2).")
            else:
                print(f"\n\n=={'CALCULO DE PAGOS':^30}==\n")
                pago.clear()
                for f in range(vivienda):
                    suma = 0
                    for c in range(mes):
                        suma += matriz[f][c]
                    pago.append(suma)
                    print(f"Vivienda {f + 1:>2} - Pago acumulado: ${suma}")

                indice = 0
                for i in range(len(pago)):
                    if pago[i] > pago[indice]:
                        indice = i

                print(f"\n=={'MAYOR CONSUMO':^30}==\n")
                print(f"La vivienda con mayor pago es la Vivienda {indice + 1} con un total de: ${pago[indice]}")

            input("\nPresione ENTER para continuar...")

        case 5:
            print("\nSaliendo del programa...")
            break

        case _:
            print("Opcion no valida")
            input("\nPresione ENTER para continuar...")
