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
        opcion_categoria = menu_categorias(diccionario_recetario)
        if opcion_categoria != "q":
            opcion_receta = menu_recetas(opcion_categoria)
            if opcion_receta != "q":
                leer_receta(opcion_receta)
    # CREAR RECETA
    elif opcion_elegida == "2":
        pass
    # CREAR CATEGORÍA
    elif opcion_elegida == "3":
        pass
    # ELIMINAR RECETA
    elif opcion_elegida == "4":
        pass
    # ELIMINAR CATEGORÍA
    elif opcion_elegida == "5":
        pass
    