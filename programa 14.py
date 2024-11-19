'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''

cantidad = int(input("¿Cuántos números primos quieres mostrar? "))

contador = 0
numero = 2  

def es_primo(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while contador < cantidad:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1
