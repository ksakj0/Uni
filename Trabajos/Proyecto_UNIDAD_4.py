#
catalogo=[
    ["AROMA:","LAVANDA","ROSA","EUCALIPTO"],
    ["PAIS:","EUROPA","PARIS","ESPAÑA"],
    ["MEDIDA:","500ML","800ML","1200ML"],
    ["PRECIO:","$250","$620","$850"],
    ]
orden=[]
while True:
    print("\n ~~~~~~ MENÚ ~~~~~~")
    print("1. Mostrar catálogo")
    print("2. Marcar orden")
    print("3. Mostrar orden")
    print("4. Deseas corregir?")
    print("5. Mostrar ticket de compra")
    print("6. SALIR")
    op=int(input("Selecciona una opcion: "))
    match op:
        case 1:
            for f in range(0,4):
                fila=[]
                print()
                for c in range(0,4):
                    print(catalogo[f][c])
        case 2:
            print("\n ~~ Elige el producto que deseas de cada categoria  ~~")
            fila=[]
            for f in range(0,3):
                print("\n ", catalogo[f][0])
                for c in range(1,4):
                    print(c, catalogo[f][c])
                seleccion=int(input("Selecciona una opcion (1-3): "))
                fila.append(catalogo[f][seleccion])
                if f==2:
                    fila.append(catalogo[3][seleccion])
            orden.append(fila)
        case 3:
            print("\n ~~~ MOSTRANDO ORDEN ~~")
            for f in range(0,len(orden)):
                print("\n Producto: ", f+1)
                for c in range(0,4):
                    print(orden[f][c], end=" ")
                    print()
        case 4:
            print("\n ~~ CORREGIR ~~")
            respuesta=input("\n ¿Deseas agregar algo más? SI/NO: ").lower()
            if respuesta=="si":
                print("Agrega el siguiente producto")
                print("Selecciona la opcion 2 del menú principal")
            else:
                print("Pedido finalizado")
                print("Selecciona la opcion 5 del menú principal")
        case 5:
            print("\n ~~~ MOSTRANDO ORDEN ~~")
            suma=0
            for f in range(0,len(orden)):
                print("~~~~~~~~~~~~~~~~~~~~~~")
                for c in range(0,4):
                    print(orden[f][c], end=" ")
                    print()
                precio=int(orden[f][3][1:])
                suma=suma+precio
            print("~~~~~~~~~~~~~~~~~~~~~~")
            print("El total de la orden es de: $", suma)
        case 6:
            print("\n Terminando ejecución")
            print("Cerrando programa ...")
            break
        case _:
            print("\n ~ OPCION INVÁLIDA! ~")