calif = [0]
name = [0]
while True:
    print("1. Ingresar nombres")
    print("2. Ingresar calificaciones")
    print("3. Promediar")
    print("4. Salir")
    
    op = int(input("Ingrese una de las siguientes opciones: "))
    
    match op:
        case 1:
            size = int(input("Cuantos elementos tendra la lista? "))   
         
            name = [None] * size
            print(f"{calif}")
            l = len(name)
            for i in range(l):
                name[i] = input("Ingresa los nombres de los estudiantes")
            print(f"Nombres de los estudiantes:\n{name}")
         
        case 2:
            calif = [0] * l
            for i2 in range(l):
                calif[i2] = int(input(f"Ingresa la calificacion de {name[i2]}:"))
            print("Ingresa las calificaciones de los estudiantes en un rango de 0-100")
            print(f"{'=' * 8} {'Calificaciones':^5} {'=' * 8}")
            print(f"{'':^5}{'No.':<7} {'Nom':<7} {'Calif':<12}")
            print(f"{'':^5}{'-' * 22}")
            for i3 in range(l):
                print(f"{'':^5} {i3 + 1:^5} -- {name[i3]:^5} -- {calif[i3]:^5}")
            print(f"{'':^5}{'-' * 22}")
            
            #Crear una pausa
            print(f"{'Pulse "Enter" para continuar...':^8}")
            input("")