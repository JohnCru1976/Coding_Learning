import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")
    ##### CÓDIGO MUY INTERESANTE ####
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)  #### <<<<--- Muy bueno
        except ValueError:
            print("Esa no es una opción válida")
        else:  #### Se ejecuta cuando el código no lanza error
            break

    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
