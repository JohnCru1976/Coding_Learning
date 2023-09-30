
mi_archivo = open('../Prueba.txt',encoding='cp1252', errors='surrogateescape')

print(mi_archivo) #-> <_io.TextIOWrapper name='../Prueba.txt' mode='r' encoding='cp1252'>

contenido = mi_archivo.read()

print(contenido)
