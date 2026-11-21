"""
Generador de tickets en texto plano.
Modifica los valores en la sección "DATOS DEL TICKET" según necesites.
"""

from datetime import datetime

# ==================== DATOS DEL TICKET ====================
NEGOCIO = "MI NEGOCIO S.A. DE C.V."
DIRECCION = "Calle Falsa 123, Guadalajara, Jal."
TELEFONO = "Tel: 33-1234-5678"
RFC = "RFC: XAXX010101000"

FOLIO = "0001"
ITEMS = [
    # (descripcion, cantidad, precio_unitario)
    ("Producto A", 45.00),
    ("Producto B", 120.50),
    ("Servicio C", 15.00),
]
ANCHO = 50  # ancho del ticket en caracteres
# ============================================================


def linea(caracter="-", ancho=ANCHO):
    return caracter * ancho


def centrar(texto, ancho=ANCHO):
    return texto.center(ancho)


def fila_item(desc, precio, ancho=ANCHO):
    importe = precio
    izq = f"{desc[:18]:<18}"
    der = f"${importe:>8.2f}"
    espacio = ancho - len(izq) - len(der)
    return f"{izq}{' ' * max(espacio, 1)}{der}"


def generar_ticket():
    lineas = []
    lineas.append(centrar(NEGOCIO))
    lineas.append(centrar(DIRECCION))
    lineas.append(centrar(TELEFONO))
    lineas.append(centrar(RFC))
    lineas.append(linea())
    lineas.append(f"Folio: {FOLIO}")
    lineas.append(linea())

    subtotal = 0
    for desc, precio in ITEMS:
        lineas.append(fila_item(desc, precio))
        subtotal += precio

    total = subtotal

    lineas.append(linea())
    lineas.append(f"{'Subtotal:':<{ANCHO-10}}${subtotal:>8.2f}")
    lineas.append(linea("="))
    lineas.append(f"{'TOTAL:':<{ANCHO-10}}${total:>8.2f}")
    lineas.append(linea("="))


    return "\n".join(lineas)


if __name__ == "__main__":
    ticket = generar_ticket()
    print(ticket)
