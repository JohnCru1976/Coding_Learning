'''Acoplamiento (Coupling): La medida de la dependencia entre dos o más clases. 
Un bajo acoplamiento es deseable para evitar que los cambios en una clase 
afecten demasiado a otras clases.'''

# https://escueladirecta-blog.blogspot.com/2021/10/acoplamiento-pilares-de-la-programacion.html

'''Se trata de un pilar vinculado con la cohesión, ya que por lo general un acoplamiento débil
 se asocia a una cohesión fuerte. Esta última es la situación buscada al escribir código.'''

### NO ME HA QUEDADO ESPECIALMENTE CLARO, AUNQUE LO COMPRENDO ###

#### EJEMPLO CON ACOPLAMIENTO ####
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

#### EJEMPLO CON ACOPLAMIENTO REDUCIDO ####

class Libro1:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca1:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

