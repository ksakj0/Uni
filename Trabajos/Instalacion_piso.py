largo = float(input("Ingresa el largo que tiene el piso\n"))
ancho = float(input("Ingresa el ancho que tiene el piso\n"))
precio_piso = float(input("Ingresa el precio por metro cuadrado de piso\n"))
precio_instalacion = float(input("Ingresa el costo que tiene la nstalacion por metro cuadrado\n"))

superficie_comprar = largo * ancho * 1.10
costo_material = superficie_comprar * precio_piso
costo_instalacion = (largo *ancho) * precio_instalacion

total = costo_material + costo_instalacion

print("Los costos de instalacion son: $", total, "\nSuperficie a comprar:", superficie_comprar)
print("El costo del material es de: $", costo_material, "\nEl costo de la instalacion es de: $", costo_instalacion)