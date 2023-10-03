'''Encapsulamiento (Encapsulation): El concepto de ocultar los detalles
internos de una clase y proporcionar una interfaz pública para interactuar 
con ella. Se logra utilizando atributos privados y métodos de acceso públicos.'''

# https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html

'''El encapsulamiento es el pilar de la programación orientada a objetos 
que se relaciona con ocultar al exterior determinados estados internos de un objeto, 
tal que sea el mismo objeto quien acceda o los modifique, pero que dicha acción no 
se pueda llevar a cabo desde el exterior, llamando a los métodos o atributos directamente.

Si bien en algunos lenguajes (como Java), puede resultar un procedimiento habitual, 
Python no lo implementa por defecto, pero nos propone una vía alternativa para lograrlo. 
Esto se hace anteponiendo dos guiones bajos (__) al nombrar un método o atributo. 
De esa manera, los mismos quedarán definidos como “privados”, y únicamente 
el mismo objeto podrá acceder a ellos.'''

class Persona:
    atributo_publico = "Mostrar"   # Accesible desde el exterior
    __atributo_privado = "Oculto"  # No accesible
    # No accesible desde el exterior
    def __metodo_oculto(self):
        print("Este método está oculto")
        self.__variable = 0
    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__metodo_oculto()
alumno = Persona()
# alumno.__metodo_oculto()  # Este método no es accesible desde el exterior
alumno.metodo_normal()      # Este método es accesible

# print(alumno.__atributo_privado) # Atributo no acccesible


'''Existe un pequeño truco (no recomendado) para acceder a los atributos y métodos ocultos. 
Dichos métodos están presentes con un nombre algo distinto:

instancia + _ + NombreClase + método/atributo oculto'''

alumno._Persona__metodo_oculto()
alumno._Persona__atributo_privado = "Me paso por los huevos que esté oculto"
print(alumno._Persona__atributo_privado)

''' CHAT-GPT
En Python, no existen modificadores de acceso como "private" o "public" como en otros lenguajes de programación. 
En su lugar, Python utiliza una convención para indicar la visibilidad de los atributos y métodos:

Atributos y métodos que comienzan con un guion bajo (_) se consideran como "PROTECTED". 
Esto indica que no deben ser accedidos desde fuera de la clase, pero no hay una restricción fuerte que lo impida. 
Los programadores pueden acceder a ellos si lo desean, aunque se considera una práctica no recomendada.

Atributos y métodos que comienzan con dos guiones bajos (__) se consideran como "PRIVATE". 
Python realiza una especie de "name mangling" (cambio de nombre) para hacer que estos atributos y 
métodos sean menos accesibles desde fuera de la clase. Aunque aún es posible acceder a ellos, 
se vuelve más incómodo y menos probable que se haga por accidente.

Atributos y métodos sin guion bajo o con un guion bajo al final son considerados "public". 
Estos son accesibles desde cualquier lugar.

Sin embargo, es importante destacar que esta convención es principalmente una recomendación 
y no una restricción fuerte. Los programadores en Python pueden acceder a 
atributos y métodos "protected" y "private" si lo desean. Python confía en la 
responsabilidad del programador para respetar estas convenciones.

Entonces, aunque el encapsulamiento en Python no es tan estricto como en algunos 
otros lenguajes de POO, aún se pueden aplicar los principios de ocultar detalles 
internos y proporcionar una interfaz pública para interactuar con objetos mediante 
el uso de estas convenciones de nomenclatura y la responsabilidad del programador.
'''