from pathlib import Path, PureWindowsPath
import os

carpeta = Path(os.getcwd()) / "Prueba.txt"

# El método read es diferente en el objeto Path
# NO es necesario OPEN ni CLOSE
print(type(carpeta))  #-> <class 'pathlib.WindowsPath'>
# READ_TEXT() Imprime contenido del archivo
print("*" * 20)
print(carpeta.read_text())
# NAME (Atributo) Devuelve el nombre del archivo
print("*" * 20)
print(carpeta.name)
# SUFFIX (Atributo) Devuelve el sufijo del archivo
print("*" * 20)
print(carpeta.suffix)
# STEM (Atributo) Nombre del archivo sin sufijo
print("*" * 20)
print(carpeta.stem)
# EXISTS() Comprobar si el archivo existe
print("*" * 20)
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Existe el archivo")
# PUREWINDOWSPATH - Transforma a ruta de archivo en windows
print("*" * 20)
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
