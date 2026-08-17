Y = float(input("Ingrese el valor de Y: "))
Z = float(input("Ingrese el valor de Z: "))

if Y > Z:
    X = 1
elif Y == Z:
    X = 2
else:
    X = 3

print(f"El valor de X es: {X}")