'''
DECORADORES: son funciones que modifican el funcionamiento de otras funciones
Concepto previo: todo en Python son objetos, incluídas las funciones
'''

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

## APLICACIÓN de la característica de que todo son objetos
## CONCEPTO PREVIO 1: Se puede asignar una función a una variable
fun_mayuscula = mayuscula
## Otro ejemplo
imprimir = print
imprimir("Hola")
## CONCEPTO PREVIO 2: Una función se puede pasar como argumento de otra función
def una_funcion(funcion):
    return funcion
una_funcion(mayuscula("Probando"))
## CONCEPTO PREVIO 3: Se pueden definir funciones dentro de otras funciones
def cambiar_letras(tipo):
    def mayusc(texto):
        print(texto.upper())
    def minusc(texto):
        print(texto.lower())
    if tipo == "may":
        return mayusc
    elif tipo == "min":
        return minusc
operacion = cambiar_letras("may")
operacion("palabra")

## CONSTRUCCIÓN DEL DECORADOR
def decorar_saludo(funcion):
        def otra_funcion(palabra):
            print("Hola")
            funcion(palabra)
            print("Adios")
        return otra_funcion

@decorar_saludo
def mayusc(texto):
    print(texto.upper())

@decorar_saludo
def minusc(texto):
    print(texto.lower())

mayusc("Prueba_Decorador")

## Quiero conseguir elegir cuándo decorar la funcion
## Usaré como ejemplo minuscula(texto)
minuscula_decorada = decorar_saludo(minuscula)
## Ahora sí
minuscula_decorada("DECORANDO_Minuscula")
