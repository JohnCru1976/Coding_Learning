def suma(*args):
    print(args)  # Esto es un tuple
    total = 0
    for num in args:
        total += num
    return total

print(suma(3,4,5,6,7,8))
print(suma(3,4,5,6,7,8,10,12,3,234,34))

# OTRO EJEMPLO

def numeros_persona(*args):
    suma_numeros = sum(args[1:])
    nombre = ""
    if args:
        nombre = str(args[0])
        return f"{nombre}, la suma de tus números es {suma_numeros}"
    return "No hay argumentos suficientes"
    
print(numeros_persona("Juan", 1, 2, 4, 67))