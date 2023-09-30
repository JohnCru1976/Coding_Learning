# Son inmutables
# Pueden tener elementos diferentes
mi_tuple1 = (1, 2, 3, 4, 5, 6)  # Se puede escribir también sin paréntesis
print(type(mi_tuple1))  #-> <class 'tuple'>
print(mi_tuple1[2])  #-> 3
print(mi_tuple1[-4])  #-> 3

# Tuples anidados
mi_tuple2 = (1, 2, 3, 4, [100, 200, 300], 1, 3, 4, 4)
print(mi_tuple2[4][1])  #-> 200

# Casting a lista
mi_tuple1 = list(mi_tuple1)
print(mi_tuple1)  #-> [1, 2, 3, 4, 5, 6]
print(type(mi_tuple1))  #-> <class 'list'>
mi_tuple1 = tuple(mi_tuple1)
print(mi_tuple1)  #-> (1, 2, 3, 4, 5, 6)
print(type(mi_tuple1))  #-> <class 'tuple'>

# PROCEDIMIENTO DE ASIGNACIÓN MÚLTIPLE
# Funciona también con listas y diccionarios
t = (1, 2, 3, 4)
a, b, c, d = t
print(a, b, c, d) #-> 1 2 3 4

d = {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4}
a, b, c, e = d
print(a, b, c, e) #-> v1 v2 v3 v4

# OTROS MÉTODOS
mi_tuple2 = (1, 2, 3, 4, [100, 200, 300], 1, 3, 4, 4)
print(mi_tuple2.count(4)) # El elemento 4 aparece 4 veces
print(mi_tuple2.index(2)) # El número de índice donde aparece
