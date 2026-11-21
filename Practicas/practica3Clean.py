tam = 15
cine = []
abc = "abcdefghijklmno"
ocupados = 0
for fila in range(tam):
    asientos = []
    for columna in range(tam):
        asientos.append('X')
    cine.append(asientos)

def sala(matriz):
    print(f"\n{'===':^23}SALA DE CINE{'===':^23}\n")
    print("    ", end="")
    for letra in abc:
        print(letra.upper(), end=" ")
    print()
    for r, fila in enumerate(matriz):
        print(f"{r + 1:>2}  ", end="")
        for asiento in fila:
            print(asiento, end=" ")
        print()

while True:
    op = input("\n\nDesearia comprar boletos para la sala? [s/n]: ").lower()
    match op:
        case "s":
            sala(cine)
            input("\n\nPresiona ENTER si estas listo para elegir asiento...")
            a = int(input("\n\nQue fila quieres? "))
            b = input("Que columna quieres? ").lower()

            col = -1
            for i, j in enumerate(abc):
                if j == b:
                    col = i

            if a < 1 or a > tam or col == -1:
                print("\nFila o columna fuera de rango")
            elif cine[a - 1][col] == '☻':
                print("\nEse asiento ya esta ocupado")
            else:
                cine[a - 1][col] = '☻'
                ocupados += 1
                print("\nAsiento reservado")

            sala(cine)
            print(f"\n\n=={'ASIENTOS LIBRES':^30}==\n\n{tam * tam - ocupados:^34}\n")
            print(f"=={'ASIENTOS OCUPADOS':^30}==\n\n{ocupados:^34}\n")
            input("\nPresiona ENTER para continuar...")
        case "n":
            print("\nVuelva pronto!!!")
            break
        case _:
            print("\nOpcion no valida, por favor elige alguna de las validas: [s/n]")