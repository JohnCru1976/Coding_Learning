import os
from pathlib import Path

# ****************************************
# El objeto Path del módulo pathlib lo utilizamos
# para poder trabajar con directorios de diferentes
# sistemas operativos
# Se añadió hace pocas versiones
# ****************************************

carpeta = Path("C:/Users/juanb/OneDrive/VariosJuan/Programacion/GitHubPortatil/Coding_Learning/Coding_Learning/Python/Udemy/Day05")
print(carpeta) # Ruta transformada a OS Windows
carpeta = Path(os.getcwd())
# Aquí se va a subir un directorio y elegir otro archivo
archivo = carpeta / ".." / "Day05" / "05-Args.py"
print(archivo)  # Ruta del archivo

mi_archivo = open(archivo)
print(mi_archivo.read(151))
mi_archivo.close()
print(archivo)

# ****************************************
# Métodos de interés para manejo de rutas
# con el módulo OS
# Directorio de trabajo
# ****************************************
ruta = os.getcwd()
print(ruta)
# Cambio de directorio de trabajo
# ruta = os.chdir("nuevo_path") 

# Crear un nuevo directorio si no existe previamente
if not os.path.isdir(ruta + "\\Prueba"):
    os.makedirs(ruta + "\\Prueba")  
input("""A continuación se va a eliminar el directorio prueba
Pulsa una tecla para continuar""")
# Eliminar directorio
os.rmdir(ruta + "\\Prueba")

# Separar nombre del archivo de la ruta
ruta = os.getcwd() + "\\Prueba.txt" # Esta es la ruta completa
                                    # con el archivo
# Basename devuelve el nombre del archivo
elemento = os.path.basename(ruta)
print(elemento)  #-> Prueba.txt
# Dirname devuelve el nombre del path
elemento = os.path.dirname(ruta)
print(elemento)  #-> Devuelve el path en esta máquina
# Ambos elementos en un tupla
tupla_path_ruta = os.path.split(ruta)
print("\n".join(tupla_path_ruta))
