#Programa que determina s una persona es mayor de edad
"""
nombre = input("Ingresa tu nombre:\n")
edad = int(input("Ingresa tu edad:\n"))
#Proceso -> determinar si la persona es mayor de edad
if edad >= 18:
    print(f"{nombre} eres mayor de edad.")
    print("Tienes que solicitar o renovar tu credencial de elector")
else:
    print(f"{nombre} eres menor de edad.")
    print("Pide autorizacion a tus padres o tutor")

print("=====Termina proceso...=====")
"""

nombre = input("Ingresa tu nombre: ")
correo = input("Ingresa tu correo electronico: ")
telefono = input("Ingresa tu numero de telefono: ")

if not nombre:
    print(f"Dato vacio")
else:
    print("Su nombre es: {nombre}")
print(f"Su correo es: {correo}")
print(f"Su telefono es: {telefono}")