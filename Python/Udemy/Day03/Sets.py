# En un set los elementos no se repiten
# Los elementos NO están ordenados en ÍNDICES INTERNOS
# NO se pueden incluir LISTAS ni DICCIONARIOS
# SÍ se pueden incluir TUPLES
# Son INMUTABLES

# DOS FORMAS DE DECLARACIÓN
set1 = set([1, 2, 3, 4, 5])
set1 = set({1, 2, 3, 4, 5})
set1 = set((1, 2, 3, 4, 5))
set2 = {1, 2, 3, 4, 5}

print(type(set1))  #-> <class 'set'>
print(set1) #-> {1, 2, 3, 4, 5}

# Se eliminan las repeticiones que se incluyan al declarar el set
# Parece que también se ordena (confirmar)
set_repeticiones = {1, 7, 2, 5, 1, 4, 7, 3, 2, 4, 5}
print(set_repeticiones)  #-> {1, 2, 3, 4, 5, 7}

# Métodos
print(len(set_repeticiones))  #-> 6
print(2 in set_repeticiones)  #-> True
# Unir sets
s1 = {4, 5, 3}
s2 = {3, 1, 2}
s3 = s1.union(s2)
print(s3)  #-> {1, 2, 3, 4, 5}
# Agregar
s1.add(2)
print(s1)  #-> {2, 3, 4, 5}
# Eliminar
s1.remove(3)  # Da error si intento eliminar un elemento no existente
print(s1)  #-> {2, 4, 5}
s1.discard(234)  # No da error al descartar elementos no existentes
print(s1)  #-> {2, 4, 5}
# Pop - Elimina un elemento al azar
s1.pop()
print(s1)  #-> {4, 5}
# Clear - Vacía nuestro set
s1.clear()
print(s1)  #-> set()
