'''Módulo con los métodos dedicados al control de los turnos'''


def generador_turnos(seccion):
    '''Generador que aumenta 1 unidad en cada llamada y devuelve un string'''
    contador = 0
    while True:
        contador += 1
        yield seccion + " - " + str(contador)

# Se crea un generador para cada categoría Farmacia, Cosmética y Perfumería
generador_farmacia = generador_turnos("F")
generador_cosmetica = generador_turnos("C")
generador_perfume = generador_turnos("P")


def decorador_turno(funcion):
    '''Decorador que añade más texto al texto devuelto por el generador'''
    texto = "Su turno es : "
    texto += funcion
    texto += "\nAguarde y será atendido"
    return texto


def siguiente_farmacia():
    '''Devuelve el texto completo decorado del siguiente turno de farmacia'''
    return decorador_turno(next(generador_farmacia))


def siguiente_cosmetica():
    '''Devuelve el texto completo decorado del siguiente turno de cosmetica'''
    return decorador_turno(next(generador_cosmetica))


def siguiente_perfume():
    '''Devuelve el texto completo decorado del siguiente turno de perfume'''
    return decorador_turno(next(generador_perfume))
