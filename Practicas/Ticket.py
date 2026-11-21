nombre = input("Ingresa tu nombre: ")
diario = float(input("Ingresa tu sueldo diario: "))
dias = int(input("Ingresa los dias trabajados: "))

base = diario * dias
print(f"Nombre: {nombre}\nSueldo diario: {diario}\nDias laborados: {dias}")
print(f"Sueldo neto: {base}\nProductividad: {base * 0.12:.2f}\nGuarderia: {base * 0.10:.2f}\nDespensa: {base * 0.08:.2f}")
print(f"Salud: {base * 0.06:.2f}\nSeguro: {base * 0.05:.2f}\nISR: {base * 0.20:.2f}")
print(f"Percepciones: {base + (base * 0.12) + (base * 0.10) + (base * 0.08):.2f}")
print(f"Deducciones: {(base * 0.06) + (base * 0.05) + (base * 0.20):.2f}")
print(f"Neto: {(base + (base * 0.12) + (base * 0.10) + (base * 0.08)) - ((base * 0.06) + (base * 0.05) + (base * 0.20)):.2f}")