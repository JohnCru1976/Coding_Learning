bool1 = True
bool2 = False
print(type(bool1))  #-> <class 'bool'>

# Ejemplos booleanos indirectos
print(5 > 2 + 4)  #-> False
print(5 < 2 + 4)  #-> True
print(5 >= 4 + 1) #-> True
print(5 <= 4 + 4) #-> True
print(5 == 6)  #-> False
print(5 != 6)  #-> True

lista = [1, 2, 3, 4]
print(5 in lista)  #-> False
print(5 not in lista)  #-> True

# Valores vacíos - todos dan False
print(bool(""))
print(bool(0))
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(()))
