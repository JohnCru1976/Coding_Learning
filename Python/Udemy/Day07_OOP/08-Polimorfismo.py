''' CHAT-GPT
El POLIMORFISMO (Polymorphism): en la programación orientada a objetos (POO) de Python 
se refiere a la capacidad de objetos de diferentes clases de responder 
de manera diferente a un mismo método o función. En otras palabras, 
varios objetos pueden compartir un nombre de método o función, pero su 
comportamiento puede variar según la clase a la que pertenezcan. 
Esto permite escribir código más genérico y flexible, ya que se pueden tratar 
objetos de diferentes clases de manera uniforme si cumplen con una interfaz común.
El polimorfismo se logra mediante el uso de herencia y la implementación de métodos
con el mismo nombre en clases diferentes, pero con implementaciones específicas 
para cada clase. Cuando se llama a un método en un objeto, Python determina en 
tiempo de ejecución cuál versión del método debe ejecutarse en función del tipo del objeto.
'''

class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(f"\t{self.nombre} dice muuu")

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(f"\t{self.nombre} dice beee")

animal1 = Vaca("Nube")
animal2 = Oveja("Jamona")

vaca = Vaca("Josefa")
oveja = Oveja("Vicenta")

def animal_hablar(animal):
    #### OJO, A ESTE MÉTODO:  ISINSTANCE ..... IMPORTANTÍSIMO ####
    if isinstance(animal, Oveja):
        print(f"Clase: {type(animal).__name__}")  ## OJO AQUÍ TAMBIÉN type(instancia).__name__ (DEVUELVE EL NOMBRE DE LA CLASE)
    else:
        print(f"Clase: {type(animal).__name__}")
    animal.hablar()

animal_hablar(animal1)
animal_hablar(animal2)
animal_hablar(vaca)
animal_hablar(oveja)