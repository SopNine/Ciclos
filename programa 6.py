'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''

cantidad = int(input("¿Cuántos números deseas introducir? "))

mayores = menores = iguales = 0

for _ in range(cantidad):
    numero = int(input("Introduce un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

# Muestra los resultados
print(f"Mayores que 0: {mayores}")
print(f"Menores que 0: {menores}")
print(f"Iguales a 0: {iguales}")
