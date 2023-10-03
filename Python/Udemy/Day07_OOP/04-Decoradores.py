## METODOS DE INSTANCIA
## METODOS DE CLASE   @classmethod
## METODOS ESTÁTICOS @staticmethod

class Prueba:
    atributo_clase = "Soy un atributo de clase"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
        self._atributo_instancia_oculto = "Soy un atributo de instancia oculto"
    # MÉTODO DE INSTANCIA
    def metodo_instancia(self, parametro_prueba): 
        print("Soy un método de instancia\n\tPuedo acceder a los atributos de instancia y de clase")
        print("\t",self.atributo_clase, sep="")
        print("\t",self.atributo_instancia, sep="")
        print("\t",self._atributo_instancia_oculto, sep="")
        print("\t",parametro_prueba, sep="")
    # MÉTODO DE CLASE
    @classmethod    ## NO PUEDEN ACCEDER A LOS ATRIBUTOS DE LA INSTANCIA
    def metodo_clase(cls, parametro_prueba):
        print("Soy un método de clase\n\tNo puedo acceder a los atributos de instancia")
        print("\t",cls.atributo_clase, sep="")
        print("\t",parametro_prueba, sep="")
    # MÉTODO ESTÁTICO
    @staticmethod   ## NO PUEDEN ACCEDER A LOS ATRIBUTOS DE LA INSTANCIA NI DE LA CLASE
    def metodo_estatico(parametro_prueba):
        print("Soy un método estatico\n\tNo puedo acceder a los atributos de instancia ni de clase")
        print("\t",parametro_prueba, sep="")

Prueba.metodo_clase("Éste es el parámetro de prueba en el método de clase")
Prueba.metodo_estatico("Éste es el parámetro de prueba en el método estático")

instancia_objeto_prueba = Prueba("Soy un atributo de instancia")
instancia_objeto_prueba.metodo_instancia("Éste es el parámetro de prueba en el método de instancia")
instancia_objeto_prueba.metodo_clase("Éste parametro de prueba se ha pasado desde la instancia")
instancia_objeto_prueba.metodo_estatico("Éste parametro de prueba se ha pasado desde la instancia")
