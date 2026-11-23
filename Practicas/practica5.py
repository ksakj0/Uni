clave = []
desc = [""]
price = []

size = int(input("Cuantos elementos tendra la lista? "))   

clave = [0] * size
desc = [None] * size
price = [0] * size

print(f"{clave}")
l = len(clave)
for i in range(l):
    clave[i] = input(f"Ingresa la clave del articulo {i+1}: ")
    desc[i] = input(f"Ingresa la descripcion de dicha clave: ")
    price[i] = float(input(f"Ingresa el precio del articulo: "))
print(f"Claves de articulos:\n{clave}")
print(f"Descripciones:\n{desc}")
print(f"Precios:\n{price}")

mayor = price[0]
l = len(clave)
for i in range(l):
    if price[i] > mayor:
        mayor = price[i]
print(mayor)

suma = 0
for i1 in range(l):
    suma += price[i1]
promedio = suma / (l)
print(f"Promedio: {promedio:.2f}")


print(f"Claves de articulos:\n{clave}")
print(f"Descripciones:\n{desc}")
print(f"Precios:\n{price}")
search = input("Ingresa la clave que desea eliminar: ")

flag = False
for i2 in range(l):
    if search == clave[i2]:
        clave.pop(i2)
        desc.pop(i2)
        price.pop(i2)
        flag = True
        break
if not flag:
    print("Clave incorrecta")

search2 = input("Ingresa la clave que desea consultar: ")
for i3 in range(l):
    if search2 == clave[i3]:
        print(clave[i3])
        print(desc[i3])
        print(price[i3])
        break

search3 = input("Ingresa la clave que desea modificar: ")
for i4 in range(l):
    if search3 == clave[i4]:
        clave[i3] = input(f"Ingresa la nueva clave del articulo {search3}: ")
        desc[i3] = input(f"Ingresa la nueva descripcion de dicha clave: ")
        price[i3] = float(input(f"Ingresa el nuevo precio del articulo: "))
        break
print(f"Claves de articulos:\n{clave}")
print(f"Descripciones:\n{desc}")
print(f"Precios:\n{price}")
