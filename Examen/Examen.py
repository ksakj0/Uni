#EXAMEN

num = int(input("Ingresa un numero entero positivo: "))
operaciones = 0
if num == 1:
    print(f"{'===':^5}{'Numero Final:':^5}{num:^5}{'===':^5}\n{'===':^5}{'Operaciones realizadas:':^5}{operaciones:^5}{'===':^5}")
else:
    while num > 1:
        if num % 2 == 0:
            num /= 2
            operaciones += 1
            print(f"{'Numero Actual:':^5}{num:^5}\n{'Operaciones realizadas:':^5}{operaciones:^5}\n")
        else:
            operaciones += 1
            num = num * 3 + 1
            print(f"{'Numero Actual:':^5}{num:^5}\n{'Operaciones realizadas:':^5}{operaciones:^5}\n")
    print(f"{'===':^5}{'Numero Final:':^5}{num:^5}{'===':^5}\n{'===':^5}{'Operaciones realizadas:':^5}{operaciones:^5}{'===':^5}")