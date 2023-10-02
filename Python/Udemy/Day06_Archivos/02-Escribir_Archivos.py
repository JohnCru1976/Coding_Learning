# Método write con parametro "w" (Sobrescribe el archivo)
archivo = open("prueba1.txt", "w")
archivo.write("Soy el nuevo texto\n")
archivo.write("""Hola
mundo
aquí estoy""")
archivo.close()

# Método writelines (escribe todo seguido)
archivo = open("prueba2.txt", "w")
archivo.writelines(["Hola Mundo!!\n", "Esto es una prueba"])
archivo.close()

# Forma de transferir elementos de una lista a un archivo
archivo = open("prueba3.txt", "w")
lista = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
for elemento in lista:
    archivo.write(f"{elemento}\n")
archivo.close()

# Parametro "a" -- lleva el cursor hasta el final del texto
archivo = open("prueba3.txt", "a")
lista = ["Seis", "Siete", "Ocho", "Nueve", "Diez"]
for elemento in lista:
    archivo.write(f"{elemento}\n")
archivo.close()
