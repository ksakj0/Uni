calif1 = int(input("Ingresa la calificacion de tu primer parcial\n"))
calif2 = int(input("Ingresa la calificacion de tu segundo parcial\n"))
calif3 = int(input("Ingresa la calificacion de tu tercer parcial\n"))

nota_final = calif1 * 0.25 + calif2 * 0.35 + calif3 * 0.40

print("Las notas que has obtenido son:")
print("Primer parcial:", calif1, "\nSegundo parcial:", calif2, "\nTercer parcial", calif3)
print("Tu nota final es de:", nota_final)