import math as m
import random as r

num = []
num2 = []
suma =[]
while True:
    print("1. Llenar el primer vector con numeros aleatorios:")
    print("2. Llenar el segundo vector con numeros aleatorios:")
    print("3. Sumar ambos: ")
    print("4. Resultados: ")
    print("5. Salir ")
    op = int(input("\nIngresa una de las 5 opciones\n"))
    
    match op:
        case 1:
            cant = int(input("Cuantos numeros aleatorios se deberian generar?\n"))
            for i in range(cant):
                num.append(r.randint(1, 5))
        case 2:
            for i in range(cant):
                num2.append(r.randint(1, 5))
        case 3:
            l = len(num)
            for i in range(l):
                casilla = num[i] + num2[i]
                suma.append(casilla)
            print(f"Vector 1: {num}\nVector 2: {num2}\nSu suma: {suma}")
        case 4:
            l = len(num)
            si = False
            si2 = False
            pos = 0
            posb = 0
            posc = 0
            prom = 0
            ####
            for i in range(l):
                cont = 0
                primera = True
                for j in range(l):
                    if num[i] == num[j]:
                        cont += 1
                        if j < i:
                            primera = False
                if cont > 1 and primera:
                    print(f"{num[i]} aparece {cont} veces en Vector 1")
                    si = True
            if not si:
                print("Ningun numero se repite Vector 1")
            ####
            for i in range(l):
                cont2 = 0
                primera = True
                for j in range(l):
                    if num2[i] == num2[j]:
                        cont2 += 1
                        if j < i:
                            primera = False
                if cont2 > 1 and primera:
                    print(f"{num2[i]} aparece {cont2} veces en Vector 2")
                    si2 = True
            if not si2:
                print("Ningun numero se repite en Vector 2")
            ####
            for i in range(l):
                if num[i] > num[pos]:
                    pos = i
            for j in range(l):
                if num2[j] > num2[posb]:
                    posb = j
            for h in range(l):
                if suma[h] > suma[posc]:
                    posc = h
            print(num[pos], num2[posb], suma[posc])
            ####
            for i in range(l):
                if num[i] < num[pos]:
                    pos = i
            for j in range(l):
                if num2[j] < num2[posb]:
                    posb = j
            for h in range(l):
                if suma[h] < suma[posc]:
                    posc = h
            print(num[pos], num2[posb], suma[posc])
            ####
            for i in range(l):
                prom += num[i] + num2[i]
            print(f"{prom/l}")
            ####
            for i in range(l):
                a = i
            print(num[0], num[a])
            
            for i in range(l):
                b = i
            print(num2[0], num2[b])
            ###
            if l % 2 == 1:
                medio = l//2
                print(num[medio])
                print(num2[medio])
            else:
                medio = l // 2 - 1
                medio2 = l // 2
                print(num[medio], num[medio2])
                print(num2[medio], num2[medio2])
        case 5:
            break
        case _:
            print("Caso no valido")