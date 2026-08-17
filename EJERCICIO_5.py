pasos=int(input("ingrese el número de pasos: "))#pedir los pasos
totalencm= pasos*45
km=totalencm//100000 # // es la división entera, divide y descarta el resto(no décimales)
metros = (totalencm % 100000) // 100
centimetros = totalencm % 100
print(f"Avanzó {km} km, {metros} metros y {centimetros} centímetros")
