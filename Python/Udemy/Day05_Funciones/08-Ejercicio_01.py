# ***********************************************
# EJERCICIO 1 - Fecha: 28-09-2023
# Autor: Juan B. Cru Murillo
# ***********************************************
def devolver_distintos(int1, int2, int3):
    '''Devuelve valores en relación a un parámetro dado'''
    lista = [int1, int2, int3]
    lista.sort()
    if sum(lista) > 15:
        return lista[2]
    elif sum(lista) < 10:
        return lista[0]
    else:
        return lista[1]


print(devolver_distintos(4, 5, 1))

# ***********************************************
# EJERCICIO 1 - SOLUCIÓN DEL INSTRUCTOR
# ***********************************************


def devolver_distintos_2(a, b, c):
    '''Devuelve valores en relación a un parámetro dado'''
    suma = a + b + c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos_2(20, 5, 7))
