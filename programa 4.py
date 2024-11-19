'''
Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''

for numero in range(1, 6):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()
