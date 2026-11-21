pc = int(input("Ingrese la cantidad de computadoras disponibles: "))
pcv = [0] * pc

for r, fila in enumerate(pcv):
    if r+1<10:
        print(f"{r+1}  {fila}")
    else:
        print(f"{r+1} {fila}")

for f in range(pc):
    pcv[f] = int(input(f"Ingrese el tiempo de uso en minutos [{f+1}]: "))
suma = 0
for i in range(pc):
    suma += pcv[i]
print(f"{suma/60:.2f}")
promedio = suma / len(pcv)
print(promedio)