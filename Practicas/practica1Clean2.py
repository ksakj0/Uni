estudiantes = []
notas = []

while True:
    print(f"\n{'===':^23}MENU DE ALUMNOS{'===':^23}\n")
    print(f"{'':^10}1. Ingresar nombres de alumnos")
    print(f"{'':^10}2. Ingresar calificaciones de los alumnos")
    print(f"{'':^10}3. Mostrar resultados")
    print(f"{'':^10}4. Salir")
    opcion = int(input("\n\nIngresa una opcion (1-4): "))

    match opcion:
        case 1:
            print(f"\n\n=={'CAPTURA DE ALUMNOS':^30}==")
            print("Escriba 'salir' cuando termine de registrar\n")
            while True:
                alumno = input("Ingresa el nombre del alumno: ")
                if alumno == "salir":
                    break
                if "*" in alumno:
                    print("Nombre no valido, contiene asterisco (*)")
                    continue
                estudiantes.append(alumno)
            print(f"\nEstudiantes en la lista: {estudiantes}")

        case 2:
            print(f"\n\n=={'CAPTURA DE CALIFICACIONES':^30}==\n")
            notas.clear()
            for al in estudiantes:
                while True:
                    cal = int(input(f"Ingresa la calificacion de {al}: "))
                    if cal >= 0 and cal <= 100:
                        break
                    print("La calificacion debe estar en un rango de 0-100!!")
                notas.append(cal)

        case 3:
            total_alumnos = len(notas)
            if total_alumnos == 0:
                print("\nNo hay calificaciones capturadas todavia.")
            else:
                suma = 0
                aprobados = 0
                reprobados = 0
                mayor = notas[0]
                menor = notas[0]
                pos_max = 0
                pos_min = 0

                for i in range(total_alumnos):
                    suma += notas[i]
                    if notas[i] > mayor:
                        mayor = notas[i]
                        pos_max = i
                    if notas[i] < menor:
                        menor = notas[i]
                        pos_min = i

                promedio = suma / total_alumnos

                print(f"\n\n=={'RESULTADOS':^30}==\n")
                print(f"Promedio general del salon: {promedio:.2f}")

                print(f"\n=={'APROBARON':^30}==")
                for i in range(total_alumnos):
                    if notas[i] >= 70:
                        print(f"{estudiantes[i]} tiene calificacion aprobatoria")
                        aprobados += 1
                porc_aprob = aprobados / total_alumnos * 100
                print(f"Aprobaron {aprobados} alumnos\nAprobo un {porc_aprob:.2f}% de alumnos")

                print(f"\n=={'REPROBARON':^30}==")
                for i in range(total_alumnos):
                    if notas[i] < 70:
                        print(f"{estudiantes[i]} tiene calificacion reprobatoria")
                        reprobados += 1
                porc_reprob = reprobados / total_alumnos * 100
                print(f"Reprobaron {reprobados} alumnos\nReprobo un {porc_reprob:.2f}% de alumnos")

                print(f"\n=={'CALIFICACION 90 O MAS':^30}==")
                for i in range(total_alumnos):
                    if notas[i] >= 90:
                        print(f"{estudiantes[i]} {notas[i]}")

                print(f"\nQuien tiene mayor calificacion es: {estudiantes[pos_max]} con {notas[pos_max]}")
                print(f"Quien tiene menos calificacion es: {estudiantes[pos_min]} con {notas[pos_min]}")

        case 4:
            print("\nSaliendo del programa...")
            break

        case _:
            print("Opcion no valida")
