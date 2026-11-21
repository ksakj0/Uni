material_a = float(input("Ingresa el costo del material A\n"))
material_b = float(input("Ingresa el costo del material B\n"))
cantidad_a = int(input("Ingresa la cantidad de material A requerida\n"))
cantidad_b = int(input("Ingresa la cantidad de material B requerida\n"))
mano_obra = float(input("Ingresa el costo que tendra la mano de obra\n"))

costo_final = material_a * cantidad_a + material_b + cantidad_b + mano_obra

print("El costo de material A es de:", material_a, "\nY el de material B es de:", material_b)
print("La cantidad de material A que se utilizo fue de: ", cantidad_a, "\nY la de material b fue de: ", cantidad_b)
print("El costo de la mano de obra es de: $", mano_obra, "\nEl costo del producto sera de : $", costo_final)
