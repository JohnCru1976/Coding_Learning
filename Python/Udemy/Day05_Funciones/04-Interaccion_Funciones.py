# ****************************************************************
# JUEGO PALITOS: intento de código propio antes de ver la lección
# ****************************************************************
from random import shuffle
from random import randint
from random import choice
# Se crea una lista inicial
palitos = ["corto", "largo", "largo", "largo"]

# Función que devuelve una mezcla de los palitos
def mezcla_palitos(lista): # Pase por referencia   
    shuffle(lista)
    return lista

def es_palito_corto(num, lista):
    if lista[num-1] == "corto":
        return True
    return False

num_palito = int(input("Elige un palito entre cuatro (1-4): "))
mezcla = mezcla_palitos(palitos)
print(palitos)

if es_palito_corto(num_palito, mezcla):
    for id, palito in list(enumerate(mezcla)):
        print(id + 1, palito, sep=" - ")
    print("Lo siento te ha tocado el palito corto")
else:
    for id, palito in list(enumerate(mezcla)):
        print(id + 1, palito, sep=" - ")
    print("Te has salvado, no te ha tocado el palito corto")

# ****************************************************************
# JUEGO PALITOS: solución en el curso
# ****************************************************************

# Lista inicial
palitos = ["-", "--", "---", "----"]
# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista
# Pedirle intento
def probar_suerte():
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número del uno al cuatro: ")
    return int(intento)
# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento - 1]}")
# Main del programa
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)


# ***************************************
# OTRO EJERCICIO
# ***************************************
def lanzar_dados():
    return [randint(1,6), randint(1,6)]
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados in range(7, 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# Main del programa
jugada1, jugada2 = lanzar_dados()
print(evaluar_jugada(jugada1, jugada2))


# ***************************************
# OTRO EJERCICIO
# ***************************************
lista_numeros = [23, 34, 12, 123, 42, 23, 2, 12]
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop()
    return lista
def promedio(lista):
    contador = 0
    suma = 0
    if lista:
        for num in lista:
            suma += num
            contador += 1
        return suma / contador
    else:
        return 0
        
print(promedio(reducir_lista(lista_numeros)))


# ***************************************
# OTRO EJERCICIO
# ***************************************
lista_numeros = [12, 2, 3, 45, 2, 67, 3, 123]

def lanzar_moneda():
    moneda = ("Cara","Cruz")
    return choice(moneda)
def probar_suerte(lanzamiento, lista):
    if lanzamiento == "Cara":
        print("La lista se autodestruirá")
        lista.clear()
        return lista
    else:
        print("La lista fue salvada")
        return lista

print(probar_suerte(lanzar_moneda(),lista_numeros))