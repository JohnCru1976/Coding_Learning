mi_texto = "Esto es una prueba"

# Localizar el elemento de un índice
resultado = mi_texto[0]
print(resultado)  # -> E
resultado = mi_texto[9]
print(resultado)  # -> n
resultado = mi_texto[-4]  # Reverse index
print(resultado)  # -> u

# Localizar un índice a partir de un elemento
# Si el elemento no existe el compilador lanza error
resultado = mi_texto.index("e")  # Devuelve la primera letra empezando por izq
print(resultado)  # -> 5
resultado = mi_texto.rindex("e")  # Devuelve la primera letra empezando por der
print(resultado)  # -> 15
resultado = mi_texto.index("prueba")  # Case sensitive
print(resultado)  # -> 12
