import os
from random import randint
from classes import *

def creacion_cliente():
    nombre = ""
    apellido = ""
    numero_cuenta = generador_numero_cuenta()
    balance = 0.0
    os.system("cls")
    print("BIENVENIDO A GESTIÓN BANCARIA\n")
    print("Introduce tus datos para registrarte como nuevo cliente")
    nombre = introduccion_datos_string("Nombre: ")
    apellido = introduccion_datos_string("Apellido: ")
    numero_cuenta = generador_numero_cuenta()
    
    return Cliente(nombre,apellido,numero_cuenta,balance)

def menu_principal(cliente):
    presentacion(cliente)
    eleccion = ""

    while eleccion not in "12s" or not eleccion:
        eleccion = input("Elige una opción: ").lower()

    while eleccion != "s":
        if eleccion == "1":
            depositar(cliente)            
        elif eleccion == "2":
            retirar(cliente)            
        elif eleccion == "s":
            break

        presentacion(cliente)
        eleccion = ""
        while eleccion not in "12s" or not eleccion:
            eleccion = input("Elige una opción: ").lower()
        
    
    if eleccion == "s":
        os.system("cls")
        print("Ha sido un placer tu elección por Gestión Bancaria\nEsperamos que te haya sido de utilidad")
        input("\nPulsa Enter para finalizar ...")
    else:
        os.system("cls")
        print("Ha habido algún tipo de error, el programa finalizará a continuación")
        input("\nPulsa Enter para finalizar ...")

def presentacion(cliente):
    os.system("cls")
    print("BIENVENIDO A GESTIÓN BANCARIA\n")
    print(cliente)
    print("\n[1] Depositar")
    print("[2] Retirar")
    print("[S] Salir")

def depositar(cliente):
    os.system("cls")
    print("BIENVENIDO A GESTIÓN BANCARIA\n")
    print(cliente)

    deposito = 0.0
    while not deposito or deposito < 0:
        try:
            deposito = round(float(input("\nIntroduce la cantidad a depositar: ")),2)
        except Exception as e:
            deposito = 0.0
    
    cliente.depositar(deposito)
    print(f"\nHas depositado {deposito} euros\n  El balance es de {cliente.balance} euros")
    input("\nPulsa Enter para continuar ...")

def retirar(cliente):
    os.system("cls")
    print("BIENVENIDO A GESTIÓN BANCARIA\n")
    print(cliente)

    retiro = 0.0
    while not retiro or retiro < 0:
        try:
            retiro = round(float(input("\nIntroduce la cantidad a retirar: ")),2)
        except Exception as e:
            retiro = 0.0
    
    resultado_retiro = cliente.retirar(retiro)
    if  resultado_retiro == -1:
        print(f"\nNo puedes retirar {retiro} euros\n  El balance es de {cliente.balance} euros")
        input("\nPulsa Enter para continuar ...")
    else:
        print(f"\nHas retirado {retiro} euros\n  El balance es de {resultado_retiro} euros")
        input("\nPulsa Enter para continuar ...")

def generador_numero_cuenta():
        cuenta = ""
        for digitos in range(1,19):
            cuenta += str(randint(0,9))
        return "ES" + cuenta

def introduccion_datos_string(prompt):
    dato = ""
    while not dato:
          dato = input(prompt)
    return dato
