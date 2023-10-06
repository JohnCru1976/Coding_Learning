from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

## ALGUNOS USOS DE COUNTER
lista = [3,3,3,3,4,4,4,4,4,4,2,2,2,2,5,5,5,5,5,7,7,7,7]
frase = "al pan pan y al vino vino"
serie_numeros = Counter(lista)

print(serie_numeros)  #-> Counter({4: 6, 5: 5, 3: 4, 2: 4, 7: 4})  (por orden de frecuencia)
print(serie_numeros.get(4)) #-> 6
print(serie_numeros.get(11)) #-> none
print(Counter(frase))  #-> Counter({'a': 9, 'b': 3, 'r': 3, ' ': 3, 'c': 2, 'd': 2, 'p': 1, 't': 1, 'e': 1})
print(Counter(frase.split(" ")))  #-> Counter({'al': 2, 'pan': 2, 'vino': 2, 'y': 1})
print(serie_numeros.most_common())  #-> [(4, 6), (5, 5), (3, 4), (2, 4), (7, 4)]  (por orden de frecuencia)
print(serie_numeros.most_common(2))  #-> [(4, 6), (5, 5)] (Los dos primeros más comunes)
print(list(serie_numeros))  #-> [3, 4, 2, 5, 7]  (elementos de la lista por orden de aparición)


# ALGUNOS USOS DE DEFAULTDICT
mi_dic = {"uno": "Verde", "dos": "Azul", "tres": "Rojo"}
# print(mi_dic["cuatro"])  #-> arroja error
mi_dic_prueba = defaultdict(lambda: "nada")
mi_dic_prueba["uno"] = "Verde"
mi_dic_prueba["dos"] = "Azul"
mi_dic_prueba["tres"] = "Rojo"

print(mi_dic_prueba)  #-> defaultdict(<function <lambda> at 0x000001963F454540>, {'uno': 'Verde', 'dos': 'Azul', 'tres': 'Rojo'})
print(mi_dic_prueba["dos"])  #-> "Azul"
print(mi_dic_prueba["cuatro"])  #-> "nada"

# ALGUNOS USOS DE NAMEDTUPLE (acceso a través de un nombre a elementos de una tupla)
Persona = namedtuple("Persona", ["nombre", "altura", "edad"]) #-> Genera una clase Persona con los atributos indicados
mi_persona = Persona("Juan", 1.63, 13)
print(mi_persona.altura)  #-> 1.63
print(mi_persona[1])  #-> 1.63

# ALGUNOS USOS DE DQUE ("double-ended queue" o "cola de doble extremo" en inglés)
my_deque = deque([1,3,4])

my_deque.append(1)  
 
my_deque.append(2)
my_deque.append(3)
print(my_deque)  #-> deque([1, 3, 4, 1, 2, 3])

my_deque.appendleft(0)
print(my_deque)  #-> deque([0, 1, 3, 4, 1, 2, 3])

my_deque.pop()  
print(my_deque)  #-> deque([0, 1, 3, 4, 1, 2])
my_deque.popleft()
print(my_deque)  #-> deque([1, 3, 4, 1, 2])

my_deque.extend(lista)
print(my_deque)  #-> deque([1, 3, 4, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 5, 5, 5, 5, 5, 7, 7, 7, 7])
