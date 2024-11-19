'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''


import random

numero_a_adivinar = random.randint(1, 100)
intentos = 10

while intentos > 0:
    intento_usuario = int(input("Introduce un número entre 1 y 100: "))
    
    if intento_usuario == numero_a_adivinar:
        print(f"¡Acertaste! El número era {numero_a_adivinar}. Lo lograste en {10 - intentos + 1} intento(s).")
        break
    elif intento_usuario < numero_a_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")
    
    intentos -= 1
    print(f"Te quedan {intentos} intento(s).")

if intentos == 0:
    print(f"Lo siento, se acabaron los intentos. El número era {numero_a_adivinar}.")
