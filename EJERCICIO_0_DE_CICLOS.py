# Solicitar los dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Al primer número se le suma 3, cuatro veces (reasignando cada vez)
numero1 = numero1 + 3
numero1 = numero1 + 3
numero1 = numero1 + 3
numero1 = numero1 + 3

# Al segundo número se le multiplica por 3, tres veces (reasignando cada vez)
numero2 = numero2 * 3
numero2 = numero2 * 3
numero2 = numero2 * 3

# Solicitar al usuario que copie los nombres de dichos números, usando formateo en el input
nombre1 = input(f"Copie el nombre de la variable con valor {numero1}: ")
nombre2 = input(f"Copie el nombre de la variable con valor {numero2}: ")

# Formateo de strings - Forma 1: operador %
print("Forma 1 (%): El número %s tiene el valor %d" % (nombre1, numero1))
print("Forma 1 (%): El número %s tiene el valor %d" % (nombre2, numero2))

# Formateo de strings - Forma 2: método .format()
print("Forma 2 (.format()): El número {} tiene el valor {}".format(nombre1, numero1))
print("Forma 2 (.format()): El número {} tiene el valor {}".format(nombre2, numero2))

# Formateo de strings - Forma 3: f-string
print(f"Forma 3 (f-string): El número {nombre1} tiene el valor {numero1}")
print(f"Forma 3 (f-string): El número {nombre2} tiene el valor {numero2}")
