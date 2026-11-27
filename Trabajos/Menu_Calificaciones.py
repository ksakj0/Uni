#Programa que presenta un menú modo texto
#Solicitar el tamaño de la lista (el número de elementos)
tamaño = int(input("Ingresa el tamaño para la lista de Calificaciones:"))

#Crear la lista con elemtos fijos inicializado con 0
calificaciones = [0]*tamaño

#Variable para controlar el menú op -> opción del menú
op =0
#Ciclo while (mientras no pulse 0)
def pausa():
    input("Puse enter para continuar...")
    
while op!=4:
    print("Menú Calificaciones")
    print("1. Capturar")
    print("2. Imprimir")
    print("3. Promediar")
    print("4. Salir")
    #Solicitar al usuario la opción
    op = int(input("Ingrese la opción:"))
    match op:
        case 1:
            print("Capturar")
            #Usar un ciclo for con range()
            for indice in range(tamaño):
                calificaciones[indice] = int(input(f"Ingrese la calificación {indice+1}:" ))
            #Pausa
            pausa()
        case 2:
            #Imprime la lista con f-string (modo tabla)
            print("imprimir")
            print(calificaciones)#Solo para probar...
            print("-"*18)
            print(f"{'No.':<5} {'Calificación':<12}")
            print("-"*18)
            for indice in range(tamaño):
                print(f"{indice+1:^5} {calificaciones[indice]:^12}")
            print("-"*18)
            #Pausa
            pausa()
           
        case 3:
            #Calcula la calificación promedio 
            suma=0
            print("promediar")
            for indice in range(tamaño):
                suma+=calificaciones[indice]
            prom=suma/tamaño
            print(f"Promedio:{prom:.1f}")
            #Pausa
            pausa()
        case 4:
            print("salir")
        case _:
            print("Opción no válida")
            #Pausa
            pausa()