import os
from pathlib import Path


# Establece como directorio de trabajo el directorio del archivo
def change_working_directory():
    file_diretory = os.path.dirname(__file__)
    os.chdir(file_diretory)
# Recorrer todos los archivos y subcarpetas
def lista_path_files(path):
    rutas = os.walk(path)
    lista_path = []
    for carpeta, subcarpeta, archivos in rutas:
        if archivos:
            for archivo in archivos:
                ruta = Path(carpeta, archivo)
                lista_path.append(ruta)
    return lista_path
# Comparar texto de un listado de archivos
def lista_coincidencias():
    pass
