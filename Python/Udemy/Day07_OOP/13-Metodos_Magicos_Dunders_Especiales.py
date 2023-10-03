'''Estos métodos permiten que las clases definidas por el usuario se comporten 
de manera especial en ciertas situaciones y se integren con características del 
lenguaje de Python.'''

### Desde mi punto de vista los dunders son la reacción a EVENTOS que se pueden incluir en las clases ###

## ESTO ES UNA PRUEBA PERSONAL ##
class Prueba_dunder:
    def __add__(self, objeto):
        if isinstance(objeto, Prueba_dunder):
            return "Has sumado dos objetos de la misma clase ... eres un crack"
        else:
            return "Los objetos no son de la misma clase"

objeto1 = Prueba_dunder()
objeto2 = Prueba_dunder()

suma = objeto1 + 1
print(suma)  #-> 'Los objetos no son de la misma clase'
suma = objeto1 + objeto2
print(suma)  #-> 'Has sumado dos objetos de la misma clase ... eres un crack'

## MÁS EJEMPLOS
# EJERCICIO 1 : crear un tipo de datos que reaccione a la función len()

class CompactDisc:
    '''We still don't know what the class are going to do'''
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        self.__listado = [autor, titulo, canciones]
    
    def __str__(self):
        return f"[{self.autor}, {self.titulo}, {self.canciones}]"
    def __iter__(self):
        return iter(self.__listado)
    def __len__(self):
        return len(self.__listado)
    def __del__(self):
        print("Se ha eliminado el objeto")
    
mi_objeto = CompactDisc("Julio Iglesias", "Hey", 12)

## Uso del dunder __str__
print(mi_objeto)  #-> [Julio Iglesias, Hey, 12]
## Uso del dunder __iter__
for elemento in mi_objeto:
    print(elemento)  
## Uso del dunder __len__
print(len(mi_objeto))   #-> 3
## DEL Elimina la instancia del objeto
## El dunder __del__ se utiliza a estos efectos
del mi_objeto   #-> Se ha eliminado el objeto
    