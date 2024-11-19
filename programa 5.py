'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''

suma = 0

for _ in range(10):
    numero = float(input("Introduce un número: "))
    suma += numero

promedio = suma / 10
print(f"El promedio de los números introducidos es: {promedio}")
