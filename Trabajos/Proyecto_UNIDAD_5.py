# U ~ N ~ I ~ D ~ A ~ D ~ [ 4 ]
perfumes=[]
while True:
    print("\n ~~~~~~ MENÚ ~~~~~~")
    print("1. AROMA")
    print("2. PAÍS")
    print("3. MEDIDA Y PRECIO")
    print("4. ELIMINAR")
    print("5. MOSTRAR TICKET")
    print("6. SALIR")
    op=int(input("Selecciona una opcion: "))
    match op:
        case 1:
            print("\n ~ Selecciona el aroma ~")
            aroma=input("Aroma: ").upper()
        case 2:
            print("\n ~ Selecciona el pais ~")
            pais=input("Pais: ").upper()
        case 3:
            print("\n ~ Selecciona la cantidad que deseas ~")
            medida=input("Medida (ml): ").upper()
            precio=input("Precio: $")
            perfumes.append(
                {
                "aroma":aroma,
                "pais":pais,
                "medida":medida,
                "precio":precio
                 }
            )
            print("Pedido guardado! ")
        case 4:
            if not perfumes:
                print("Lista vacía !!")
            else:
                print("\n ~ Selecciona el pedido a eliminar ~")
                for f in range(0,len(perfumes)):
                    print(f+1,perfumes[f]["aroma"], perfumes[f]["pais"],perfumes[f]["medida"])
                buscar=int(input("Número de pedido a eliminar: "))
                if buscar>=1 and buscar<=len(perfumes):
                    perfumes.remove(perfumes[buscar-1])
                    print("Pedido eliminado!")
                else:
                    print("Pedido no encontrado :(")
        case 5:
            suma=0
            print("\n ~~~~~ TICKET DE COMPRA ~~~~~")
            for pedido in perfumes:
                print("\n AROMA:",pedido["aroma"])
                print("PAÍS:",pedido["pais"])
                print("MEDIDA:",pedido["medida"], "ml")
                print("PRECIO: $",pedido["precio"])
                suma=suma+float(pedido["precio"])
            print("\n TOTAL DE LA COMPRA: $",suma)
        case 6:
            print("\n Terminando ejecución")
            print("Cerrando programa ...")
            break
        case _:
            print("\n ~ OPCION INVÁLIDA! ~")
            print("Elige una opcion 1-5")