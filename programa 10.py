'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''

base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = 1

    for _ in range(exponente):
        resultado *= base

    print(f"{base} elevado a la {exponente} es {resultado}")
