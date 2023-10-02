# Recorrer una lista de nombres
lista_nombres = ["Juan", "Jose", "Pepe", "María", "Josefa", "Javier"]

for nombre in lista_nombres:
    if nombre.startswith("J"):
        print(f"Índice {lista_nombres.index(nombre)}",
              f"Hola {nombre}", sep=" - ")

# Sumar los valores de una lista
numeros = [5, 1, 6, 1, 7, 1, 1]
suma = 0

for numero in numeros:
    suma += numero

print("La suma de los números de la lista es: " + str(suma)) 

# Recorrer un string
for letra in "No me toques los Pythons":
    print(letra)    

# Recorrer un dic
dic = {"v1": "coche", "v2": "casa", "v3": "ajedrez"}
for value in dic.values(): # Forma 1
    print (value)
for value in dic: # Forma 2
    print (dic[value])
for clave, valor in dic.items(): # Forma 3
    print(valor)
for item in dic.items(): # Forma 4
    print(item[1])

# ELSE EN UN BUCLE FOR

for i in range(5):
    if i == 3:
        break  # Para aquí si se cumple la condición
    print(i) # Imprime si no se cumple la condición
else: # Hace esto al final del bucle si no actúa break
    print("El bucle for se ha completado normalmente.")

print("Fin del programa")

