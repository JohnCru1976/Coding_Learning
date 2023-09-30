# INMUTABILIDAD
texto = "Carina"
# texto[0] = "K" -> Lanza un error
# 'str' object does not support item assignment
print(texto.replace("C", "K"))
print(texto)

# CONCATENABLE
print(texto*3)
print(texto + texto)

# MULTILINEA
poema = """Mil pequeños peces blancos
como si hirviera 
el color del agua"""
print(poema)

# COMPROBAR SI HAY CONTENIDO
print("peces" in poema)  # -> True
print("mojón" in poema)  # -> False
print("mojón" not in poema)  # -> True

# LONGITUD
print(len(poema))
print(len(texto))
