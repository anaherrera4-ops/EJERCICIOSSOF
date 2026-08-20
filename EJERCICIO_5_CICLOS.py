continuar = "s"

while continuar == "s":
    numero = int(input("Ingrese un número entre 0 y 20: "))

    if numero < 0 or numero > 20:
        print("Error: el número debe estar entre 0 y 20")
    else:
        factorial = 1
        i = 1
        while i <= numero:
            factorial = factorial * i
            i = i + 1
        print("El factorial de", numero, "es:", factorial)

    continuar = input("¿Desea volver a empezar? (s/n): ")

print("Programa finalizado")
