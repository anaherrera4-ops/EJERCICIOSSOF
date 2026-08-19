n = int(input("Ingrese un número entero positivo (máximo 9): "))
x = int(input("Ingrese el exponente x (máximo 9): "))

i = 0
while i <= n:
    resultado = i ** x
    print(resultado)
    i = i + 1
