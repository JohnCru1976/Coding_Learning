# PRIMERA EXPLICACIÓN CONCEPTUAL
def type_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

type_kwargs(a=1, b=2, c=3)
#type_kwargs({'a':1, 'b':2, 'c':3})  # TypeError: type_kwargs() takes 0 positional arguments but 1 was given

# EJEMPLO
def suma(**kwargs):
    result = 0
    for clave, valor in kwargs.items():
        print(clave, valor, sep=" = ")
        result += valor
    return result

print(suma(a=1, b=2, c=3))

# EJEMPLO CON MEZCLA DE ARGUMENTOS
def prueba(num1, num2, *args, **kwargs):  # Tiene que ser en este orden
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    
    for clave, valor in kwargs.items():
        print(clave, valor, sep=" = ")

prueba("Hola", {2: 23, 4: 34}, 3, 4, 5, 6, 7, 8, 23, a="1", b=2.34, c=3)

lista = [3, 4, 5, 6, 7, 8, 23]
key_value = {"a":"1", "b":2.34, "c":3}
prueba("Hola", {2: 23, 4: 34}, *lista, **key_value) # OJO, se pasa el valor con los asteriscos