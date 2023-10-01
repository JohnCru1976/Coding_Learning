from functions import *

while fin_aplicacion == False:
    opcion_elegida = menu_inicial()
    if opcion_elegida == "q":
        os.system("cls")
        print("***************************************")
        print("Gracias por utilizar GESTIÓN DE RECETAS")
        print("\t¡¡¡Hasta la próxima!!!")
        print("***************************************")
        fin_aplicacion = True
    # LEER RECETA
    elif opcion_elegida == "1":
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
        opcion_categoria = menu_categorias(diccionario_recetario,"Categorías")
        if opcion_categoria != "q":
            opcion_receta = menu_recetas(opcion_categoria, diccionario_recetario,"Elección de receta")
            if opcion_receta != "q":
                leer_receta(opcion_receta)
    # CREAR RECETA
    elif opcion_elegida == "2":
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
        opcion_categoria = menu_categorias(diccionario_recetario, "Categoría para creación de receta")
        if opcion_categoria != "q":
            crear_receta(opcion_categoria)
            diccionario_recetario = actualiza_recetario(PATH_RECETAS)
    # CREAR CATEGORÍA
    elif opcion_elegida == "3":
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
        crear_categoria()
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
    # ELIMINAR RECETA
    elif opcion_elegida == "4":
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
        opcion_categoria = menu_categorias(diccionario_recetario, "Categoría para eliminación de receta")
        if opcion_categoria != "q":
            opcion_receta = menu_recetas(opcion_categoria, diccionario_recetario,"Elección de receta a eliminar")
            if opcion_receta != "q":
                eliminar_receta(opcion_receta)
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
    # ELIMINAR CATEGORÍA
    elif opcion_elegida == "5":
        diccionario_recetario = actualiza_recetario(PATH_RECETAS)
        opcion_categoria = menu_categorias(diccionario_recetario, "Elegir categoría a eliminar")
        if opcion_categoria != "q":
            eliminar_categoria(opcion_categoria)