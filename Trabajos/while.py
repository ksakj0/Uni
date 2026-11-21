#Clase prueba while
"""
n_veces = int(input("Ingresa el numero de veces que quieres que se imprima el mensaje\n"))
contador = 1
while contador <= n_veces:
    print("Usando ciclos en python")
    contador += 1
print("Termina el ciclo")

numero = int(input("Dame la cantidad de numeros a sumar\n"))
suma = 0
while suma <= numero:
    suma = numero + numero
    numero += 1
    print (suma)
print(suma)

///

numero = int(input("Ingresa un numero inicial"))
contador = 1
suma = 0

while numero >= contador:
    suma = suma + contador
    contador += 1
    print(suma)
print("Fin")

///

num = int(input("Ingresa un numero que quieras voltear"))
result = 0
print(num)
while num > 0:
    result = result * 10
    result = result + num % 10
    num //= 10
    print(result, end = "") #El 'end = ""' funciona para anular ese salto de linea por defecto que trae python

///

intentos = 0
intentos_m = 3
NIP = 3563
while intentos < intentos_m:
   psw = int(input("Ingresa el NIP\n"))
   if psw == NIP:
       print("===Acceso concedido===")
       break
   print("===Acceso denegado===")
   intentos += 1
   quedan = intentos_m - intentos
   print(f"Quedan {quedan} intentos\n\n")
else:
    print("Se quedo sin intentos")

///

articulos = 0
total = 0
precio = int(input("Ingresa el precio del articulo: "))
while precio > 0:
    total += precio
    articulos += 1
    precio = int(input("Ingresa el precio del siguiente articulo: "))
if articulos == 0:
    print("No se registro ningun articulo")
else:
    print(f"El total antes de impuestos es de: {total}, y la catidad de articulos fue de: {articulos}")

///

nombre = input("Ingresa un nombre: ")
cont = 0
for cara in nombre:
    print(cara)
    cont += 1
print(f"Numero de caracteres: {cont}")

///
for i in range (1, 11):
    print(f"{i: < 10} {i**2:<10}")
///

while True:
    ahorro = float(input("especifica el monto que quieres ahorrar: "))
    if ahorro <= 0:
        break
    interes = float(input("Especifica la tasa de interes anual que tendra la cuenta de ahorros: "))
    if interes >= 1:
        interes/= 100
    tiempo = int(input("Ingresa el tiempo que pasara el ahorro en la cuenta: "))

    final = ahorro * (1 + interes)**tiempo
    print(f"{final:.2f}")

///

ahorro = float(input("especifica el monto que quieres ahorrar: "))
interes = float(input("Especifica la tasa de interes anual que tendra la cuenta de ahorros: "))
if interes >= 1:
    interes /= 100
tiempo = int(input("Ingresa el tiempo que pasara el ahorro en la cuenta: "))
cont = 1
for cont in range (1, tiempo + 1):
    ahorro = ahorro * (1 + interes)
    if cont == 1:
        print(f"Tiempo: {cont} año, Ahorro de: {ahorro:,.2f}")
    else:
        print(f"Tiempo: {cont} años, Ahorro de: {ahorro:,.2f}")
print(f"{cont} años y {ahorro:,.2f} de ahorro")

///

cadena = input("Ingresa un texto: ").lower()
cont_vocal = 0
vocal = "a, e, i, o, u"
for cara in cadena:
    if cara in vocal:
        cont_vocal += 1
print (f"La palabra: {cadena}\nTiene: {cont_vocal} vocales")

///
cadena = input("Ingresa un texto: ").lower()
caracter = input("Ingresa el caracter especifico que deseas contar en la palabra: ").lower()
cont_vocal = 0
for cara in cadena:
    if cara in caracter:
        cont_vocal += 1
print (f"La palabra: {cadena}\nTiene: {cont_vocal} '{caracter}'")

///
num = int(input("Ingresa un numero entero mayor a 1: "))
divisor = 0
ban = 0
for divisor in range (2, num):      
    if num % divisor == 0:
        print(f"{num} no es primo, es divisible entre {divisor}")
        ban = 1
        break
if ban == 0:
    print(f"{num} si es primo")
    
    #se solicita un numero, se inicializan variables como divisor y bandera en 0
    #divisor se pone en rango del 2, hasta el numero puesto en el input
    #se divide numero entre divisor y si es igual a 0 se determina que no es primo
    #bandera se suma en 1 para determinar que es primo y se rompe el ciclo
    #si bandera continua con el valor inicial de 0 se determina que la parte anterior del ciclo fue falsa
    #por lo tanto el numero es primo
    
///

texto = input("Ingresa una palabra: ")

print(f"{'indice': ^10} : {'caracter': ^10}")
for indice, caracter in enumerate(texto):
    print(f"{indice: ^10} : {caracter: ^10}")
"""

# Prueba de listas

###
edades = [0]*5
print(edades)
calif = [None]*5
for i in range (5):
    calif[i] = input(f"Ingrese la calificacion {i + 1}: ")
    

print (calif)
###
despensa = ["leche", "limones", "pasta", "huevos", "pan"]

while True:
    nuevo = input("Ingresa los elementos que deseas agregar: ")
    if nuevo in despensa or nuevo == "salir":
        break
    despensa.append(nuevo)
print(despensa)