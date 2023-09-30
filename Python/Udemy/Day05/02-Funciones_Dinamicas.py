def chequear_3_cifras(num):
    # Return True or False if then number is in the range or not
    return num in range(100,1000)

print(chequear_3_cifras(34))
print(chequear_3_cifras(456))

# Chequear los elementos de una lista
def chequear_3_cifras_list(list_num):
    # Devuelve la lista de elementos de tres cifras
    lista = []
    for num in list_num:
        if num in range(100,1000):
            lista.append(num)
        else:
            pass
    return lista
    

print(chequear_3_cifras_list([232,122,23,434,23]))
print(chequear_3_cifras_list([23,12,23,44,23]))


def cantidad_pares(lista):
    lista_pares = [n for n in lista if n % 2 == 0]
    return len(lista_pares)
lista_numeros=[1,2,3,4,5,6]
print(cantidad_pares(lista_numeros))