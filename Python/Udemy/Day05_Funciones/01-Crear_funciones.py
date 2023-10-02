def saludar_persona(nombre):
    # This function greets people
    print(f"Hola {nombre}")

nombre = "Juan"

saludar_persona(nombre)

# RETURN
def sumar(num1, num2):
    # This function sums two numbers
    total = num1 + num2
    return total

resultado = sumar(4,2)
print(resultado)

# NOTA: si en la función anterior introduzco 2 strings lanzará un error
# Más adelante en el curso se aprenderá a controlar este tipo de cuestiones
def invertir_palabra(word):
    return word[::-1].upper()
    
print(invertir_palabra("Hoal"))