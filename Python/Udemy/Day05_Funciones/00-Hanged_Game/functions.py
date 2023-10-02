import os
import unicodedata
from random import randint

limite_fallos = 7
rondas = 10

def draw_hanged(num_errors):
    ''' This function returns a hanged in string format
        according the number of errors passes as parameter
        The limit is 6 errors'''
    hanged = " ----:\n"
    if num_errors <= 0:
        hanged += " | \n" + " | \n" + " | \n"              
    elif num_errors == 1:
        hanged += " |   O \n" + " | \n" + " | \n"
    elif num_errors == 2:
        hanged += " |   O\n" + " |   |  \n" + " |\n"
    elif num_errors == 3:
        hanged += " |   O\n" + " | - |\n" + " |\n"
    elif num_errors == 4:
        hanged += " |   O\n" + " | - | -\n" + " |\n"
    elif num_errors == 5:
        hanged += " |   O\n" + " | - | -\n" + " |  |\n"
    else:
        hanged += " |   O\n" + " | - | -\n" + " |  | |\n"
    hanged += "[-]"
    return hanged

def quitar_acentos_palabra(palabra):
    # Usa la función normalize para eliminar acentos y diacríticos
    palabra_sin_acentos = ""
    for letra in palabra:        
        palabra_sin_acentos += unicodedata.normalize('NFKD', letra).encode('ASCII', 'ignore').decode('ASCII')
    return palabra_sin_acentos

def random_word(lista_palabras):
    ''' Esta función devuelve una palabra al azar dada una colección
        de palabras'''
    num_azar = randint(0,len(lista_palabras)-1)
    return str(lista_palabras[num_azar])

def representacion_palabra(palabra_azar, letras_acertadas):
    ''' Devuelve String con la representación de las letras acertadas según la palabra'''
    palabra = ""
    posicion = 0
    for letra in quitar_acentos_palabra(palabra_azar.lower()):
        if letra in letras_acertadas:
            palabra += " " + palabra_azar[posicion]
        else:
            palabra += " _"
        posicion += 1
    return palabra.upper()

def comprobacion(letra, palabra_azar, letras_acertadas, letras_falladas):
    ''' Esta funcion comprueba si la letra está en la palabra y devuelve una lista con 3 elementos
        Primero: -1 si la letra ya fue utilizada, 0 si se ha acertado, 1 si se ha fallado
        Segundo: Actualización lista de letras acertadas
        Tercero: Actualización lista de letras falladas
        Cuarto: String con la representación de las letras acertadas según la palabra'''
    result = []
    # Comprobar si la letra está incluída en las letras ya acertadas o falladas
    lista_aciertos_fallos = letras_acertadas + letras_falladas
    if letra in lista_aciertos_fallos:
        result.append(-1)
        result.append(letras_acertadas)
        result.append(letras_falladas)
        result.append(representacion_palabra(palabra_azar, letras_acertadas))        
    # Comprobar si la letra está en la palabra
    elif letra in quitar_acentos_palabra(palabra_azar):
        result.append(1)
        letras_acertadas.append(letra)
        result.append(letras_acertadas)
        result.append(letras_falladas)
        result.append(representacion_palabra(palabra_azar, letras_acertadas))        
    else:
        result.append(0)
        result.append(letras_acertadas)
        letras_falladas.append(letra)
        result.append(letras_falladas)
        result.append(representacion_palabra(palabra_azar, letras_acertadas))        
    return result

def presentacion(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, ronda):
    
    '''Esta funcion hace la primera presentación tras cada intento'''
    fallos = len(letras_falladas)
    str_letras_falladas = str(len(letras_falladas)) + " fallos"
    str_letras_acertadas = representacion_palabra(palabra_azar, letras_acertadas)

    os.system("cls")
    
    print("****JUEGO DEL AHORCADO****")
    print(f"** {limite_fallos} FALLOS DE LÍMITE **\n")
    if ronda > rondas:
        print("RONDA: " + str(rondas) + " de " + str(rondas))
    else:
        print("RONDA: " + str(ronda) + " de " + str(rondas))
    print("PARTIDAS GANADAS: " + str(partidas_ganadas))

    if ronda != rondas + 1:
        print("\n" + draw_hanged(fallos) + "\n")
        print("Aciertos: " + str_letras_acertadas  + "\n")

        if fallos > 0 and fallos <= limite_fallos:
            str_letras_falladas += ": "
            for letra in letras_falladas:
                str_letras_falladas += str(letra).upper() + " "
        print(str_letras_falladas + "\n")

def palabra_completada(palabra_azar, letras_acertadas):
    '''Devuelve True si la palabra ha sido completada'''
    lista = []
    # Convertir string a lista
    for letra in str(palabra_azar).lower():
        lista.append(letra)
    # Quitar elementos repetidos
    lista = list(set(lista))
    # Comprobar palabra
    return len(lista) == len(list(letras_acertadas))

def introducir_letra(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, ronda):
    '''Esta funcion gestiona la introduccion de nuevas letras
        Cuando llega al límite de fallos ya no se ejecuta
        Devuelve True cuando acaba el juego'''
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".lower()
    letra = "-"
    lista_comprobacion = []

    presentacion(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, ronda)

    if len(letras_falladas) >= limite_fallos: 
        presentacion(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, ronda)       
        return [True, lista_comprobacion]

    while letra == "" or letra[0] not in abecedario:
        letra = quitar_acentos_palabra(input("INTRODUCE UNA LETRA: ").lower())
        if letra != "":
            lista_comprobacion = comprobacion(letra, palabra_azar.lower(), letras_acertadas, letras_falladas)
            # Comprobar si la letra ya se ha introducido
            if lista_comprobacion[0] == -1:
                print("La letra ya ha sido introducida")
                letra = "-"
    
    
    if palabra_completada(palabra_azar.lower(), letras_acertadas):
        presentacion(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, ronda) 
        return [True, lista_comprobacion]
    else:
        presentacion(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, ronda) 
        return [False, lista_comprobacion]
