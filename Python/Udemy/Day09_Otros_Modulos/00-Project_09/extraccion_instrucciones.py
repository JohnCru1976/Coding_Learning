''' 
Este archivo es un juego planteado por el instructor
para practicar la descompresión de archivos
'''

import shutil
import os

# Establece como directorio de trabajo el directorio actual
os.chdir(os.path.dirname(os.path.abspath(__file__)))

shutil.unpack_archive("Proyecto+Dia+9.zip","Instrucciones_proyecto")
