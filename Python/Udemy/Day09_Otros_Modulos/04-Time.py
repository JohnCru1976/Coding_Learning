import time
import timeit

# TIME uso para hacer marcas de tiempo
# Ejemplo de aplicación para medir comparación de la duración de dos procesos
# En procesos muy breves TIME no tiene mucha precisión

def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(300000)
fin = time.time()
print(f"Cálculo prueba_for con módulo TIME: {fin - inicio}")

inicio = time.time()
prueba_while(300000)
fin = time.time()
print(f"Cálculo prueba_while con módulo TIME: {fin - inicio}")

## TIMEIT ... medición más precisa
# Para este ejemplo se crearan las variables string que serán parseadas al método

declaracion = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number = 100000)
print(f"Cálculo prueba_for con módulo TIMEIT: {duracion}")


declaracion = '''
prueba_while(10)
'''
mi_setup = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number = 1000000)
print(f"Cálculo prueba_while con módulo TIMEIT: {duracion}")