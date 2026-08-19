A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

if A > B and A > C:
    if B > C:
        print(A, B, C)
    else:
        print(A, C, B)
elif B > A and B > C:
    if A > C:
        print(B, A, C)
    else:
        print(B, C, A)
else:
    if A > B:
        print(C, A, B)
    else:
        print(C, B, A)
