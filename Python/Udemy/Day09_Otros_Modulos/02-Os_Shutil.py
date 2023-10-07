import os
import shutil

# Obtener la ruta donde se encuentra el archivo actual
ruta = os.path.abspath(__file__)
# Obtener el nombre del directorio actual
directorio_actual = os.path.dirname(ruta)
print(directorio_actual)
# Cambiar el directorio de trabajo
os.chdir(str(directorio_actual))

archivo = open("curso.txt", "w")
archivo.write("Texto prueba")
archivo.close()

# Obtener lista de archivos
print(os.listdir())

# Mover archivos
try:
    shutil.move("curso.txt", directorio_actual + "\\prueba")
except:
    pass

# os.walk(path) -> recorre directorios y subdirectorios
archivos = os.walk(directorio_actual)
for carpeta, subcarpeta, archivo in archivos:
    print("Carpeta:" + carpeta, "Sub:" + str(subcarpeta), "File:" + str(archivo), sep="-")