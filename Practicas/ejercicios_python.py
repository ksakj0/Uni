# -*- coding: utf-8 -*-
"""
EJERCICIOS SIMPLES DE PYTHON
============================
Temas: print, match/case, while y el uso correcto de for.

Nota: en Python NO existe `printf` (eso es de C). La funcion equivalente es
`print`. Aqui se explica y se practica.

Para ejecutar:  python ejercicios_python.py
"""


# =====================================================================
# PARTE 1: print (el "printf" de Python)
# =====================================================================
# print puede recibir varios argumentos y los separa con un espacio.
# `sep` cambia el separador y `end` cambia lo que se imprime al final.

def parte_1_print():
    print("=== PARTE 1: print ===")

    # 1.1 Varios argumentos y separador personalizado
    print("Nombre:", "Ana", "Edad:", 25)                 # separador por defecto: espacio
    print("2024", "01", "31", sep="-")                   # -> 2024-01-31

    # 1.2 `end` evita el salto de linea
    print("Cargando", end="")
    print("...", end="")
    print(" listo!")                                     # toda la linea sale junta

    # 1.3 f-strings: la forma moderna de formatear (equivale al %d / %s de C)
    nombre = "Luis"
    edad = 30
    print(f"Hola {nombre}, tienes {edad} anios.")         # -> Hola Luis, tienes 30 anios.

    # 1.4 Formato numerico con f-strings
    precio = 19.5
    print(f"Precio: {precio:.2f} euros")                  # 2 decimales -> 19.50
    print(f"Binario de 10: {10:b} | Hexadecimal: {255:x}")  # -> 1010 | ff

    # 1.5 EJERCICIO: completa tu mismo
    #   Imprime una tabla de multiplicar del 7 con 3 columnas separadas por " | "
    #   y el resultado de 7*3 con 2 decimales.
    print()


# =====================================================================
# PARTE 2: match / case (Python 3.10+)
# =====================================================================
# Es el "switch" de otros lenguajes, pero mucho mas potente.
# Puntos clave:
#   - Solo entra en UN case y sale (no hay fall-through como en C).
#   - `case _:` es el "default" (comodin).
#   - Se pueden usar guardas: `case x if condicion:`
#   - Los patrones pueden ser literales, tuplas, listas, diccionarios o clases.

def parte_2_match_case():
    print("=== PARTE 2: match / case ===")

    # 2.1 Caso basico con un menu
    def menu(opcion):
        match opcion:
            case 1:
                return "Elegiste: sumar"
            case 2:
                return "Elegiste: restar"
            case 3:
                return "Elegiste: salir"
            case _:
                return "Opcion no valida"

    for op in (1, 3, 9):
        print(f"menu({op}) -> {menu(op)}")

    # 2.2 Patrones de tipo y guardas (if dentro del case)
    def clasificar(valor):
        match valor:
            case 0:
                return "cero"
            case int() as n if n < 0:
                return f"entero negativo ({n})"
            case int() as n:
                return f"entero positivo ({n})"
            case str() as s if len(s) > 5:
                return f"texto largo ({s!r})"
            case _:
                return "otro tipo"

    for v in (0, -4, 12, "hola mundo", 3.14):
        print(f"clasificar({v!r}) -> {clasificar(v)}")

    # 2.3 Patrones de secuencia y de diccionario
    def comando(cmd):
        match cmd.split():
            case ["salir"]:
                return "Saliendo del programa..."
            case ["sumar", a, b]:
                return f"Suma = {int(a) + int(b)}"
            case ["saludar", *resto]:
                return f"Hola {' '.join(resto)}!"
            case _:
                return "Comando desconocido"

    for c in ("salir", "sumar 4 8", "saludar Ana Maria", "borrar todo"):
        print(f"comando({c!r}) -> {comando(c)}")

    # 2.4 EJERCICIO: escribe un `match` que reciba una letra de nota
    #   ("A", "B", "C", "D", "F") y devuelva su descripcion. Usa `case _`
    #   para las notas desconocidas.
    print()


# =====================================================================
# PARTE 3: while
# =====================================================================
# `while` repite MIENTRAS la condicion sea verdadera. Se usa cuando NO
# sabemos cuantas vueltas hay que dar (depende de una condicion).
# Reglas de oro:
#   1. Algo dentro del bucle debe cambiar, o se vuelve infinito.
#   2. Cuidado con el patron "pedir hasta que sea valido".
#   3. `break` sale del bucle, `continue` salta a la siguiente vuelta.

