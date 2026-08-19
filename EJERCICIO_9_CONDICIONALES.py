n1 = float(input("Ingrese el dato 1: "))
n2 = float(input("Ingrese el dato 2: "))
n3 = float(input("Ingrese el dato 3: "))
n4 = float(input("Ingrese el dato 4: "))

mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4

suma = mayor + menor
print("La suma del mayor y el menor es:", suma)
