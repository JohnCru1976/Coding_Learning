'''Herencia (Inheritance): La capacidad de una clase para heredar atributos 
y métodos de otra clase base. Esto permite la creación de jerarquías 
de clases y la reutilización de código.'''

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")
class Pajaro(Animal):
    pass

## __BASES__ (propiedad) indica la clase parent 
## Devuelve una tupla, por tanto falta por ver si se puede 
## heredar de varias clases
print(Pajaro.__bases__)  #->(<class '__main__.Animal'>,)

## __SUBCLASSES__ (método) indica las clases que están heredando
print(Animal.__subclasses__()) #->[<class '__main__.Pajaro'>]

piolin = Pajaro(23,"Rojo")

piolin.nacer()
print(f"Es de color {piolin.color}")