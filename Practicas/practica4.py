fila = 3
column = fila
est = [None] * fila

while True:
    op = input("Desea registrar estaturas? [s/n] ").lower()
    
    match op:
        case "s":
            for f in range(fila):
                est[f] = [None] * column
        
            for f in range(fila):
                for c in range(column):
                    est[f][c] = float(input("Ingrese una estatura: ")) 
            def matriz():
                for f in range(fila):
                    for c in range(column):
                        if est[f][c] is None:
                            print(f"- \t", end="")
                        else:
                            print(f"{est[f][c]:.2f} \t", end="")
                    print("")
            
            matriz()
                
            print("Eliminemos una estatura")
            a = int(input("A que fila pertenece el dato a eliminar? "))
            a -= 1 
            b = int(input("A que columna pertenece el dato a eliminar? "))
            b -= 1
            
            print(est[a][b])
            est[a][b] = None
            matriz()
            
            print("Ahora modifiquemos alguno de esos datos ")
            a = int(input("A que fila pertenece el dato a modificar? "))
            a -= 1
            b = int(input("A que columna pertenece el dato a modificarr? "))
            b -= 1
            c = float(input("Cual sera la nueva estatura? "))
            
            print(est[a][b])
            est[a][b] = c
            matriz()
            
            print("Sumemos")
            suma = 0
            for f in range(fila):
                suma += est[f][f]
            print(f"Suma de la diagonal principal: {suma}")
            
            l = len(est)
            print(est[0][0])
            
            if l % 2 == 1:
                medio = l//2
                print(f"Posicion central: fila {medio + 1}, columna {medio + 1}")
                print(f"Estatura central: {est[medio][medio]}")
            
            for f in range(fila):
                for c in range(column):
                    f=f
                    c=c
            print(est[f][c])
            
            vector = []
            for f in range(fila):
                for c in range(column):
                    vector.append(est[f][c])
            print(vector)
            
            alto = vector[0]
            bajo = vector[0]
            for i in range (l):
                if vector[i] > alto:
                    alto = vector[i]
                    pos = i
                if vector[i] < bajo:
                    bajo = vector[i]
                    posb = i
            print(f"Mayor: {alto}\nBajo: {bajo}")
        case "n":
            break
        case _:
            print("Caso no valido, presiona ENTER para continuar")
            input("")