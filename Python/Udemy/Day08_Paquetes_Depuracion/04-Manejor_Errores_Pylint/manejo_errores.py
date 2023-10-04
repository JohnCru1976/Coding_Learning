'''
Módulo de aprendizaje para la depuración de errores y manejo de Pylint
Este archivo cumple todos los requisitos PEP-8, según Pylint
Sintaxis: pylint nombre_archivo.py -r y  (-r de reporte ... y de yes)
'''

def suma():
    '''Función que suma dos números'''
    numero1 = int(input("Introduce el número 1: "))
    numero2 = int(input("Introduce el número 2: "))  # ValueError si no introducimos un número
    print(numero1 + numero2)
    print("Gracias por sumar" + numero1) # TypeError al no ser n1 un string

### ESTRUCTURA TRY-EXCEPT-ELSE-FINALLY
try: # TRY (Código a evaluar)
    suma()
except TypeError: # EXCEPT (Código que se ejecuta SI HAY UN ERROR)
    print("La cadena no se puede concatenar con un integer")
except ValueError: # EXCEPT (Código que se ejecuta SI HAY UN ERROR)
    print("Se debe introducir un número entero")
else: # ELSE (Optativo - Código que se ejecuta SI NO HAY UN ERROR)
    print("Hiciste todo bien")
finally:# FINALLY (Optativo - Se ejecuta independientemente de si hay o no un error)
    print("El código de riesgo ha finalizado ... por fin")

## EJEMPLO DE USO PRÁCTICO ##
def pedir_numero(texto):
    '''Funcion para la gestión de entrada de números'''
    numero = 0
    while True:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Introduce un número")
        except NotImplementedError:
            pass
        else:
            return numero

print(pedir_numero("Introduce un número: "))
