numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = 0
contador = 0

while contador < numero2:
    resultado = resultado + numero1
    contador = contador + 1

print("El resultado de la multiplicación es:", resultado)
