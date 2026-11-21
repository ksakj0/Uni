dim = 15
sala = []
letras = "abcdefghijklmno"
total_ocupados = 0

for f in range(dim):
    fila = []
    for c in range(dim):
        fila.append("X")
    sala.append(fila)

while True:
    opcion = input("\n\nDesearia comprar boletos para la sala? [s/n]: ").lower()

    match opcion:
        case "s":
            print(f"\n{'===':^23}SALA DE CINE{'===':^23}\n")
            print("    ", end="")
            for letra in letras:
                print(letra.upper(), end=" ")
            print()
            for i in range(dim):
                print(f"{i + 1:>2}  ", end="")
                for j in range(dim):
                    print(sala[i][j], end=" ")
                print()

            input("\n\nPresiona ENTER si estas listo para elegir asiento...")
            fila_elegida = int(input("\n\nQue fila quieres? "))
            col_elegida = input("Que columna quieres? ").lower()

            col_index = -1
            for k in range(len(letras)):
                if letras[k] == col_elegida:
                    col_index = k

            fila_index = fila_elegida - 1

            if fila_index < 0 or fila_index >= dim or col_index == -1:
                print("\nFila o columna fuera de rango")
            elif sala[fila_index][col_index] == "☻":
                print("\nEse asiento ya esta ocupado")
            else:
                sala[fila_index][col_index] = "☻"
                total_ocupados += 1
                print("\nAsiento reservado")

            print(f"\n{'===':^23}SALA DE CINE{'===':^23}\n")
            print("    ", end="")
            for letra in letras:
                print(letra.upper(), end=" ")
            print()
            for i in range(dim):
                print(f"{i + 1:>2}  ", end="")
                for j in range(dim):
                    print(sala[i][j], end=" ")
                print()

            asientos_libres = (dim * dim) - total_ocupados
            print(f"\n\n=={'ASIENTOS LIBRES':^30}==\n\n{asientos_libres:^34}\n")
            print(f"=={'ASIENTOS OCUPADOS':^30}==\n\n{total_ocupados:^34}\n")
            input("\nPresiona ENTER para continuar...")

        case "n":
            print("\nVuelva pronto!!!")
            break

        case _:
            print("\nOpcion no valida, por favor elige alguna de las validas: [s/n]")
