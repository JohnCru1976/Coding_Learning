## TIPOS ATRIBUTO: DE CLASE Y DE INSTANCIA
class Pajaro:
    # ATRIBUTO DE CLASE (ACCESIBLE SIN DECLARAR OBJETO)
    plumas = True
    # ATRIBUTOS DEL OBJETO
    # Método constructor, el atributo self es obligatorio
    # Self es la propia instancia
    def __init__(self, color, especie):
        self.color = color  # ATRIBUTO DE OBJETO
        self.especie = especie    # ATRIBUTO DE OBJETO
        self._atributo_privado = "Prueba"
    # GETTER para el atributo privado

    def get_atributo_privado(self):
        '''Geter del atributo privado'''
        return self._atributo_privado

# INSTANCIANDO OBJETO
mi_pajaro = Pajaro("rojo", "gorrion")
# ACCESO A LOS ATRIBUTOS DE OBJETO
print(mi_pajaro.color, mi_pajaro.especie, sep=" - ")  # -> rojo - gorrion
# ACCESO DIRECTO AL ATRIBUTO DE CLASE
print(Pajaro.plumas)
## ¿¿SE PUEDE MODIFICAR UN ATRIBUTO DE CLASE DIRECTAMENTE?? ##
Pajaro.plumas = False  # SÍ, queda pendiente averiguar como proteger este atributo
print(Pajaro.plumas)
# Prueba con atributo privado (protegido)
print(Pajaro.get_atributo_privado(mi_pajaro))  # Forma 1
print(mi_pajaro.get_atributo_privado())  # Forma 2
# --> NO FUNCIONA -- Puedo acceder directamente al atributo "privado"
mi_pajaro._atributo_privado = "Hola"  #->> Pylint avisa de que es una atributo "protegido"
print(mi_pajaro.get_atributo_privado())

''' CHAT-GPT
En Python, los atributos de clase no tienen una protección real contra escritura 
en el sentido de que no hay un mecanismo integrado para hacer que un atributo de 
clase sea completamente inmutable o privado. Python sigue el principio de 
"consentimiento del adulto" (EAFP: "Easier to Ask for Forgiveness than Permission") 
en lugar de "pedir permiso" (LBYL: "Look Before You Leap"), lo que significa que se 
espera que los programadores sean responsables y respeten las convenciones 
de nomenclatura y las reglas establecidas.
'''