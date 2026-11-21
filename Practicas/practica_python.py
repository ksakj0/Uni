# -*- coding: utf-8 -*-
"""
PRACTICA DE PYTHON - 16 ejercicios simples
==========================================
Temas: print / f-strings, match-case, while y for.

COMO USARLO
-----------
1. Abre este archivo en tu editor.
2. Cada ejercicio es una funcion con `raise NotImplementedError`.
   Borra esa linea y escribe TU solucion.
3. Guarda y ejecuta:      python practica_python.py

El programa revisa tus respuestas solo y te dice [OK] o [XX].
No mires el final del archivo para "adivinar": los chequeos solo
describen QUE se espera, no COMO hacerlo.

Requiere Python 3.10 o superior (por el match-case).
Nota: en Python no existe printf; se usa print.
"""


# =====================================================================
# BLOQUE 1 - print y f-strings
# =====================================================================

def saludo(nombre):
    """Imprime exactamente:  Hola, Ana!
    (usa print con f-string; debe terminar en salto de linea)

    saludo("Ana")  ->  imprime "Hola, Ana!"
    """
    print(f"Hola, {nombre}!")


def tabla_multiplicar(n):
    """Imprime la tabla del n del 1 al 10, una linea por multiplicacion,
    con este formato exacto (espacios incluidos):

    3 x 1 = 3
    3 x 2 = 6
    ...
    3 x 10 = 30

    Pista: puedes recorrer la tabla con un for.
    """
    for i in range (1, 11):
        (print(f"{n} x {i} = {n*i}"))


def formato_precio(cantidad):
    """Imprime el precio con 2 decimales y la palabra EUR:

    formato_precio(19.5)  ->  imprime "Total: 19.50 EUR"
    formato_precio(5)     ->  imprime "Total: 5.00 EUR"
    """
    print(f"Total: {cantidad:.2f} EUR")


# =====================================================================
# BLOQUE 2 - match / case
# =====================================================================

def dia_semana(n):
    """Devuelve (return) el nombre del dia en minusculas.
    1=lunes, 2=martes, 3=miercoles, 4=jueves, 5=viernes,
    6=sabado, 7=domingo. Cualquier otro numero -> "Dia no valido".

    dia_semana(1) -> "lunes"
    dia_semana(9) -> "Dia no valido"
    """
    match n:
        case 1:
            return("lunes")
        case 2:
            return("martes")
        case 3:
            return("miercoles")
        case 4:
            return("jueves")
        case 5:
            return("viernes")
        case 6:
            return("sabado")
        case 7:
            return("domingo")
        case _:
            return("Dia no valido")
            
def tipo_dato(valor):
    """Devuelve el tipo del valor usando match con patrones de tipo:
    int -> "entero" | str -> "texto" | float -> "decimal" | otro -> "otro"

    OJO con el orden: los bool son int en Python, no te preocupes por eso.
    Pista: `case int():` y `case _:` (recuerda que float NO es int).
    """
    match valor:
        case int():
            return("entero")
        case str():
            return("texto")
        case float():
            return("decimal")
        case _:
            return("otro")


def estacion(mes):
    """Devuelve la estacion del mes (1 a 12), o "mes no valido".
    12, 1, 2 -> "invierno" | 3, 4, 5 -> "primavera"
    6, 7, 8  -> "verano"   | 9, 10, 11 -> "otono"
    Cualquier otro numero -> "mes no valido"

    Pista: en un case puedes combinar opciones con el operador | :
          case 12 | 1 | 2:
    """
    match mes:
        case 12| 1 | 2:
            return("invierno")
        case 3| 4 | 5:
            return("primavera")
        case 6| 7 | 8:
            return("verano")
        case 9| 10 | 11:
            return("otono")
        case _:
            return("mes no valido")


# =====================================================================
# BLOQUE 3 - while
# =====================================================================

