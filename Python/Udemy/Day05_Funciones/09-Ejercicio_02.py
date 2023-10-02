# ***********************************************
# EJERCICIO 2 - Fecha: 28-09-2023
# Autor: Juan B. Cru Murillo
# ***********************************************

def ordena_letras(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra.lower())
    lista = list(set(lista))
    lista.sort()
    return lista

print(ordena_letras("Abracadabra"))

# ***********************************************
# EJERCICIO 2 - SOLUCIÓN DEL INSTRUCTOR
# ***********************************************
def letras_unicas(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(letras_unicas("entretenido"))