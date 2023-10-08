import zipfile
import shutil
import os

directorio_file = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorio_file)

# Creación del archivo zip
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
# Incluyendo documentos al zip
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")
# Cierre del archivo
mi_zip.close()
# Abrir archivo que hemos creado y extraer sus archivos
zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
zip_abierto.extractall()
zip_abierto.close()


## OPERACIONES CON SHUTIL
carpeta_origen = directorio_file + "\\carpeta_pruebas"
archivo_destino = "carpeta_pruebas"
## Comprimir
shutil.make_archive(archivo_destino,"zip",carpeta_origen)
## Descomprimir
shutil.unpack_archive("carpeta_pruebas.zip","Extraccion_acabada")
