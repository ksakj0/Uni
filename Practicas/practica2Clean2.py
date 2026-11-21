import random as r

vector1 = []
vector2 = []
vector3 = []

while True:
    print(f"\n{'===':^23}MENU DE VECTORES{'===':^23}\n")
    print(f"{'':^10}1. Llenar el primer vector con numeros aleatorios")
    print(f"{'':^10}2. Llenar el segundo vector con numeros aleatorios")
    print(f"{'':^10}3. Sumar ambos")
    print(f"{'':^10}4. Resultados")
    print(f"{'':^10}5. Salir")
    op = int(input("\n\nIngresa una de las 5 opciones: "))

    match op:
        case 1:
            cantidad = int(input("\n\nCuantos numeros aleatorios se deberian generar? "))
            vector1.clear()
            vector2.clear()
            vector3.clear()
            for i in range(cantidad):
                vector1.append(r.randint(100, 1000))
            print(f"\nVector 1: {vector1}")

        case 2:
            if len(vector1) == 0:
                print("\n\nPrimero llene el vector 1 (opcion 1)")
            else:
                vector2.clear()
                vector3.clear()
                for i in range(len(vector1)):
                    vector2.append(r.randint(100, 1000))
                print(f"\nVector 2: {vector2}")

        case 3:
            if len(vector1) == 0 or len(vector1) != len(vector2):
                print("\n\nLlene ambos vectores con la misma cantidad de numeros")
            else:
                vector3.clear()
                for i in range(len(vector1)):
                    vector3.append(vector1[i] + vector2[i])
                print(f"\n\n=={'SUMA DE VECTORES':^30}==\n")
                print(f"Vector 1: {vector1}\nVector 2: {vector2}\nSu suma: {vector3}")

        case 4:
            if len(vector3) == 0:
                print("\n\nPrimero llene ambos vectores y sumelos (opcion 3)")
            else:
                tam = len(vector1)

                print(f"\n\n=={'REPETIDOS':^30}==\n")
                vistos1 = []
                hay1 = False
                for i in range(tam):
                    num = vector1[i]
                    if num not in vistos1:
                        veces = vector1.count(num)
                        if veces > 1:
                            print(f"{num} aparece {veces} veces en Vector 1")
                            hay1 = True
                        vistos1.append(num)
                if not hay1:
                    print("Ningun numero se repite en Vector 1")

                vistos2 = []
                hay2 = False
                for i in range(tam):
                    num = vector2[i]
                    if num not in vistos2:
                        veces = vector2.count(num)
                        if veces > 1:
                            print(f"{num} aparece {veces} veces en Vector 2")
                            hay2 = True
                        vistos2.append(num)
                if not hay2:
                    print("Ningun numero se repite en Vector 2")

                mayor1 = vector1[0]
                menor1 = vector1[0]
                mayor2 = vector2[0]
                menor2 = vector2[0]
                mayor3 = vector3[0]
                menor3 = vector3[0]
                suma_total = 0

                for i in range(tam):
                    if vector1[i] > mayor1:
                        mayor1 = vector1[i]
                    if vector1[i] < menor1:
                        menor1 = vector1[i]

                    if vector2[i] > mayor2:
                        mayor2 = vector2[i]
                    if vector2[i] < menor2:
                        menor2 = vector2[i]

                    if vector3[i] > mayor3:
                        mayor3 = vector3[i]
                    if vector3[i] < menor3:
                        menor3 = vector3[i]

                    suma_total += vector3[i]

                promedio = suma_total / tam

                print(f"\n=={'MAYORES Y MENORES':^30}==\n")
                print(f"Mayor -> Vector 1: {mayor1} | Vector 2: {mayor2} | Suma: {mayor3}")
                print(f"Menor -> Vector 1: {menor1} | Vector 2: {menor2} | Suma: {menor3}")
                print(f"\nPromedio de la suma: {promedio:.2f}")

                print(f"\n=={'PRIMERO Y ULTIMO':^30}==\n")
                print(f"Vector 1: {vector1[0]} y {vector1[-1]}\nVector 2: {vector2[0]} y {vector2[-1]}")

                print(f"\n=={'POSICION CENTRAL':^30}==\n")
                if tam % 2 == 1:
                    medio = tam // 2
                    print(f"Vector 1: {vector1[medio]}\nVector 2: {vector2[medio]}")
                else:
                    med1 = tam // 2 - 1
                    med2 = tam // 2
                    print(f"Vector 1: {vector1[med1]} y {vector1[med2]}\nVector 2: {vector2[med1]} y {vector2[med2]}")

        case 5:
            print("\nSaliendo...")
            break

        case _:
            print("Caso no valido")
