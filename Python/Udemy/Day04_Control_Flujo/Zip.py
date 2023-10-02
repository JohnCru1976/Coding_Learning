# Función incorporada que se utiliza para combinar 
# elementos de dos o más iterables en una secuencia de tuplas.
# Se asume la longitud de la lista más corta

nombres = ["Jose", "Vicente", "Hugo", "Javier"]
edades = [12, 20, 11, 23, 35]
ciudades = ["España", "Argentina", "Brasil"]

print(zip(nombres, edades, ciudades))  #-> <zip object at 0x0000020F3E281F80>
lista_final = list(zip(nombres, edades, ciudades))

print(lista_final)  #-> [('Jose', 12, 'España'), ('Vicente', 20, 'Argentina'), ('Hugo', 11, 'Brasil')]

for nombre, edad, ciudad in lista_final:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")