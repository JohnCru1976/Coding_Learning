mi_lista = ["a", "b", "c"]
print(type(mi_lista))  # -> <class 'list'>

# Puede tener varios tipos de datos
# También pueden anidar otras listas
mi_lista_2 = ["a", 55, 23.3]

# Propiedades y métodos
print(len(mi_lista_2))  # -> 3
print(mi_lista[0:2])  # -> ['a', 'b']
print(mi_lista + mi_lista_2) # -> ['a', 'b', 'c', 'a', 55, 23.3]
mi_lista.append(34)
print(mi_lista)  # -> ['a', 'b', 'c', 34]
mi_lista.pop()
print(mi_lista)  # -> ['a', 'b', 'c']
saving_pop = mi_lista.pop(0)
print(mi_lista)  # -> ['b', 'c']
print(saving_pop)  # -> a
mi_lista_3 = ["n", "o", "a", "x", "l"]
mi_lista_3.sort()  # No devuelve nada. Modifica la lista
print(mi_lista_3)  # -> ['a', 'l', 'n', 'o', 'x']
mi_lista_3.reverse()  # No devuelve nada. Modifica la lista
print(mi_lista_3)  # -> ['x', 'o', 'n', 'l', 'a']

# Acceso a elementos
print(mi_lista[1])  # -> c
mi_lista[1] = 2  # Esto no se puede hacer con un string
print(mi_lista[1])  # -> 2



