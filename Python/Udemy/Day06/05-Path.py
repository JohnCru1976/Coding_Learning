from pathlib import Path

# Construir rutas relativas o absolutas
relativo = Path("./", "Barcelona", "Sagrada_Familia.txt")
print(relativo)
absoluto = Path(Path.home(), "prueba", relativo)
print(absoluto)
absoluto = Path(Path.cwd(), "prueba", relativo)
print(absoluto)
print("*" * 20)

# Apuntar a otro archivo aprovechando un archivo path
nueva_ruta = absoluto.with_name("Otro_Archivo.txt")
print(nueva_ruta)
print("*" * 20)

# Subir al directorio parent
ruta_parent = nueva_ruta.parent
print(ruta_parent)
ruta_parent = ruta_parent.parent
print(ruta_parent)
ruta_parent = ruta_parent.parent.parent.parent.parent.parent.parent.parent
print(ruta_parent)
print("*" * 20)

# Conseguir una lista de archivos en un directorio
ruta_working_directory = Path(Path.cwd())
lista_archivos = Path(ruta_working_directory).glob("*")
for ruta_archivo in lista_archivos:
    print(ruta_archivo)
print("*" * 20)
# Imprimir solo el nombre de los archivos txt
lista_archivos = Path(ruta_working_directory).glob("*.txt")
for ruta_archivo in lista_archivos:
    print(ruta_archivo.name)
print("*" * 20)
# Incluir carpetas y subcarpetas que se encuentren dentro
lista_archivos = Path(ruta_working_directory.parent).glob("**/*.py")
for ruta_archivo in lista_archivos:
    print(ruta_archivo.name)
print("*" * 20)

