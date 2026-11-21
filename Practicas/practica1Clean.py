nombre = []
calificaciones = []
while True:
    print(f"\n{'===':^23}MENU DE ALUMNOS{'===':^23}\n")
    print(f"{'':^10}1. Ingresar nombres de alumnos")
    print(f"{'':^10}2. Ingresar calificaciones de los alumnos")
    print(f"{'':^10}3. Mostrar resultados")
    print(f"{'':^10}4. Salir")
    menu = int(input("\n\nIngresa un numero del 1-4: "))
    match menu:
        case 1:
            print(f"\n\n=={'CAPTURA DE NOMBRES':^30}==")
            print("Si ya completo los nombres escriba 'salir'\n")
            while True:
                name = input("Ingresa el nombre del estudiante: ")
                if name == "salir":
                    break
                if "*" in name:
                    print("El nombre contiene caracteres invalidos, vuelva a ingresarlo")
                    continue
                nombre.append(name)
            print(f"\nAlumnos registrados: {nombre}")
        case 2:
            print(f"\n\n=={'CAPTURA DE CALIFICACIONES':^30}==\n")
            calificaciones.clear()
            for i in nombre:
                while True:
                    calif = int(input(f"Ingresa la calificacion de {i}: "))
                    if calif != 0:
                        break
                    print("La calificacion debe estar en un rango de 0-100!!")
                calificaciones.append(calif)
        case 3:
            total = len(calificaciones)
            prom = 0
            conta = 0
            pos = 0
            posb = 0
            for i in range(total):
                prom += calificaciones[i]
                if calificaciones[i] > calificaciones[pos]:
                    pos = i
                if calificaciones[i] < calificaciones[posb]:
                    posb = i
            print(f"\n\n=={'RESULTADOS':^30}==\n")
            print(f"Promedio general del salon: {prom / total:.2f}")

            print(f"\n=={'APROBARON':^30}==")
            for i in range(total):
                if calificaciones[i] >= 70:
                    print(f"{nombre[i]} tiene calificacion aprobatoria")
                    conta += 1
            porc = conta / total * 100
            print(f"Aprobaron {conta} alumnos\nAprobo un {porc:.2f}% de alumnos")

            print(f"\n=={'REPROBARON':^30}==")
            for i in range(total):
                if calificaciones[i] < 70:
                    print(f"{nombre[i]} tiene calificacion reprobatoria")
            contb = total - conta
            porcr = contb / total * 100
            print(f"Reprobaron {contb} alumnos\nReprobo un {porcr:.2f}% de alumnos")

            print(f"\n=={'CALIFICACION 90 O MAS':^30}==")
            for i in range(total):
                if calificaciones[i] >= 90:
                    print(f"{nombre[i]} {calificaciones[i]}")
            print(f"\nQuien tiene mayor calificacion es: {nombre[pos]} con {calificaciones[pos]}\nQuien tiene menos calificacion es: {nombre[posb]} con {calificaciones[posb]}")
        case 4:
            break
        case _:
            print("Opcion no valida")