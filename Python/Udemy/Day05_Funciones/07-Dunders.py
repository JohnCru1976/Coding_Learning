# MEJORES EXPLICACIÓN ENCONTRADA PARA LOS DUNDERS (MÉTODOS MÁGICOS)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __ne__(self, otra_persona):
        return self.nombre != otra_persona.nombre or self.edad != otra_persona.edad

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

    def __le__(self, otra_persona):
        return self.edad <= otra_persona.edad

    def __gt__(self, otra_persona):
        return self.edad > otra_persona.edad

    def __ge__(self, otra_persona):
        return self.edad >= otra_persona.edad

persona1 = Persona("Juan", 20)
persona2 = Persona("María", 25)

print(persona1 == persona2)
print(persona1 != persona2)
print(persona1 < persona2)
print(persona1 <= persona2)
print(persona1 > persona2)
print(persona1 >= persona2)


# OTRO EJEMPLO PARA LAS ITERACIONES

class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __iter__(self):
        return iter(self.elementos)

lista = Lista([1, 2, 3])

for elemento in lista:
    print(elemento)
