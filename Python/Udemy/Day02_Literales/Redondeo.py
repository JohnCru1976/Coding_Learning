x = 90 / 7

# Valor sin redondear
print(x)  # -> 12.857142857142858
# Valor redondeado sin decimales
# Si el valor es float y el argumento
redondeo_sin_decimal = round(x)
print(redondeo_sin_decimal)   # -> 13
print(type(redondeo_sin_decimal)) # -> <class 'int'>
# Valor redondeado con dos decimales
redondeo_con_decimales = round(x, 1)
print(redondeo_con_decimales)  # -> 12.9
print(type(redondeo_con_decimales))  # -> <class 'float'>
redondeo_con_decimales = round(x, 2)
print(redondeo_con_decimales)  # -> 12.86
print(type(redondeo_con_decimales))  # -> <class 'float'>
redondeo_con_decimales = round(x, 3)
print(redondeo_con_decimales)  # -> 12.857
print(type(redondeo_con_decimales))  # -> <class 'float'>
