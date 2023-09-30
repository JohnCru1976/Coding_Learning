# SINTAXIS COMPRENSIÓN DE LISTAS
# [ expresión_para_cada_elemento for elemento in iterable ]

# Forma rudimentaria de crear una lista a partir de un string literal
palabra = "Python"
lista1 = []
for l in palabra:
    lista1.append(l)
print(lista1)

# Mediante comprension de listas
lista2 = [letra.upper() for letra in palabra]
print(lista2)

# Ejemplo con IF-ELSE
lista3 = [n ** 2 if n % 2 == 0 else "no par" for n in range(5,60,5)]
print(lista3)

# Transformar medidas
pies = [10, 23, 45, 67, 89]
metros = [str(round(medida * 0.3048, 2)) + " - " + str(medida) for medida in pies]
print(metros)

# Otros ejemplos proporcionados por Chat GPT y Bard
pares = [x for x in range(11) if x % 2 == 0]
print(pares)
cuadrados = [numero ** 2 for numero in range(1, 6)]
print(cuadrados)

# Crear una lista de los cuadrados de los números del 1 al 10
cuadrados = [x ** 2 for x in range(1, 11)]

# Crear una lista de las cadenas con su primera letra en mayúscula
cadenas = [c.capitalize() for c in ["hola", "mundo"]]

# Crear una lista de las palabras que comienzan por la letra "a"
palabras = ["amor", "paz", "amistad"]
palabras_con_a = [palabra for palabra in palabras if palabra[0] == "a"]
