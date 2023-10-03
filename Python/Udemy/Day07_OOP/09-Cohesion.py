'''Cohesión (Cohesion): El grado en el que los métodos de una clase están relacionados 
y trabajan juntos para realizar una tarea específica. Una alta cohesión es
 deseable para mantener el código organizado.'''

# https://escueladirecta-blog.blogspot.com/2021/09/cohesion-pilares-de-la-programacion.html

'''El principio de cohesión en la programación orientada a objetos (POO) 
se refiere a la medida en que las funciones o métodos de una clase están 
relacionados y trabajan juntos para realizar una tarea específica. En otras palabras, 
una clase cohesiva tiene métodos que están estrechamente relacionados en función y propósito.

Un alto grado de cohesión es deseable porque hace que las clases sean más 
fáciles de entender, mantener y reutilizar. Las clases con baja cohesión tienden
a ser confusas y difíciles de trabajar, ya que contienen métodos
que realizan tareas diversas y no relacionadas.

Aquí tienes un ejemplo simple en Python para ilustrar el principio de cohesión:'''

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return a / b


''' En este ejemplo, la clase `Calculadora` tiene métodos cohesivos que 
realizan operaciones matemáticas relacionadas (suma, resta, multiplicación y división). 
Cada método tiene un propósito claro y está diseñado para realizar una tarea específica.

La cohesión ayuda a mantener el código organizado y facilita la comprensión de cómo 
se relacionan las diferentes partes de una clase. Es importante en la POO diseñar 
clases que sigan este principio para crear un código más mantenible y legible.'''