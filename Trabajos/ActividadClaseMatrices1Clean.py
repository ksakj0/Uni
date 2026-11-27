matriz = []
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
            matriz = []
            print(f"\nConfigurado: {vivienda} viviendas y {mes} meses.")
            print("Ahora use la opcion 2 para capturar los consumos.")

            input("\nPresione ENTER para continuar...")

        case 2:
            if vivienda <= 0 or mes <= 0:
                print("\nPrimero configure la cantidad de viviendas y meses (opcion 1).")
            else:
                print(f"\n\n=={'CAPTURA DE CONSUMOS':^30}==\n")
                matriz = [None] * vivienda
                for f in range(vivienda):
                    matriz[f] = [0] * mes
                    print(f"--- Vivienda {f + 1} ---")
                    for c in range(mes):
                        consumo = int(input(f"Consumo de la Vivienda {f + 1}, Mes {c + 1}: "))
                        matriz[f][c] = consumo
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
                separador = "-" * (12 + mes * 9)
                print(separador)

                for f in range(vivienda):
                    print(f"Vivienda {f + 1:<3} ", end="")
                    for c in range(mes):
                        print(f"{matriz[f][c]:^8}", end=" ")
                    print()
                print(separador)

            input("\nPresione ENTER para continuar...")

        case 4:
            if len(matriz) == 0:
                print("\nPrimero capture los consumos (opcion 2).")
            else:
                print(f"\n\n=={'CALCULO DE PAGOS':^30}==\n")
                mayor_pago = 0
                vivienda_mayor = 1
                for f in range(vivienda):
                    suma = 0
                    for c in range(mes):
                        suma += matriz[f][c]
                    print(f"Vivienda {f + 1:>2} - Pago acumulado: ${suma}")

                    if f == 0 or suma > mayor_pago:
                        mayor_pago = suma
                        vivienda_mayor = f + 1

                print(f"\n=={'MAYOR CONSUMO':^30}==\n")
                print(f"La vivienda con mayor pago es la Vivienda {vivienda_mayor} con un total de: ${mayor_pago}")

            input("\nPresione ENTER para continuar...")

        case 5:
            print("\nSaliendo del programa...")
            break

        case _:
            print("Opcion no valida")
            input("\nPresione ENTER para continuar...")
