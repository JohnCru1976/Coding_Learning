'''Módulo main del programa TURNOS'''
from os import system
from numeros import *

def pantalla_eleccion():
    '''Funcion con la pantalla de presentación que devuelve la opción elegida'''

    opcion = ""
    while not opcion or opcion not in "fcps":
        system("cls")

        print("*" * 10)
        print("COGE TURNO")
        print("*" * 10 + "\n")
        print("[F] Farmacia")
        print("[C] Cosmética")
        print("[P] Perfumería")
        print("[S] Salir\n")

        opcion = input("Selecciona una de las opciones: ").lower()
        print(" ")

    return opcion

def mostrar_turno(opcion):
    '''Función que muestra el turno en función de la opción elegida'''
    system("cls")
    if opcion == "s":
        print("Ha sido un placer ser de utilidad")
        print("Nos vemos en otra ocasión")
        return True
    elif opcion == "c":
        print(siguiente_cosmetica())
        input("\nPulsa Enter para volver al menú principal...")
        return False
    elif opcion == "f":
        print(siguiente_farmacia())
        input("\nPulsa Enter para volver al menú principal...")
        return False
    elif opcion == "p":
        print(siguiente_perfume())
        input("\nPulsa Enter para volver al menú principal...")
        return False
    else:
        print("Ha habido algún tipo de error")
        print("El programa se ha interrumpido")
        return True

if __name__ == "__main__":
    FIN = False
    while not FIN:
        FIN = mostrar_turno(pantalla_eleccion())
