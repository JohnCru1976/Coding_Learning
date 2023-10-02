from os import system

print("Programa")

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

# Así se limpia la consola
system("cls")

print(f"Tu nombre es {nombre} y tienes {edad} años")