def contar_hasta(n):
    """Devuelve una lista [1, 2, 3, ..., n] construida con un while.
    Si n es 0 o negativo, devuelve una lista vacia [].

    contar_hasta(5) -> [1, 2, 3, 4, 5]
    contar_hasta(0) -> []
    """
    lista = []
    i = 1
    while i <= n:
        lista.append(i)
        i += 1
    return lista

def suma_digitos(n):
    """Devuelve la suma de los digitos de n, usando while con % 10 y // 10.
    No conviertas el numero a texto.

    suma_digitos(1234) -> 10      (1+2+3+4)
    suma_digitos(0)    -> 0
    """
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def invertir_numero(n):
    """Devuelve el numero con sus digitos al reves, usando while.
    No conviertas el numero a texto.

    invertir_numero(1234) -> 4321
    invertir_numero(100)  -> 1
    """
    resultado = 0
    while n > 0:
        resultado = resultado * 10 + n % 10
        n //= 10
    return resultado


def primer_multiplo_de(n, minimo):
    """Devuelve el multiplo de n mas pequeno que sea >= minimo, usando while.

    primer_multiplo_de(7, 20) -> 21
    primer_multiplo_de(3, 9)  -> 9
    """
    raise NotImplementedError


# =====================================================================
# BLOQUE 4 - for
# =====================================================================

def sumar_sin_sum(numeros):
    """Devuelve la suma de la lista usando un for con acumulador.
    Prohibido usar la funcion sum().

    sumar_sin_sum([1, 2, 3, 4]) -> 10
    sumar_sin_sum([])           -> 0
    """
    raise NotImplementedError


def mayor_y_menor(numeros):
    """Devuelve una tupla (mayor, menor) usando for.
    Prohibido usar max() y min(). La lista nunca viene vacia.

    mayor_y_menor([3, 9, 1, 7]) -> (9, 1)
    mayor_y_menor([5])          -> (5, 5)
    """
    raise NotImplementedError


def contar_vocales(texto):
    """Cuenta cuantas vocales (a, e, i, o, u) tiene el texto, con un for.
    Cuenta mayusculas y minusculas. No hace falta contar acentos.

    contar_vocales("Hola Mundo") -> 4
    contar_vocales("xyz")        -> 0
    """
    raise NotImplementedError


def numeros_pares(limite):
    """Devuelve la lista de pares desde 2 hasta limite (incluido), con range
    y el parametro de paso. Si limite es impar, el ultimo par es menor.

    numeros_pares(10) -> [2, 4, 6, 8, 10]
    numeros_pares(7)  -> [2, 4, 6]
    """
    raise NotImplementedError


def cuadrados_hasta(n):
    """Devuelve [1, 4, 9, ..., n*n] usando una comprension de listas.

    cuadrados_hasta(5) -> [1, 4, 9, 16, 25]
    """
    raise NotImplementedError


def indice_de(lista, valor):
    """Devuelve la posicion (indice, empezando en 0) donde aparece `valor`,
    o -1 si no esta. Usa enumerate y el `else` del for.

    indice_de(["a", "b", "c"], "c") -> 2
    indice_de(["a", "b"], "z")      -> -1
    """
    raise NotImplementedError


# =====================================================================
# VERIFICADOR AUTOMATICO  (no necesitas tocar nada de aqui abajo)
# =====================================================================

import contextlib
import io


