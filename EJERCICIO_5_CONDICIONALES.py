inscripcion = input("Ingrese el número de inscripción: ")
nombres = input("Ingrese los nombres: ")
patrimonio = float(input("Ingrese el patrimonio: "))
estrato = int(input("Ingrese el estrato: "))

pago = 50000

if patrimonio > 2000000 and estrato > 3:
    pago = pago + (patrimonio * 0.03)

print("Número de inscripción:", inscripcion)
print("Nombres:", nombres)
print("Pago de matrícula:", pago)
