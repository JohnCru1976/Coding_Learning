'''
FUNCIÓN GENERADORA: Va entregando los valores generados poco a poco para no colapsar los recursos
En lugar de utilizar RETURN se utiliza la keyword YIELD
'''

def funcion_normal():
    lista = []
    for numero in range(1,5):
        lista.append(numero * 10)
    return lista

def funcion_generadora():
    for numero in range(1,5):
        yield numero * 10

print(funcion_normal())
print(funcion_generadora())  # Clase generador

# Forma 1
generador = funcion_generadora()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
# print(next(generador))  #-> Esto lanza error porque no hay más elementos que iterar
# Forma 2
print(next(funcion_generadora()))
# Forma 3
print(funcion_generadora().__next__())


#### OTRO EJEMPLO ####
# Es posible utilizar la keyword YIELD en varias ocasiones sin interrumpir el código de la función
def generador2():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = generador2()
print(next(g), next(g), next(g))

## CONCLUSIÓN PROPIA - EJEMPLO PROPIO
## Generador infinito
def generador3():
    x = 1
    while True:
        yield x
        x += 1

g3 = generador3()
for i in range(1,10):
    print(next(g3))


