'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''

ahorro_total = 0

for mes in range(1, 13):
    deposito = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
    ahorro_total += deposito
    print(f"Ahorro acumulado hasta el mes {mes}: {ahorro_total:.2f}")

print(f"\nEl total ahorrado al final del año es: {ahorro_total:.2f}")
