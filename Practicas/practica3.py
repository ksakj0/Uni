cine = []
abc = "abcdefghijklmno"
cont = 0
for fila in range(15):
    asientos = []
    for columna in range(15):
        asientos.append('X')
    cine.append(asientos)
    
def sala(cine):
    print(f"{'':^20} {'=' * 10} {'SALA DE CINE':^10} {'=' * 10}")
    print(f"{'':^2} {'A':^5} {'B':^3} {'C':^5} {'D':^3} {'E':^5} {'F':^4} {'G':^4} {'H':^4} {'I':^4} {'J':^4} {'K':^4} {'L':^4} {'M':^4} {'N':^4} {'O':^4}")
    for r, fila in enumerate(cine):
        if r+1<10:
            print(f"{r+1}  {fila}")
        else:
            print(f"{r+1} {fila}")
            
while True:
    op = input("Desearia comprar boletos para la sala? [s/n]\n").lower()
    match op:
        case "s":
            cont = 0
            sala(cine)
            print("Presiona ENTER si estas listo para elegir asiento...")
            input('')
            a = int(input("Que fila quieres? "))
            b = input("Que columna quieres? ").lower()
            for i, j in enumerate(abc):
                if j == b:
                    cine[a-1][i] = '☻'
            
            sala(cine)

            for fila in cine:
                for asiento in fila:
                    if asiento == 'X':
                        cont += 1
            print("\n\n")
            print(f"{'':^20} {'=' * 10} {'ASIENTOS LIBRES':^10} {'=' * 10}")
            print(f"\n{'':<39}{cont}\n")
            print(f"{'':^20} {'=' * 10} {'ASIENTOS OCUPADOS':^10} {'=' * 10}")
            print(f"\n{'':<40}{15*15-cont}\n")
            
            print("Presiona ENTER...")
            input('')
        case "n":
            print("Vuelva pronto!!!")
            break
        case _:
            print("Opcion no valida, por favor elige alguna de las validas: [s/n]")