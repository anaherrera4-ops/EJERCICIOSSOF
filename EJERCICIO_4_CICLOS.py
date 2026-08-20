N = int(input("Ingrese el valor de N: "))

suma = 0
numero = 1

while numero <= N:
    if numero % 2 != 0:
        suma = suma + numero
    numero = numero + 1

print("La suma de los números impares es:", suma)

