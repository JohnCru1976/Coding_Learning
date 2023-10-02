precios_cafe = [('Capuchino', 1.5), ('Expresso', 1.2), ('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
    precio_caro = 0
    cafe_caro = ""

    for cafe, precio in precios_cafe:
        if precio > precio_caro:
            precio_caro = precio
            cafe_caro = cafe

    return(cafe_caro, precio_caro)


for cafe, precio in precios_cafe:
    print(cafe, precio)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es {cafe} que cuesta {precio}")

