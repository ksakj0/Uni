aroma =["Lavanda", "Lirio", "Rosa"]
precio =[10, 20, 30]
pais = ["Mx", "USA", "ALM"]
while True:
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")
    print("8")
    op = int(input("Seleccione una opcion: "))
    
    match op:
        case 1:
            nombre = input("Ingresa tu nombre: ")
            
        case 2:
            print("CATALOGO\n")
            
            for i in range(len(precio)):
                print(aroma[i], precio[i])
        case 3:
            print("PAIS\n")
            
            for i1 in range(len(precio)):
                print(pais[i1], aroma [i1])