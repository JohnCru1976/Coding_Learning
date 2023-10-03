class Padre:
    def hablar(self):
        print("Padre dice hola")

class Madre:
    def hablar(self):
        print("Madre dice hola")
    def reir(self):
        print("Madre se ríe, ja, ja")

class Hijo(Madre, Padre):  # EJEMPLO DE HERENCIA MÚLTIPLE
    ## LOS MÉTODOS HEREDADOS DE MADRE TIENEN PREFERENCIA POR ESTAR EN PRIMER LUGAR (Madre, Padre)
    pass

class Nieto(Hijo): 
    pass

nieto = Nieto()

### MUY INTERESANTE ###
### Método especial __mro__ (Method Order Resolution)
print(Nieto.__mro__)
# Devuelve: (<class '__main__.Nieto'>, <class '__main__.Hijo'>, <class '__main__.Madre'>, <class '__main__.Padre'>, <class 'object'>)

nieto.reir()
nieto.hablar()