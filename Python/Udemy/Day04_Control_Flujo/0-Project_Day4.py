'''****************************************************
File: 0-Project04_Text_Analyzer.py
Description: Educational purpose project. The user
             have tu guess a random number between 0-100.
Date creation: 2023-09-26
Last update: 2023-09-26
Author: Juan B. Cru
****************************************************'''
from random import *

start = ""
random_number = randint(1, 100)

print("ADIVINA EL NÚMERO")
name = input("Dime tu nombre: ")

while not (start == "n" or start == "s"):
    start = input(
        f"Bueno, {name}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número, ¿quieres jugar? (S/N)").lower()

if start == "n":
    print("Pues nada, nos vemos en la siguiente")
else:
    for i in range(1, 9):
        number = 0
        while number < 1 or number > 100:
            number = int(input(f"Intento {i}, introduce tu número (1-100): "))
            if number < 1 or number > 100:
                print("El número elegido no está permitido")
        if number == random_number:
            print(
                f"¡Enhorabuena, el número es {number}! Has usado {i} intentos.")
            break
        elif number < random_number:
            if i == 8:
                print(f"Lo siento, has agotado los intentos. El número secreto es {random_number}")                
            else:
                print(f"Lo siento, {number} es menor que el número secreto")
        else:
            if i == 8:
                print(f"Lo siento, has agotado los intentos. El número secreto es {random_number}")                
            else:
                print(f"Lo siento, {number} es mayor que el número secreto")
            
    
