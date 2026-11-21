#Trabajo en clase
"""
nombre = input("Ingresa tu nombre: ")
correo = input("Ingresa tu correo electronico: ")
telefono = input("Ingresa tu numero telefonico: ")
valido = True

if not nombre:
    print("Falta el nombre")
elif not correo:
    print("Falta el correo")
elif not telefono:
    print("Falta el telefono")
else:
    print("todos los datos se calcularon")
###

if not nombre:
    print("Tienes que ingresar tu nombre!")
    valido = False
if not correo:
    print("Tienes que ingresar tu correo electronico!")
    valido = False
if not telefono:
    print("Tienes que ingresar tu numero telefonico!")
    valido = False
if valido:
    print("Los datos fueron capturados")

###
while not nombre:
    print("Tienes que ingresar tu nombre!")
    nombre = input("Ingresa tu nombre: ")
while not correo:
    print("Tienes que ingresar tu correo electronico!")
    correo = input("Ingresa tu correo electronico: ")
while not telefono:
    print("Tienes que ingresar tu numero telefonico!")
    telefono = input("Ingresa tu numero telefonico: ")

###
hora = int(input("Ingrese una hora\n"))

if hora >= 17 and hora < 20:
    print("Hora feliz 2x1")
"""

while True: #Inicia un bucle para el programa
    dia = int(input("Ingresa un numero del 1-7\n"))
    match dia: #Hace una comparacion entre las respuestas
        case 1: #Cada case cae en la comparacion del match, en el momento en que una concida no se siguen comparando los demas
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
        case _: # '_:' funciona como un "En cualquier otro caso", siempre tiene que ir al final
            print(f"El dia {dia} no coincide con ninguno de la semana\n\n")
            continue #En caso de que el numero ingresado no concida con los anteriores vuelve a repetir el bucle
    break #En caso de que el numero coincida con alguno de los casos el bucle termina y termina el proceso
