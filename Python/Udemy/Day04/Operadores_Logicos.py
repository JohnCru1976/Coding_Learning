# AND
my_bool = 1 < 5 and 5 > 10  # -> False

print("Table AND")
print(False and False)  # -> False
print(False and True)  # -> False
print(True and False)  # -> False
print(True and True)  # -> True

# OR
my_bool = 1 < 5 or 5 > 10  # -> True

print("Table OR")
print(False or False)  # -> False
print(False or True)  # -> True
print(True or False)  # -> True
print(True or True)  # -> True

# NOT
my_bool = 1 < 5 and not (5 > 10)  # -> True

print("Table NOT")
print(not False)  # -> True
print(not True)  # -> False

# Ejemplo de búsqueda de palabras en una frase
print("Ejemplo de búsqueda de palabras")
frase = "Esta frase es un ejemplo"
my_bool = ("Coche" in frase) and ("frase" in frase)
print(my_bool)
