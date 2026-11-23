#Clase matrices2
import random as r
filas = 3
columnas = 3
matriz = [0] * filas
print(matriz)
 
for f in range(filas):
    matriz[f] = [0] * columnas
    
print(matriz)

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = r.randint(1, 10)
        print(matriz[f][c], "\t", end="")
    print()
    
for f in range(filas):
    if matriz[f][f] is not None:
        print(f"\n{matriz[f][f]}")