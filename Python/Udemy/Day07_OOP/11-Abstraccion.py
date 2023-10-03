'''Abstracción (Abstraction): La capacidad de representar objetos del 
mundo real en un programa de manera simplificada, 
enfocándose en los aspectos relevantes y ocultando los detalles innecesarios.'''

# https://escueladirecta-blog.blogspot.com/2021/10/abstraccion-pilares-de-la-programacion.html

'''La abstracción es el pilar de la programación orientada a objetos que se relaciona 
con ocultar toda la complejidad que algo puede tener por dentro, ofreciendo una interfaz 
con funciones de alto nivel, por lo general sencillas de usar, que pueden ser usadas para
interactuar con la aplicación sin tener conocimiento de lo que hay dentro.'''

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Crear instancias de objetos
mi_perro = Perro("Max", "Canino")
mi_gato = Gato("Whiskers", "Felino")

# Utilizar el método de la abstracción
print(f"{mi_perro.nombre} es un {mi_perro.especie} y hace el sonido: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} es un {mi_gato.especie} y hace el sonido: {mi_gato.hacer_sonido()}")
