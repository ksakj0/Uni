import math
"""
nombre = input("Ingrese su nombre completo\n")
prestamo = float(input("Ingrese la cantidad que desea recibir como prestamo\n"))
interes = float(input("Ingrese la cantidad de interes que se le aplicara al prestamo\n"))

if interes >= 1:
    interes = interes / 100
final = prestamo * interes
prestamo_final = prestamo + final

print("Su nombre es:", nombre,"\nSolicito un prestamo de:",prestamo,"\nCon un interes de:",interes,"\nEl Monto de interes que debera pagar es de:", final)
print("El monto final que debera pagar es de:", prestamo_final)

###
nombre = input("Ingresa tu nombre\n")
name = len(input("Ingresa el nombre de nuevo\n"))

print("Tipo de dato de nombre", type(nombre))
print("Tipo de daro de name", type(name))

#Entrada y salida de variable precio
producto = "Cuaderno"
precio = 27.50
    #precio = float(input("Ingresa el precio\n"))
mensaje = f"El {producto} cuesta ${precio:.2f}" # ':' indica que se abrira una condicion especial para 'precio' | '.2f' indica que se tomaran 2 decimales despues del . decimal
    #tambien valido --> print(f"El{producto} cuesta ${precio:.2f}") 
print(mensaje)

###
nombre = input("Nombre: ")
edad = int(input("Edad: "))

print(f"Hola, {nombre}")
print(f"El proximo año tendras {edad + 1}, años")
"""

radio = float(input("Ingresa el radio del circulo\n"))
area_circulo = math.pi * radio**2
print(f"El area es: {area_circulo:.2f}")