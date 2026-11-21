import random as r

num = []
num2 = []
suma = []
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
            cant = int(input("\n\nCuantos numeros aleatorios se deberian generar? "))
            num.clear()
            suma.clear()
            for i in range(cant):
                num.append(r.randint(100, 1000))
            print(f"\nVector 1: {num}")
        case 2:
            if len(num) == 0:
                print("\n\nPrimero llene el vector 1 (opcion 1)")
            else:
                num2.clear()
                suma.clear()
                for i in range(len(num)):
                    num2.append(r.randint(100, 1000))
                print(f"\nVector 2: {num2}")
        case 3:
            if len(num) == 0 or len(num) != len(num2):
                print("\n\nLlene ambos vectores con la misma cantidad de numeros")
            else:
                suma.clear()
                for i in range(len(num)):
                    suma.append(num[i] + num2[i])
                print(f"\n\n=={'SUMA DE VECTORES':^30}==\n")
                print(f"Vector 1: {num}\nVector 2: {num2}\nSu suma: {suma}")
        case 4:
            if len(suma) == 0:
                print("\n\nPrimero llene ambos vectores y sumelos (opcion 3)")
            else:
                l = len(num)
                print(f"\n\n=={'REPETIDOS':^30}==\n")
                hay = False
                for i in range(l):
                    cont = 0
                    for j in range(l):
                        if num[i] == num[j]:
                            cont += 1
                            if j < i:
                                cont = 0
                                break
                    if cont > 1:
                        print(f"{num[i]} aparece {cont} veces en Vector 1")
                        hay = True
                if not hay:
                    print("Ningun numero se repite en Vector 1")

                hay = False
                for i in range(l):
                    cont = 0
                    for j in range(l):
                        if num2[i] == num2[j]:
                            cont += 1
                            if j < i:
                                cont = 0
                                break
                    if cont > 1:
                        print(f"{num2[i]} aparece {cont} veces en Vector 2")
                        hay = True
                if not hay:
                    print("Ningun numero se repite en Vector 2")

                mayor1 = num[0]
                mayor2 = num2[0]
                mayor3 = suma[0]
                menor1 = num[0]
                menor2 = num2[0]
                menor3 = suma[0]
                prom = 0
                for i in range(l):
                    if num[i] > mayor1:
                        mayor1 = num[i]
                    if num2[i] > mayor2:
                        mayor2 = num2[i]
                    if suma[i] > mayor3:
                        mayor3 = suma[i]
                    if num[i] < menor1:
                        menor1 = num[i]
                    if num2[i] < menor2:
                        menor2 = num2[i]
                    if suma[i] < menor3:
                        menor3 = suma[i]
                    prom += suma[i]

                print(f"\n=={'MAYORES Y MENORES':^30}==\n")
                print(f"Mayor -> Vector 1: {mayor1} | Vector 2: {mayor2} | Suma: {mayor3}")
                print(f"Menor -> Vector 1: {menor1} | Vector 2: {menor2} | Suma: {menor3}")
                print(f"\nPromedio de la suma: {prom / l:.2f}")

                print(f"\n=={'PRIMERO Y ULTIMO':^30}==\n")
                print(f"Vector 1: {num[0]} y {num[l - 1]}\nVector 2: {num2[0]} y {num2[l - 1]}")

                print(f"\n=={'POSICION CENTRAL':^30}==\n")
                if l % 2 == 1:
                    medio = l // 2
                    print(f"Vector 1: {num[medio]}\nVector 2: {num2[medio]}")
                else:
                    medio = l // 2 - 1
                    medio2 = l // 2
                    print(f"Vector 1: {num[medio]} y {num[medio2]}\nVector 2: {num2[medio]} y {num2[medio2]}")
            break
        case 5:
            break
        case _:
            print("Caso no valido")