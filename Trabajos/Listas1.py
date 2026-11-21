numeros = [10, 20, 30, 40, 50]
print(f"{'Indice':^10} {'valor':^10}")
#for i, numero in enumerate(numeros):
#    print(f"{i:^10}{numero:^10}")
for indice in range (5):
    print(f"{indice:^10}{numeros[indice]:^10}")
    
while True:    
    transporte = [0]*8
    asiento = int(input("Que asiento quiere? "))
    #0 = libre || 1 = ocupado
    if transporte[asiento] == 0:
        transporte[asiento] = 1
        print(f"Has comprado el asiento: {asiento}")
    else:
        print("Asiento ocupado")
        break
