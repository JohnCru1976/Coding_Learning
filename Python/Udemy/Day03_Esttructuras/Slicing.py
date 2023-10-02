texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)  # -> CDE
fragmento = texto[:5]
print(fragmento)  # -> ABCDE
fragmento = texto[2:40:2]  # ¡¡¡ No hay overflow !!!
print(fragmento)  # -> CEGIKM
fragmento = texto[::2]
print(fragmento)  # -> ACEGIKM
fragmento = texto[::-1]  # Cadena al revés
print(fragmento)  # -> MLKJIHGFEDCBA