lista = ["a", "b", "c"]

# Forma básica de indizar los elementos de la lista
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

# Con enumerate (crea una lista de tuples tipo (indice, elemento))
for indice, item in enumerate(lista):
    print(indice, item)