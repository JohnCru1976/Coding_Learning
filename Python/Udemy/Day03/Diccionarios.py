cliente = {
    "nombre": "Juan",
    "apellido": "Fuentes",
    "peso": 80,
    "talla": 1.69
}

print(type(cliente))  # -> <class 'dict'>

# Acceso a elementos del diccionario
consulta = cliente["apellido"]
print(consulta)  # -> "Fuentes"
consulta = cliente["peso"]
print(consulta)  # -> 80

# Modificar y añadir elementos
cliente["nombre"] = "Pepe"
print(cliente["nombre"])  # -> "Pepe"
cliente["id"] = 100
print(cliente)  # -> {'nombre': 'Pepe', 'apellido': 'Fuentes',
#                    'peso': 80, 'talla': 1.69, 'id': 100}

# Puede contener cualquier tipo de elementos
dic = {
    "c1": 55,
    "c2": [10, 20, 30],
    "c3": {
        "s1": 100,
        "s2": 200
    }
}
print(dic["c2"][1])  # -> 20
print(dic["c3"]["s2"])  # -> 200

# Pequeño ejercicio (imprimir la letra "e" en uppercase
dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic["c2"][1].upper())  # -> E

# Podemos utilizar otros tipo de valores para las key
dic = {1: 'a', 2: 'b', 3: 'c'}

# Otros métodos
print(dic.keys())  # -> dict_keys([1, 2, 3])
print(type(dic.keys()))  # -> <class 'dict_keys'>
print(dic.values())  # -> dict_values(['a', 'b', 'c'])
print(type(dic.values()))  # -> <class 'dict_values'>
print(dic.items())  # -> dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
print(type(dic.items()))  # -> <class 'dict_items'>
