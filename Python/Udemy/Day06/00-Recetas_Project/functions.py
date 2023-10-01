from pathlib import Path
import os

PATH_RECETAS = Path(__file__).parent / "Recetas"
# pylint: disable=invalid-name
fin_aplicacion = False
diccionario_recetario = {}

def actualiza_recetario(root_path):
    '''Devuelve un diccionario con todos los path del recetario'''
    # Crea un diccionario vacío para almacenar las categorías y rutas de recetas.
    diccionario = {}    
    # Obtiene una lista de elementos en el directorio especificado por root_path.
    elementos_directorio = root_path.iterdir()    
    # Crea una lista de categorías, que son subdirectorios en root_path.
    lista_categorias = [categoria for categoria in elementos_directorio if categoria.is_dir()]    
    # Itera a través de las categorías.
    for ruta_categoria in lista_categorias:
        # Busca todos los archivos con extensión .txt en la categoría actual.
        recetas = list(Path(ruta_categoria).glob("*.txt"))        
        # Agrega la categoría y la lista de rutas de recetas al diccionario.
        diccionario[ruta_categoria] = recetas    
    # Devuelve el diccionario resultante que contiene las categorías y rutas de recetas.
    return diccionario

def menu_inicial():
    '''Muestra el menu inicial y devuelve el caracter del menú seleccionado'''
    caracter_introducido = "-"
    caracteres_posibles = "12345q"

    while not caracter_introducido in caracteres_posibles:
        os.system("cls")
        print("BIENVENIDO A GESTIÓN DE RECETAS")
        print(f"Las recetas se encuentran en {PATH_RECETAS}")
        print(f"Recetas totales: {contar_recetas(PATH_RECETAS)}\n")
        print("[1] Leer una receta")
        print("[2] Crear una nueva receta")
        print("[3] Crear una nueva categoría")
        print("[4] Eliminar una receta")
        print("[5] Eliminar una categoría")
        print("[Q] Salir de la aplicación")
        caracter_introducido = input("\nSelecciona una opción: ").lower()
        if not caracter_introducido:
            caracter_introducido ="-"
    
    return caracter_introducido

def menu_categorias(diccionario, texto):
    '''Muestra las categorías y devuelve el path de la categoría seleccionada'''
    caracter_introducido = "-"
    caracteres_posibles = "q"
    categorias_diccionario = diccionario.keys()

    if not categorias_diccionario:
        os.system("cls")
        print("GESTIÓN DE RECETAS\n")
        print("NO SE HA CREADO NINGUNA CATEGORÍA\n")
        input("Pulsa Enter para volver al menú principal")
        return "q"

    while not caracter_introducido in caracteres_posibles:
        contador = 1
        os.system("cls")
        print("GESTIÓN DE RECETAS\n")
        print(f"{texto}:")

        for categoria in categorias_diccionario:
            print(f"[{contador}] {categoria.name}")
            caracteres_posibles += str(contador)
            contador += 1
        print("[Q] Volver al menú principal")

        caracter_introducido = input("\nSelecciona una categoría: ").lower()
        if not caracter_introducido:
            caracter_introducido ="-"
    
    if caracter_introducido == "q":
        return "q"
    else:
        return Path(list(categorias_diccionario)[int(caracter_introducido) - 1])

def menu_recetas(path_categoria, diccionario, texto):
    '''Muestra recetas y devuelve del path de la receta seleccionada'''

    caracter_introducido = "-"
    caracteres_posibles = "q"
    recetas_categoria = diccionario[path_categoria]

    if not recetas_categoria:
        os.system("cls")
        print("GESTIÓN DE RECETAS\n")
        print(f"NO HAY RECETAS EN LA CATEGORÍA {path_categoria.name.upper()}\n")
        input("Pulsa Enter para volver al menú principal")
        return "q"


    while caracter_introducido not in caracteres_posibles:
        contador = 1
        os.system("cls")
        print("GESTIÓN DE RECETAS\n")
        print(f"RECETAS EN LA CATEGORÍA {path_categoria.name.upper()}:")
        print(f"{texto.upper()}:")

        for receta in recetas_categoria:            
            print(f"[{contador}] {Path(receta).stem}")
            caracteres_posibles += str(contador)
            contador += 1
        print("[Q] Volver al menú principal")

        caracter_introducido = input("\nSelecciona una receta: ").lower()
        if not caracter_introducido:
            caracter_introducido ="-"
    
    if caracter_introducido == "q":
        return "q"
    else:
        return Path(list(recetas_categoria)[int(caracter_introducido) - 1])

