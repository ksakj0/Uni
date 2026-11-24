#Consumo de agua en un conjunto de viviendas
import random as r
matriz = []
vivienda = int(input("Ingresa la cantidad de viviendas: "))
mes = int(input("Ingresa la cantidad de meses: "))

for filas in range(vivienda):
    fila = []
    for columnas in range(mes):
        fila.append(r.randint(1, 20))
    matriz.append(fila)
    
print(f"{"":^13}", end="")
for i in range(vivienda+1):
    print(f"Mes{i+1}{"":^3}", end=" ")
print()
for r, fila in enumerate(matriz):
    print(f"Vivienda{r + 1:>2} ", end="")
    for i2 in fila:
        print(f"{"":^3}{i2}{"":^3}", end=" ")
    print()
    
pago = []
for i in range(vivienda):
    suma = 0
    for i2 in range(mes):
        if i2>i-1:
            suma += matriz[i][i2]
    pago.append(suma)
    print(f"suma{i+1} {suma}\n")
print(f"pago {pago}\n")


indice = 0
for i in range(len(pago)):
    if pago[i] > pago[indice]:
        indice = i

print(pago[indice])