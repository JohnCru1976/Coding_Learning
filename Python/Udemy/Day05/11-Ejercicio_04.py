# ***********************************************
# EJERCICIO 4 - Fecha: 28-09-2023
# Autor: Juan B. Cru Murillo
# ***********************************************
def contar_primos(num):
    '''Count prime numbers til the argument given'''
    lista_primos = []
    for n_primo in range(2, num+1):
        if n_primo > 1 and num > 1:
            primo = True
            for i in range(2, n_primo):
                if n_primo % i == 0:
                    primo = False
            if primo:
                lista_primos.append(n_primo)
    print(lista_primos)
    return "En total hay " + str(len(lista_primos)) + " números primos"

print(contar_primos(7))

# ***********************************************
# EJERCICIO 4 - SOLUCIÓN DEL INSTRUCTOR
# ***********************************************
def contar_primos_2(numero):
    primos = [2]
    iteracion = 3

    if numero < 2: 
        return 0
    
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:  ## (1)
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)  

print(contar_primos_2(7))

''' ## (1) En Python, la palabra clave "else" 
se puede usar en un bucle "for" en combinación 
con un "break" para ejecutar un bloque de código
 cuando el bucle se completa normalmente, es decir, 
 cuando no se encuentra ninguna instrucción "break". 
 Esto es útil cuando deseas realizar alguna acción 
 después de que el bucle haya terminado sin interrupciones'''

# ELSE EN UN BUCLE FOR
for i in range(5):
    if i == 3:
        break  # Para aquí si se cumple la condición
    print(i) # Imprime si no se cumple la condición
else: # Hace esto al final del bucle si no actúa break
    print("El bucle for se ha completado normalmente.")

print("Fin del programa")