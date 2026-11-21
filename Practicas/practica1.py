nombre = []
calificaciones = []
matriz = [
    [nombre],
    [calificaciones]
    ]
while True:
    print("1. Ingresar nombres de alumnos")
    print("2. Ingresar calificaciones de los alumnos")
    print("3. Mostrar resultados")
    print("4. Salir")
    menu = int(input("Ingresa un numero: "))
    match menu:
        case 1:
            while True:
                name = input("Ingresa el nombre del estudiante: ")
                if name == "salir":
                    break
                if "*" in name:
                    print("El nombre contiene caracteres invalidos, vuelva a ingresarlo")
                    continue
                print("Si ya completo los nombres escriba 'salir'")
                nombre.append(name)
            print (nombre)
        case 2:
            calificaciones.clear()
            for i in nombre:
                while True:
                    calif = int(input(f"Ingresa la calificacion de {i}: "))
                    if calif == 0:
                        print("La calificacion debe estar en un rango de 0-100!!")
                        continue
                    else:
                        break
                calificaciones.append(calif)
        case 3:
            prom = 0
            porc = 0
            porcr = 0
            conta = 0
            contb = 0
            for i in calificaciones:
                prom += i
            prom /= len(calificaciones)
            print(f"Promedio general del salon: {prom}")
            
            print("APROBARON")
            for i in range(len(calificaciones)):
                if calificaciones [i] >= 70:
                    print(f"{nombre[i]} tiene calificacion aprobatoria")
                    conta += 1
            porc = conta / len(calificaciones) * 100
            print(f"Aprobaron {conta} alumnos")
            print(f"Aprobo un {porc}% de alumnos")
            
            print("REPROBARON")
            for i in range(len(calificaciones)):
                if calificaciones [i] < 70:
                    print(f"{nombre[i]} tiene calificacion reprobatoria")
                    contb += 1
            porcr = contb / len(calificaciones) * 100
            print(f"Reprobaron {contb} alumnos")
            print(f"Reprobo un {porcr}% de alumnos")
            
            alto = calificaciones[0]
            bajo = calificaciones[0]
            pos = 0
            posb = 0
            print("Los siguientes alumnos tienen calificaciones iguales o mayores a 90")
            for i in range (len(calificaciones)):
                if calificaciones[i] > alto:
                    alto = calificaciones[i]
                    pos = i
                if calificaciones[i] < bajo:
                    bajo = calificaciones[i]
                    posb = i    
                if calificaciones[i] >= 90:
                    print(f"{nombre[i]} {calificaciones[i]}")
            print(f"Quien tiene mayor calificacion es: {nombre[pos]} con {alto}")
            print(f"Quien tiene menos calificacion es: {nombre[posb]} con {bajo}")
        case 4:
            break
        case _:
            print("Opcion no valida")
