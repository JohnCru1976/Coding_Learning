## TIPOS ATRIBUTO: DE CLASE Y DE INSTANCIA
class Pajaro:
    # ATRIBUTO DE CLASE (ACCESIBLE SIN DECLARAR OBJETO)
    plumas = True
    # ATRIBUTOS DEL OBJETO
    # Método constructor, el atributo self es obligatorio
    # Self es la propia instancia
    def __init__(self, color, especie):
        self.color = color  # ATRIBUTO DE OBJETO
        self.especie = especie    # ATRIBUTO DE OBJETO

## DECLARANDO OBJETI
mi_pajaro = Pajaro("rojo", "gorrion")

print(mi_pajaro.color, mi_pajaro.especie, sep=" - ")  #-> rojo - gorrion
print(Pajaro.plumas)

Pajaro.alas
