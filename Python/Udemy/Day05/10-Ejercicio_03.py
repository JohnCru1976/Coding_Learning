# ***********************************************
# EJERCICIO 3 - Fecha: 28-09-2023
# Autor: Juan B. Cru Murillo
# ***********************************************
def doble_cero(*args):
    cero = False
    for arg in args:
        if int(arg) == 0 and cero == False:
            cero = True
        elif int(arg) == 0 and cero == True:
            return True
        elif int(arg) != 0 and cero == True:
            cero = False
    return False

print(doble_cero(3,4,5,6,3,0,2,1,0,2))

# ***********************************************
# EJERCICIO 3 - SOLUCIÓN DEL INSTRUCTOR
# ***********************************************
def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else: 
            contador += 1
    return False

print(doble_cero(3,4,5,6,3,0,0,1,0,2))