filas = 2
columnas = 4

ancho_f = 12
ancho_c = 6
#Crear la matriz tienda 2x4
tienda = [[20, 10, 15, 60],
          [30, 15, 25, 40]]

#Imprimir los titulos de las columnas
#Espacio de la esquina superior izquierda
print(f"{' ':<{ancho_f}}", end="")

#Ciclo para imprimir cada titulo de la columna
for c in range(columnas):
    print(f"{'Pza '+str(c+1):>{ancho_c}}", end="")
print()
print("-"*40)

#Imprimir matriz
for f in range(filas):
    #Imprime el titulo de la fila
    print(f"{'Almacen '+str(f+1):<{ancho_f}}", end="")
    for c in range(columnas):
        print(f"{tienda[f][c]:>{ancho_c}}", end="")
    print()
print("-"*40)