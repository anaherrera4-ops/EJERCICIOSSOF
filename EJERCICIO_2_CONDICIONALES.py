nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))
nota4 = float(input("Ingrese nota 4: "))
nota5 = float(input("Ingrese nota 5: "))

promedio = (nota1 * 0.30) + (nota2 * 0.15) + (nota3 * 0.15) + (nota4 * 0.20) + (nota5 * 0.20)

if promedio >= 3:
    print("Usted está Aprobado")
else:
    print("Usted está Reprobado")

print(f"Su promedio es: {promedio:.2f}")