def parte_3_while():
    print("=== PARTE 3: while ===")

    # 3.1 Contador simple
    i = 1
    while i <= 5:
        print(f"contador: {i}")
        i += 1                       # <-- imprescindible

    # 3.2 Sumar numeros hasta superar un limite
    suma, n = 0, 1
    while suma < 20:
        suma += n
        n += 1
    print(f"Se necesitaron {n - 1} numeros para superar 20 (suma = {suma})")

    # 3.3 while True + break: el patron tipico de los menus
    #    (aqui simulamos las respuestas del usuario para que se pueda ejecutar)
    respuestas = iter([2, 5, 0])
    while True:
        opcion = next(respuestas, 0)          # en la vida real: int(input("Opcion: "))
        if opcion == 0:
            print("Saliendo del menu...")
            break
        print(f"Procesando opcion {opcion}")

    # 3.4 continue: saltar los multiplos de 3
    vistos = []
    x = 0
    while x < 10:
        x += 1
        if x % 3 == 0:
            continue
        vistos.append(x)
    print(f"Sin multiplos de 3: {vistos}")

    # 3.5 while ... else: el `else` se ejecuta si el bucle termino SIN break
    intentos = 0
    while intentos < 3:
        intentos += 1
    else:
        print("El bucle termino normalmente (sin break)")

    # 3.6 EJERCICIO: con while, invierte los digitos de 1234 (resultado 4321)
    #   sin convertir el numero a string (usa % 10 y // 10).
    print()


# =====================================================================
# PARTE 4: LA FORMA CORRECTA DE USAR `for`
# =====================================================================
# IDEA CENTRAL: en Python `for` NO es un contador con indice como en C/Java.
# Es un ITERADOR: recorre los elementos de algo (una lista, un string, un
# rango, un diccionario...). Se lee "para cada elemento EN la secuencia".
#
#   MAL (estilo C)                    BIEN (estilo Python)
#   for i in range(len(lista)):       for elemento in lista:
#       print(lista[i])                   print(elemento)
#
# `range()` solo se usa cuando REALMENTE necesitas el numero.
# Si necesitas indice Y valor a la vez, usa `enumerate()`.
# Si necesitas recorrer dos listas en paralelo, usa `zip()`.

def parte_4_for():
    print("=== PARTE 4: for ===")

    # 4.1 Lo basico: recorrer directamente
    frutas = ["manzana", "pera", "uva"]
    for fruta in frutas:
        print(f"Fruta: {fruta}")

    # 4.2 range: cuando necesitas numeros
    #    range(fin) | range(inicio, fin) | range(inicio, fin, paso)
    #    OJO: el limite final NUNCA se incluye.
    print(f"range(3)          -> {list(range(3))}")
    print(f"range(2, 6)       -> {list(range(2, 6))}")
    print(f"range(10, 0, -2)  -> {list(range(10, 0, -2))}")

    # 4.3 enumerate: indice + valor (forma correcta, sin range(len(...)))
    for pos, fruta in enumerate(frutas, start=1):
        print(f"{pos}. {fruta}")

    # 4.4 zip: recorrer varias secuencias a la vez
    nombres = ["Ana", "Luis", "Eva"]
    notas = [8.5, 6.0, 9.2]
    for nombre, nota in zip(nombres, notas):
        estado = "Aprobado" if nota >= 7 else "Desaprobado"
        print(f"{nombre}: {nota} -> {estado}")

    # 4.5 items(): recorrer un diccionario correctamente
    precios = {"pan": 1.5, "leche": 0.9}
    for producto, precio in precios.items():
        print(f"{producto}: {precio:.2f}")

    # 4.6 Acumuladores: for sirve para CONSTRUIR un resultado
    total = 0
    for p in precios.values():
        total += p
    print(f"Total: {total:.2f}")

    # 4.7 Comprension de listas: el reemplazo de for + append
    cuadrados = [n * n for n in range(1, 6)]
    print(f"Cuadrados: {cuadrados}")

    # 4.8 break / continue / else dentro de for
    for n in range(2, 10):
        for divisor in range(2, n):
            if n % divisor == 0:
                break                # no es primo, cortamos
        else:
            print(f"{n} es primo")    # el else del for: nadie hizo break

    # 4.9 LO QUE NO SE DEBE HACER: modificar la lista mientras la recorres
    #   MAL:  for x in lista: lista.remove(x)
    #   BIEN: for x in lista[:]: ...   (copia)  o  lista = [x for x in lista if ...]
    numeros = [1, 2, 2, 3, 2]
    limpia = [x for x in numeros if x != 2]
    print(f"Sin doses: {limpia}")

    print()


# =====================================================================
if __name__ == "__main__":
    parte_1_print()
    parte_2_match_case()
    parte_3_while()
    parte_4_for()