def _capturar(funcion, *args):
    """Ejecuta la funcion capturando lo que imprime con print."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        funcion(*args)
    return buffer.getvalue()


def _tabla_esperada(n):
    return "".join(f"{n} x {i} = {n * i}\n" for i in range(1, 11))


CHEQUEOS = [
    # (numero, nombre, prueba, resultado esperado, pista)
    ("1", "saludo", lambda: _capturar(saludo, "Ana"), "Hola, Ana!\n",
     'f"Hola, {nombre}!" pasa el nombre, no la palabra nombre'),
    ("2", "tabla_multiplicar", lambda: _capturar(tabla_multiplicar, 3), _tabla_esperada(3),
     "un for de 1 a 10 y f-string con el formato exacto"),
    ("3", "formato_precio", lambda: _capturar(formato_precio, 19.5), "Total: 19.50 EUR\n",
     "prueba (5) aparte: quieres 5.00, asi que usa :.2f"),

    ("4", "dia_semana", lambda: (dia_semana(1), dia_semana(7), dia_semana(9)),
     ("lunes", "domingo", "Dia no valido"), "7 case + case _ para lo demas"),
    ("5", "tipo_dato", lambda: (tipo_dato(5), tipo_dato("a"), tipo_dato(3.5), tipo_dato([1])),
     ("entero", "texto", "decimal", "otro"), "case int(): / str(): / float(): / _:"),
    ("6", "estacion", lambda: (estacion(1), estacion(4), estacion(7), estacion(10), estacion(13)),
     ("invierno", "primavera", "verano", "otono", "mes no valido"), "agrupa meses con |"),

    ("7", "contar_hasta", lambda: (contar_hasta(5), contar_hasta(0)),
     ([1, 2, 3, 4, 5], []), "i = 1 antes del while; i += 1 dentro"),
    ("8", "suma_digitos", lambda: (suma_digitos(1234), suma_digitos(0)),
     (10, 0), "while n > 0: n % 10 y luego n //= 10"),
    ("9", "invertir_numero", lambda: (invertir_numero(1234), invertir_numero(100)),
     (4321, 1), "acumula resultado = resultado * 10 + digito"),
    ("10", "primer_multiplo_de", lambda: (primer_multiplo_de(7, 20), primer_multiplo_de(3, 9)),
     (21, 9), "empieza en minimo y sube de uno en uno hasta que sea divisible"),

    ("11", "sumar_sin_sum", lambda: (sumar_sin_sum([1, 2, 3, 4]), sumar_sin_sum([])),
     (10, 0), "total = 0 antes del for"),
    ("12", "mayor_y_menor", lambda: (mayor_y_menor([3, 9, 1, 7]), mayor_y_menor([5])),
     ((9, 1), (5, 5)), "inicializa con el primer elemento de la lista"),
    ("13", "contar_vocales", lambda: (contar_vocales("Hola Mundo"), contar_vocales("xyz")),
     (4, 0), "pasa el texto a minusculas antes de comparar"),
    ("14", "numeros_pares", lambda: (numeros_pares(10), numeros_pares(7)),
     ([2, 4, 6, 8, 10], [2, 4, 6]), "range(2, limite + 1, 2)"),
    ("15", "cuadrados_hasta", lambda: cuadrados_hasta(5), [1, 4, 9, 16, 25],
     "[algo for n in ...]"),
    ("16", "indice_de", lambda: (indice_de(["a", "b", "c"], "c"), indice_de(["a", "b"], "z")),
     (2, -1), "for i, x in enumerate(lista): ... return i, con else: return -1"),
]


def main():
    print("=" * 62)
    print("REVISION DE TUS EJERCICIOS")
    print("=" * 62)

    resueltos = 0
    for numero, nombre, prueba, esperado, pista in CHEQUEOS:
        try:
            obtenido = prueba()
        except NotImplementedError:
            print(f"[--] {numero:>2}. {nombre:<20} sin implementar")
            continue
        except Exception as error:
            print(f"[!!] {numero:>2}. {nombre:<20} {type(error).__name__}: {error}")
            continue

        if obtenido == esperado:
            resueltos += 1
            print(f"[OK] {numero:>2}. {nombre}")
        else:
            print(f"[XX] {numero:>2}. {nombre:<20} esperado {esperado!r}")
            print(f"     {'':<20} obtuviste {obtenido!r}")
            print(f"     pista: {pista}")

    total = len(CHEQUEOS)
    print("-" * 62)
    print(f"Resultado: {resueltos}/{total} ejercicios correctos")
    if resueltos == total:
        print("Excelente: los 16 estan bien. Pide la parte 2 con dificultad media.")
    else:
        print("Corrige los [XX] / [!!] y vuelve a ejecutar el archivo.")


if __name__ == "__main__":
    main()