def leer_receta(path_receta):
    '''Muestra el contenido de una receta a partir de su path'''
    os.system("cls")
    print("GESTIÓN DE RECETAS\n")
    print(f"LECTURA RECETA {path_receta.stem.upper()}:\n")

    print(Path(path_receta).read_text())

    input("\nPulsa Enter para continuar...")

def crear_receta(path_categoria):
    '''Crea una receta en la carpeta de la categoría seleccionada'''
    nombre_receta = ""
    texto_receta = ""
    continuar = False
    ruta = ""

    os.system("cls")
    print("GESTIÓN DE RECETAS\n")
    print(f"CREACIÓN DE RECETA EN LA CATEGORÍA {path_categoria.name.upper()}:\n")

    while not continuar or not nombre_receta:
        nombre_receta = input("Introduce el nombre de la nueva receta: ")
        if not nombre_receta:
            continue
        if existe_receta(path_categoria, nombre_receta):
            print("La receta ya existe, debes introducir un nuevo nombre")
            continue
        
        try:
            ruta = Path(path_categoria) / (nombre_receta + ".txt")
            ruta.write_text("")
        except IOError as error:
            print("Error: Ha sido imposible crear el archivo con ese nombre")
            continue
        else:
            continuar = True
    
    # Introduccion de texto
    texto_receta = ""
    print("\nIngresa el texto de la receta. Pulsa Enter tras cada línea, hasta finalizar:\n")
    while True:
        linea = input()
        if not linea:
            break  # Salir del bucle si se presiona Enter (cadena vacía)
        texto_receta += linea + "\n"
    ruta.write_text(texto_receta)
    print("Texto guardado con éxito, pulsa Enter para continuar...")
    input()

def crear_categoria():
    '''Crea una carpeta para la nueva categoría '''
    nombre_categoria = ""
    continuar = False
    ruta = ""

    os.system("cls")
    print("GESTIÓN DE RECETAS\n")
    print("CREACIÓN DE UNA NUEVA CATEGORÍA\n")

    while not continuar or not nombre_categoria:
        nombre_categoria = input("Introduce el nombre de la nueva categoria: ")
        if not nombre_categoria:
            continue
        if existe_categoria(nombre_categoria):
            print("La categoría ya existe, debes introducir un nuevo nombre")
            continue
        
        try:
            ruta = Path(PATH_RECETAS) / nombre_categoria
            ruta.mkdir()
        except IOError as error:
            print("Error: Ha sido imposible crear la categoría con ese nombre")
            continue
        else:
            continuar = True

    print("\nCategoría guardada con éxito, pulsa Enter para continuar...")
    input()

def eliminar_receta(path_receta):
    '''Elimina una receta dado su path'''          
    try:
        ruta = Path(path_receta)
        ruta.unlink()
    except IOError as error:
        print("Error: Ha sido imposible eliminar el archivo")
        print(error)
    else:
        print("Receta eliminada con éxito, pulsa Enter para continuar...")
        input()

def eliminar_categoria(path_categoria):
    '''Elimina una categoria dado su path'''
    if path_categoria.exists() and path_categoria.is_dir():     
        # Comprobar si el directorio está vacío
        archivos = len(list(Path(path_categoria).glob("*")))
        #print(archivos)
        if archivos > 0:
            print(f"Hay {archivos} recetas dentro de la categoría, debes eleminarlas antes de eliminar la categoría")
            print("Pulsa Enter para continuar...")
            input()
            return ""
               
        try:
            ruta = Path(path_categoria)
            ruta.rmdir()
        except IOError as error:
            print("Error: Ha sido imposible eliminar la categoría")
            print(error)
        else:
            print("Categoría eliminada con éxito, pulsa Enter para continuar...")
            input()
    else:
        print("Algo no ha ido bien, pulsa Enter para continuar...")
        input()

def existe_receta(path_categoria,nombre_receta):
    '''Devuelve True si la receta ya existe en el path_categoria'''
    nombre_archivo = nombre_receta + ".txt"
    ruta_total = Path(path_categoria) / nombre_archivo
    return Path(ruta_total).exists()

def existe_categoria(nombre_categoria):
    '''Devuelve True si la receta ya existe en el path_categoria'''
    ruta_total = PATH_RECETAS / nombre_categoria
    return Path(ruta_total).exists()

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador