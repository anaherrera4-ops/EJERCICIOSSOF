pi = 3.1416

peso1 = float(input("Ingrese el peso de la esfera 1: "))
radio1 = float(input("Ingrese el radio de la esfera 1: "))

peso2 = float(input("Ingrese el peso de la esfera 2: "))
radio2 = float(input("Ingrese el radio de la esfera 2: "))

peso3 = float(input("Ingrese el peso de la esfera 3: "))
radio3 = float(input("Ingrese el radio de la esfera 3: "))

volumen1 = (4/3) * pi * (radio1 ** 3)
volumen2 = (4/3) * pi * (radio2 ** 3)
volumen3 = (4/3) * pi * (radio3 ** 3)

densidad1 = peso1 / volumen1
densidad2 = peso2 / volumen2
densidad3 = peso3 / volumen3

if densidad1 > densidad2 and densidad1 > densidad3:
    print("La esfera 1 tiene mayor densidad")
elif densidad2 > densidad1 and densidad2 > densidad3:
    print("La esfera 2 tiene mayor densidad")
else:
    print("La esfera 3 tiene mayor densidad")
