text = "Este es el texto de Federico"
# UPPER
resultado = text.upper()
print(resultado)
resultado = text[2].upper()
print(resultado)
# LOWER
resultado = text.lower()
print(resultado)
resultado = text[0].lower()
print(resultado)
# SPLIT
resultado = text.split()
print(resultado)
resultado = text.split("t")  # Indica el separador como parametro
print(resultado)
# JOIN
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a, b, c, d])
print(e)
# FIND (es como el método index)
# La diferencia con index es que devuelve -1 si no encuentra
# el resultado en lugar de lanzar error
resultado = text.find("texto")
print(resultado)  # -> 11
resultado = text.find("asdsxx")
print(resultado)  # -> -1
# REPLACE
resultado = text.replace("texto", "cojón")
print(resultado)
resultado = text.replace("e", "x")
print(resultado)
text = "Este Este".replace("Este", "Oeste")
print(text)
