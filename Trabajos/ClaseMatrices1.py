import random as r
"""
filas = 2
columnas = 3

matriz = [0] * filas
    print(matriz)

for f in range(filas):
    matriz[f] = [0] * columnas
print(matriz)

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], end="")
    print("")
"""

filas = int(input("Ingresa el numero de filas de la matriz cuadrada: "))
columnas = int(input("Ingresa el numero de columnas de la matriz cuadrada: "))

matriz_num = [0] * filas

for f in range(filas):
    matriz_num[f] = [0] * columnas

for f in range(filas):
    for c in range(columnas):
        matriz_num[f][c] = (r.randint(1,20)) 
    
for f in range(filas):
    for c in range(columnas):
        print(matriz_num[f][c], "\t", end="")
    print("")

search = int(input("Que valor desea buscar? "))
flag = False
for f in range(filas):
    for c in range(columnas):
        if search == matriz_num[f][c]:
            print(f, c)
            flag = True
if not flag:
    print("Dato no encontrado")
    
f = int(input(f"Ingresa la fila [0-{filas-1}]: "))
c = int(input(f"Ingresa la columna [0-{columnas-1}]: "))

if (f >= 0 and f < filas) and (c >= 0 and c < columnas):
    print(matriz_num[f][c])
else:
    print(f"El valor de la fila o columna estan fuera de rango")