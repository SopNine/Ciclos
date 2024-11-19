'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''

numero = int(input("Introduce un número entero: "))

print(f"El número {numero} en binario es: {bin(numero)[2:]}")
