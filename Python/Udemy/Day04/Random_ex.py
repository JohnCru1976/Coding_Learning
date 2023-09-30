from random import *
#from random import randint

## RANDINT : Probabilidad de que salga la lotería
numero_elegido = 99535

contador = 0
for n in range(36500):
    if numero_elegido == randint(0,99999):
        contador += 1

print(f"El {numero_elegido} ha salido {contador} veces")
print(f"La probabilidad ha sido de {contador/100}%")

## UNIFORM: devuelve un valor decimal
aleatorio = uniform(0.5,0.6)
print(aleatorio)
aleatorio = uniform(5,6)
print(aleatorio)

## RANDOM: devuelve float entre 0 y 1
aleatorio = random()
print(aleatorio)

## CHOICE: trabaja sobre una lista
lista = ["azul", "verde", "rojo", "amarillo", "carmesí"]
print(choice(lista))

## SHUFFLE: mezcla de valores de un coleccionable
lista = list(range(5, 50, 5))
print(lista)
shuffle(lista)  # Función in-place: no devuelve nada
print(lista)


