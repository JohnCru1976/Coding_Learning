class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")
    def hablar(self):
        print("Este animal emite un sonido")

## ¿QUÉ MÉTODOS PUEDEN TENER LAS SUBCLASES
# MÉTODOS HEREDADOS
# MÉTODOS HEREDADOS MODIFICADOS
# MÉTODOS PROPIOS
## ¿Qué sucede si una subclase hereda de dos clases con métodos con el mismo nombre?
# En primer lugar ejecuta el método propio si lo ha sobrescrito (override)

class Pajaro(Animal):
    ## HAY DOS MANERAS DE AGREGAR ATRIBUTOS A UNA SUBCLASE
    def __init__(self, edad, color, altura_vuelo):   # Altura_vuelo es el nuevo atributo
        # Esto sustituye a la declaración tradicional self.edad = edad, self.color = color
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    # Método sobrescrito (override) de la clase animal
    # Este método tendrá preferencia sobre lo heredado
    def nacer(self):
        print("Este pájaro ha nacido")
    def volar(self, metros):
        print(f"Este pájaro ha volado {metros} metros")

piolin = Pajaro(3,"negro",5)
piolin.nacer()
piolin.volar(2)