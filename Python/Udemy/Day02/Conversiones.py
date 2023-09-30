# Ejemplo de conversión implícita
num1 = 20
num2 = 30.5

num1 = num1 + num2  # Aquí la conversión

print(type(num1))  # -> <class 'float'>
print(type(num2))  # -> <class 'float'>

# Ejemplos de conversión explícita
num1 = 5.8
print(num1)  # -> 5.8
print(type(num1))  # -> <class 'float'>

num2 = int(num1)  # Aquí el casting o conversión
print(num2)  # -> 5
print(type(num2))  # -> <class 'int'>

edad = input("Dime tu edad: ")
edad = int(edad)  # Conversión explícita
nueva_edad = edad + 1
print("Tu nueva edad va a ser: " + str(nueva_edad))
print(f"Tu nueva edad va a ser: {nueva_edad}")
