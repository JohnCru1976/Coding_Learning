from pathlib import Path
import os

PATH_RECETAS = Path(__file__).parent / "Recetas"
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
        print("BIENVENIDO A GESTIÓN DE RECETAS\n")
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

def menu_categorias(diccionario):
    '''Muestra las categorías y devuelve el path de la categoría seleccionada'''
    caracter_introducido = "-"
    caracteres_posibles = "q"
    categorias_diccionario = diccionario.keys()

    while not caracter_introducido in caracteres_posibles:
        contador = 1
        os.system("cls")
        print("GESTIÓN DE RECETAS\n")
        print("CATEGORÍAS:")

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

def menu_recetas(path_categoria):
    '''Muestra recetas y devuelve del path de la receta seleccionada'''
    diccionario_recetario = actualiza_recetario(PATH_RECETAS)

    caracter_introducido = "-"
    caracteres_posibles = "q"
    recetas_categoria = diccionario_recetario[path_categoria]

    while not caracter_introducido in caracteres_posibles:
        contador = 1
        os.system("cls")
        print("GESTIÓN DE RECETAS\n")
        print(f"RECETAS EN LA CATEGORÍA {path_categoria.name.upper()}:")

        for receta in recetas_categoria:
            print(f"[{contador}] {receta.name}")
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
    print(f"LECTURA RECETA {path_receta.name.upper()}:\n")

    print(Path(path_receta).read_text())

    input("\nPulsa una tecla para continuar...")

def crear_receta(path_categoria):
    '''Crea una receta en la carpeta de la categoría seleccionada'''


    # Introduccion de texto
    entrada_multilinea = ""
    print("Ingresa texto. Para finalizar presiona Enter tras la última linea:")
    while True:        
        linea = input()
        if not linea:
            break  # Salir del bucle si se presiona Enter (cadena vacía)
        entrada_multilinea += linea + "\n"
    print("Texto guardado con éxito, pulsa una tecla...")
    input()

def crear_categoria():
    '''Crea una carpeta para la nueva categoría '''
    pass

def eliminar_receta(path_receta):
    '''Elimina una receta dado su path'''
    pass

def eliminar_categoria(path_receta):
    '''Elimina una categoria dado su path'''
    pass
