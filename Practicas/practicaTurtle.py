import turtle
import math
import random

def HelloWorld(texto):
    print(texto)
HelloWorld("print")
HelloWorld("\n")
"""
Ingresa los kilometros recorridos
kilometros = kilometros recorridos
Ingresa los litros consumidos
litros = litros consumidos

rendimiento = kilometros / litros

el rendimiento promedio es: 
"""
###
kilometros = float(input("Ingresa los kilometros recorridos: \n"))
litros = float(input("Ingresa los litros consumidos: \n"))
rendimiento = kilometros / litros
print("El rendimiento promedio es: ",rendimiento)
###
"""
###
print("\n\n")
cons = int(input("Ingresa un valor\n"))
if cons >= 10:
     print("hola")
else:
    print("adios")
###
a diferencia de otros lenguajes solo basta con poner ":" despues de if o else
para indicar a python que estas haciendo una desicion
en cs se necesita de las"{}" para abrir o cerrar estas desiciones
  
###


#Turtle tutorial

nombre = turtle.Turtle()

Al inicio se le asigna un nombre x a la flecha para posteriormente asignarle el valor de 'turtle.Turtle()'
esto lo que hace es darle nombre a la variable para despues poder darle ordenes especificas
sin esto la flecha que genera el programa no sera capaz de generarse y mucho menos seguir las instrucciones que se le dieron
"""
##
"""
#Un cuadrado con salto para hacer otro cuadrado
nombre.speed(2) #Esto dicta la velocidad a la que 'nombre' dibuja las instrucciones que se le dan
nombre.forward(100) #Se mueve 100 pixeles hacia adelante
nombre.left(45) #Gira 'n' cantidad de grados hacia 'x' direccion, puede abreviarse 'left' utilizando 'lt', y 'right' con 'rt'
nombre.forward(100)
nombre.rt(90)
nombre.forward(100)

nombre.color("#30D6FF", "orange") #Esto le da color a la flecha, viene con colores pre cargados pero tambien soporta hexa y RGB, siempre tiene que ir entre comillas
#Si se le quieren dar colores distintos al outline y al relleno de la figura, se tienen que poner ambos dentro de color
nombre.begin_fill() #Le da a entender al programa que lo que esta dentro de esto va a ser relleno con color
nombre.forward(100)
nombre.lt(90)
nombre.forward(100)
nombre.lt(90)
nombre.forward(100)
nombre.lt(90)
nombre.forward(100)
nombre.end_fill() #Da la orden para rellenar de color lo que sea que se haya formado con las instrucciones de en medio

nombre.penup() #Da la instruccion de 'levantar el lapiz'
nombre.forward(70) #Se levanta durante 'n' pixeles hacia 'x' posicion
nombre.pendown() #Da la instruccion de 'bajar el lapiz'

nombre.forward(100)
nombre.lt(90)
nombre.forward(100)
nombre.lt(90)
nombre.forward(100)
nombre.lt(90)
nombre.forward(100)
nombre.home()

#Una estrella con size incremental
nombre.color("orange")
nombre.speed(30)
for i in range(800): # 'i' se repite 'n' veces, siendo 'i' las instrucciones dentro del for y 'n' la cantidad asignada en el rango
    nombre.forward(math.sqrt(i)*30) #Aqui la raiz cuadrada (sqrt) de 'i' se va multiplicando por 'n' cantidad con cada trazo
    #nombre.left(i%60) #No entendi muy bien esta ecuacion, solo supe que al llegar a 'n' cantidad de grados esta vuelve a 1
    nombre.left(165)
nombre.home()

#Una Estrella con picos de estrella
nombre.speed(100)
nombre.color("green")
nombre.getscreen().bgcolor("cyan")
nombre.penup()
nombre.goto(-200, 100) #Va hacia las coordenadas que se le asignan sin necesidad de estar poniendo forward, left o right
nombre.pendown()

def star(name, size):
    if size <= 5: #Esto define que tan chica sera la estrella dibujada
        return
    else:
        for i in range(5): #Como una estrella tiene 5 picos no hay necesidad de repetir mas veces la secuencia, a menos que se modifique la cantidad de grados para agregar mas picos
            name.forward(size)
            star(name, size/2.70) #Esto define la cantidad de estrellas que se dibujaran por cada pico, mientras mas chico el numero mayor cantidad de estrellas se dibujan por cada pico
            name.left(216)
            
star(nombre, 300)
nombre.home()

#Un corazon
name = turtle.Turtle()
name.color("red", "red")
nombre.color("red", "red")
with nombre.fill():
    with name.fill():
        #nombre.begin_fill()
        #name.begin_fill()
        nombre.left(40)
        nombre.forward(140)
        nombre.left(45)
        nombre.forward(70)
        nombre.left(65)
        nombre.forward(70)
        nombre.left(65)
        nombre.forward(75)

        name.right(40)
        name.backward(140)
        name.right(45)
        name.bk(70)
        name.rt(65)
        name.bk(70)
        name.rt(65)
        name.bk(75)
        #nombre.end_fill()
        #name.end_fill()
nombre.home()
name.home()

#Otra estrella
nombre.speed(10)
nombre.color("red", "orange")
nombre.getscreen().bgcolor("cyan")
nombre.penup()
nombre.goto(-200, 100) #Va hacia las coordenadas que se le asignan sin necesidad de estar poniendo forward, left o right
nombre.pendown()

start = nombre.pos()
with nombre.fill():
    def star(name, size):
        if size <= 5: #Esto define que tan chica sera la estrella dibujada
            return
        else:
            #for i in range(5):
            while True: 
                name.forward(size)
                #star(name, size/2.7999) 
                name.left(190) 
                if nombre.distance(start) < 1:
                    break
                
    star(nombre, 300)
nombre.penup()
nombre.home()
nombre.pendown()

turtle.done()
"""
