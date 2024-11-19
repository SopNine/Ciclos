'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''

while True:
    limite_inferior = int(input("Introduce el límite inferior: "))
    limite_superior = int(input("Introduce el límite superior: "))
    if limite_inferior < limite_superior:
        break
    print("El límite inferior debe ser menor que el superior. Inténtalo de nuevo.")

suma_dentro = 0
fuera_intervalo = 0
igual_a_limites = False

while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    if limite_inferior < numero < limite_superior:  
        suma_dentro += numero
    else:  
        fuera_intervalo += 1
    if numero == limite_inferior or numero == limite_superior:  
        igual_a_limites = True

print(f"\nResultados:")
print(f"Suma de los números dentro del intervalo: {suma_dentro}")
print(f"Números fuera del intervalo: {fuera_intervalo}")
if igual_a_limites:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
