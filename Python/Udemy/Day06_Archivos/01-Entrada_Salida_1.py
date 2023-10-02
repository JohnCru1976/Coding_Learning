# Método read
print("** Método read **")
mi_archivo = open('Prueba.txt')
print(mi_archivo) #-> <_io.TextIOWrapper name='../Prueba.txt' mode='r' encoding='cp1252'>
archivo_completo = mi_archivo.read()
print(archivo_completo)
mi_archivo.close()

# Método readline
print("** Método readline **")
mi_archivo = open('Prueba.txt')
linea_1 = mi_archivo.readline()
print(linea_1)
linea_2 = mi_archivo.readline()
print(linea_2.rstrip())  # Se quita el salto de línea
linea_3 = mi_archivo.readline()
print(linea_3.upper())
mi_archivo.close()

# Iteración dentro de un archivo
print("** Iteración dentro de un archivo **")
mi_archivo = open('Prueba.txt')
for linea in mi_archivo:
    print(linea)
mi_archivo.close()

# Método readlines
print("** Método readlines **")
mi_archivo = open('Prueba.txt')
lineas = mi_archivo.readlines()  # Es una lista
print(lineas)
for linea in lineas:
    print(linea.rstrip())
mi_archivo.close()