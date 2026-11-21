pc = 0
pcv = []

while True:
    print(f"\n{'===':^23}MENU DE COMPUTADORAS{'===':^23}\n")
    print(f"{'':^10}1. Ingresar cantidad de computadoras")
    print(f"{'':^10}2. Ingresar tiempo de uso")
    print(f"{'':^10}3. Mostrar lista de computadoras")
    print(f"{'':^10}4. Mostrar resultados")
    print(f"{'':^10}5. Salir")
    op = int(input("\n\nIngresa un numero del 1-5: "))

    match op:
        case 1:
            print(f"\n\n=={'REGISTRO DE COMPUTADORAS':^30}==\n")
            pc = int(input("Ingrese la cantidad de computadoras disponibles: "))
            pcv = [0] * pc
            print(f"\nComputadoras registradas: {pc}")
            print(f"\n=={'LISTA DE COMPUTADORAS':^30}==\n")
            for r, fila in enumerate(pcv):
                if r + 1 < 10:
                    print(f"Computadora {r + 1}  {fila}")
                else:
                    print(f"Computadora {r + 1} {fila}")
            
            print("\n")
            input("Presione ENTER para continuar...")

        case 2:
            print(f"\n\n=={'CAPTURA DE TIEMPOS':^30}==\n")
            for f in range(pc):
                pcv[f] = int(input(f"Ingrese el tiempo de uso en minutos para la computadora [{f + 1}]: "))
            print("\nTiempos registrados correctamente")
            
            print("\n")
            input("Presione ENTER para continuar...")

        case 3:
            print(f"\n\n=={'LISTA DE COMPUTADORAS':^30}==\n")
            for r, fila in enumerate(pcv):
                if r + 1 < 10:
                    print(f"Computadora{r + 1}  {fila}")
                else:
                    print(f"Computadora {r + 1} {fila}")
            
            print("\n")
            input("Presione ENTER para continuar...")
        case 4:
            suma = 0
            for i in range(pc):
                suma += pcv[i]
            promedio = suma / len(pcv)

            print(f"\n\n=={'RESULTADOS':^30}==\n")
            print(f"Tiempo total en minutos: {suma} min")
            print(f"Tiempo total en horas: {suma / 60:.2f} hrs")
            print(f"Promedio de tiempo de uso: {promedio:.2f} min")

            print("\n")
            input("Presione ENTER para continuar...")
            
        case 5:
            print("\nSaliendo del programa...")
            break

        case _:
            print("\nOpcion no valida")
