# PALABRAS CLAVE EN LOS BUCLES  FOR, WHILE
# BRAKE, CONTINUE, PASS

monedas = 5
while monedas > 0:
    print(f"Te quedan {monedas} monedas")
    monedas -= 1
else: 
    print("No te queda un chavo, Vicent")

# Bucle de decisión del usuario
respuesta = "s"
while respuesta == "s":
    respuesta = input("¿Quieres continuar? (s/n)")
else:
    print("Es una pena que dejes este bucle")

# PASS es una construcción en Python que no hace nada, 
# pero es útil para mantener la sintaxis correcta en situaciones 
# donde necesitas un bloque de código vacío como marcador de posición.
for i in range(5):
    pass  # Este bucle no realiza ninguna acción aún

while respuesta == "s":
    pass  # Este bucle no realiza ninguna acción aún

# BRAKE - Interrumpe la iteración dentro del bucle
monedas = 5
monedas = 5
while monedas > 0:
    print(f"Te quedan {monedas} monedas")
    if monedas == 2:
        print("Mejor reserva estas 2 monedas")
        break # Sale del bucle cuando monedas es igual a 2
    monedas -= 1

# CONTINUE - omitir la ejecución de las iteraciones restantes
#  en el bucle actual y pasar a la siguiente iteración
#  sin salir completamente del bucle
numeros = -1

while numeros <= 20:
    numeros += 1
    if numeros % 2 != 0:
        continue
    print(numeros)
    numeros