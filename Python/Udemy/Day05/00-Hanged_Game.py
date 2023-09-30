# ESTA ES LA SOLUCIÓN DEL INSTRUCTOR

# IMPORTAR LIBRERÍAS
from random import choice

# DECLARACIÓN DE VARIABLES
palabras = ["panadero", "dinosaurio", "helipuerto", "tiburon"]
letras_correctas = []        # Lista para almacenar letras correctas adivinadas
letras_incorrectas = []      # Lista para almacenar letras incorrectas adivinadas
intentos = 6                 # Número de intentos disponibles
aciertos = 0                 # Número de letras correctas adivinadas
juego_terminado = False      # Indicador de si el juego ha terminado

# DECLARACIÓN DE FUNCIONES
# Función para elegir una palabra al azar de la lista
def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas_interna = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas_interna

# Función para pedir al usuario una letra y validarla
def pedir_letra():
    letra_elegida = ""
    es_valida = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")
    
    return letra_elegida

# Función para mostrar el tablero con las letras adivinadas
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for letra_interna in palabra_elegida:
        if letra_interna in letras_correctas:
            lista_oculta.append(letra_interna)
        else:
            lista_oculta.append("-")
    print(' '.join(lista_oculta))

# Función para verificar si la letra elegida es correcta o incorrecta
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra diferente")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

# Función que se ejecuta cuando el jugador pierde
def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)
    return True

# Función que se ejecuta cuando el jugador gana
def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("¡¡¡¡Enhorabuena, has encontrado la palabra!!!!")
    return True

# AQUÍ EMPIEZA EL PROGRAMA
palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letra incorrectas: " + '-'.join(letras_incorrectas))
    print("Vidas restantes: " + str(intentos))
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado