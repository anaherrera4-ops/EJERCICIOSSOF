a = float(input("Ingrese el valor de a: "))
n = int(input("Ingrese el valor de n: "))

resultado = 0
contador = 1

while contador <= n:
    resultado = resultado + (1/a) ** contador
    contador = contador + 1

print("El resultado de la sumatoria es:", resultado)
