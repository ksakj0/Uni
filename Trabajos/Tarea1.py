#Trabajos de practica
print(f"{'===':^23}MENU DE TAREAS{'===':^24}\n")
print(f"{'':^10}1. Preparación de una lámina decorativa ")
print(f"{'':^10}2. Dígito de control de una etiqueta ")
print(f"{'':^10}3. Selección de una batería para un dispositivo ")
print(f"{'':^10}4. Almacenamiento de una grabación de audio ")
print(f"{'':^10}5. Autorización para utilizar un laboratorio ")
print(f"{'':^10}6. Clasificación de una prueba de mecanografía  ")
print(f"{'':^10}7. Conversor de unidades de almacenamiento ")
print(f"{'':^10}8. Movimiento de una ficha en un tablero ")
print(f"{'':^10}9. Reducción sucesiva de una tira ")
print(f"{'':^9}10. Registro de duraciones con cancelación ")
print(f"{'':^9}11. Valor de un equipo a través de los años ")
print(f"{'':^9}12. Construcción de un texto con vocales ocultas ")

trabajos = int(input("Ingresa un numero del 1-12 para mostrar los trabajos: "))
match trabajos:
    case 1:
        ancho = float(input("\n\nIngresa el ancho de la lamina en centimetros: "))
        alto = float(input("Ingresa el largo de la lamina en centimetros: "))
        precio = float(input ("Ingresa el precio de impresion por centimetro cuadrado: "))
        desicion = input("Desea cubierta protectora? : [si/no]").lower()
            
        total = (ancho * alto) * precio
        cargo = 0
        if desicion == "si":
            cargo = total * 0.08
            total = total + cargo
        print(f"Area: {ancho*alto:.2f}fcm^2\nCosto de impresion: {total:.2f}\nCargo por cubierta: {cargo:.2f}\nTotal: {total:.2f}")
    case 2:
        while True:
            num = int(input("\n\nIngresa un numero entre 10-99: "))
            if num < 10 or num > 99:
                print("El numero tiene que ser mayor a 10 y menor a 99!!")
            else:
                break
        dec = num // 10
        un = num % 10
        sum = dec + un
        cont = sum
        if sum > 9:
            cont = sum - 9
        print(f"Digitos: {dec:.2f} y {un:.2f}\nSuma: {sum:.2f}\nProducto: {cont:.2f}")
    case 3:
        wh = float(input("\n\nIngrese el consumo en Wh por hora: "))
        h = float(input("Cuantas horas debe funcionar? "))
        bateria = float(input("Cuanta Wh disponibles hay en la bateria? "))
        
        necesario = wh * h
        posible = bateria / wh
        print(f"Energia requerida: {necesario:.2f}")
        print(f"Horas que permite la bateria: {posible:.2f}")
        if necesario<=bateria:
            total = bateria - necesario
            print(f"El consumo es de: {wh:.2f}\nDurante: {h:.2f}horas\nLa bateria tiene: {bateria:.2f}Wh\nSobran: {total:.2f}Wh en la bateria")
        else:
            total = necesario - bateria
            print(f"Energia insuficiente en la bateria, se necesitan {total:.2f}Wh para poder funcionar durante ese periodo")
    case 4:
        minutos = int(input("\n\nIngresa la duracion en minutos del archivo: "))
        calidad = input("Ingresa la calidad en el que lo quieres: [estandar/alta] ").lower()
        almacenamiento = 0.03
        
        if calidad == "alta":
            pesomb = 18
            otra = 7
        else:
            pesomb = 7
            otra = 18
            
        mb = minutos * pesomb
        gb = mb / 1000
        costo = mb * 0.03
        diferencia = abs(mb - minutos * otra)
        
        print(f"Espacio en MB: {mb:.2f}\nEn GB: {gb:.2f}\nCosto de almacenamiento: ${costo:.2f}\nDiferencia absoluta: ${diferencia:.2f}")
    case 5:
        capacitacion = input("\n\nConcluyo con la capacitacion? [si/no] ").lower()
        if capacitacion == "si":
            libre = float (input("Cuantas horas libres tienes? "))
            if libre>=2:
                print(f"\n\n=={'Acceso autorizado':^10}==\n\n")
                prep = float(input("Minutos de preparacion: "))
                fab = float(input("Minutos de fabricacion: "))
                restante = libre * 60 - prep - fab
                if restante<0:
                    print(f"Tiempo insuficiente")
                else:
                    print(f"Tiempo libre restante: {restante:.2f} minutos")
        else:
            print(f"=={'Debe completar la capacitacion':^10}==")
    case 6:
        escrito = int(input("\n\nIngresa las palabras escritas: "))
        errores = int(input("Ingresa la cantidad de errores que tuviste: "))
        minutos = float(input("Ingresa la duracion en minutos: "))
        
        correcto = escrito - errores
        porcentaje = errores / escrito * 100
        velocidad = correcto / minutos
        
        if velocidad >= 60:
            nivel = "avanzado"
        elif velocidad >=40:
            nivel = "intermedio"
        else:
            nivel = "inicial"
            
        print(f"\nLas palabras correctas son: {correcto}\nPorcentaje de errores: {porcentaje}\nVelocidad efectiva: {velocidad}\nNivel: {nivel}")
    case 7:
        print(f"{'':^23}============")
        print(f"{'':^23}{'MENU':^13}")
        print(f"{'':^23}============")
        print(f"1. KiB a bytes\n2. MiB a bytes\n3. GiB a bytes")
        while True:
            opcion = int(input("Elige 1 de las 3 opciones en nuestro menu\n"))
            if opcion>3:
                break
            cantidad = float(input("Que cantidad de desea convertir?\n"))
        
            match opcion:
                case 1:
                    bytes = cantidad * 1024
                    print(f"{cantidad} KiB = {bytes} bytes")
                    break
                case 2:
                    bytes = cantidad * 1024**2
                    print(f"{cantidad} MiB = {bytes} bytes")
                    break
                case 3:
                    bytes = cantidad * 1024**3
                    print(f"{cantidad} GiB = {bytes:.2f} bytes")
                    break
        print("Opcion invalida")
    case 8:
        x = int(input("Ingresa la posicion en la coordenada 'x'\n"))
        y = int(input("Ingresa la posicion en la coordenada 'y'\n"))
        direccion = input("A que direccion va? [N, S, E, O]\n").upper()
        cantidad = int(input("Cuantas casillas avanzara?\n"))
        
        match direccion:
            case "N":
                y += cantidad
            case "S":
                y -= cantidad
            case "E":
                x += cantidad
            case "O":
                x -= cantidad
            case _:
                print("Direccion invalida")
                
        print(f"Coordenadas finales: {x, y}")
    case 9:
        largo = float(input("Ingresa la longitud inicial en centimetros: "))
        lim = float(input("Ingresa un limite en la longitud: "))
        
        cortes = 0
        while largo > lim:
            largo/= 2
            cortes += 1
            print(f"Longitud: {largo}\nCortes: {cortes}\n")
        print(f"Longitud final: {largo}")
    case 10:
        obs = int(input("Cuantas observaciones se realizaran? "))
        
        registrado = 0
        total = 0
        while registrado < obs:
            duracion = float(input(f"Duracion de la observacion: {registrado + 1}. "))
            if duracion == -1:
                print(f"Registro cancelado, se registraron: {obs} observaciones")
                break
            total += duracion
            registrado += 1
        else:
            promedio = total / obs
            print(f"Registro completado\nTiempo total: {total:.2f}\nPromedio: {promedio:.2f}")
    case 11:
        inicial = float(input("Valor inicial del equipo: "))
        porcentaje = float(input("Porcentaje de perdida anual [0-100]\n"))
        y = int(input("Duracion en años: "))
        
        actual = inicial
        per = porcentaje / 100
        for y in range (1, y+1):
            inicio = actual
            perdida = inicio * per
            actual = inicio - perdida
            print(f"Año {y}: inicia con: ${inicio:.2f} | pierde: ${perdida:.2f} | termina con: ${actual:.2f}")
        acumulado = inicial - actual
        print(f"Valor final: {actual}\nPerdida acumulada: ${acumulado}")
    case 12:
        frase = input("Escribe una frase: ").lower()
        voc = "aeiouáéíóúü"
        contador = 0
        nuevo = ""
        for i in frase:
            if i in voc:
                nuevo += "*"
                contador += 1
            else:
                nuevo += i
        print(f"Original: {frase}\nTexto nuevo: {nuevo}\nVocales sustituidas: {contador}")