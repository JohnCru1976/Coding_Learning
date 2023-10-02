class Pajaro:

    alas = True

    def __init__(self, nombre, color, especie):
        self.nombre = nombre
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio!!, mi color es {self.color.lower()}")

    def volar(self, metros):
        print(f"{self.nombre} ha volado {metros} metros")

piolin = Pajaro("Piolín", "Amarillo", "Canario")
piolin.piar()
piolin.volar(23)
