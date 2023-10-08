import re

''' CHAT-GPT: MÓDULO RE
El módulo re en Python proporciona funcionalidades para trabajar con expresiones regulares, 
que son patrones utilizados para buscar y manipular cadenas de texto de una manera flexible y poderosa

1.- Búsqueda de patrones:
    re.search(): Busca un patrón en una cadena de texto y devuelve la primera coincidencia encontrada.
    re.match(): Busca un patrón al principio de una cadena de texto y devuelve la primera coincidencia
                si está presente en el inicio de la cadena.
2.- Coincidencia de patrones:
    re.findall(): Encuentra todas las coincidencias del patrón en una cadena de texto y 
                  devuelve una lista de todas las coincidencias.
    re.finditer(): Encuentra todas las coincidencias del patrón en una cadena de texto y
                   devuelve un iterador que proporciona objetos de coincidencia para cada una.
3.- Sustitución de texto:
    re.sub(): Reemplaza todas las coincidencias de un patrón en una cadena de texto con un texto especificado.
    re.subn(): Similar a re.sub(), pero también devuelve el número de sustituciones realizadas.
4.- División de texto:
    re.split(): Divide una cadena de texto en una lista de subcadenas utilizando un patrón como separador.
5.- Objetos de coincidencia (Match):
    Cuando se encuentra un patrón en una cadena de texto, se crea un objeto de coincidencia que contiene información sobre la coincidencia, como la posición en la cadena, el texto coincidente y grupos capturados.
6.- rupos y captura de información:
    Los grupos se definen utilizando paréntesis en el patrón y permiten capturar partes específicas de una coincidencia.
    re.group(): Devuelve el texto coincidente de todo el patrón o de un grupo específico.
    re.groups(): Devuelve una tupla de todos los grupos capturados en una coincidencia.
    re.groupdict(): Devuelve un diccionario de nombres de grupo a valores capturados.
7.- Modificadores y opciones:
    Puedes utilizar modificadores como re.IGNORECASE para realizar búsquedas insensibles a mayúsculas y minúsculas.
    Puedes utilizar otras opciones para controlar el comportamiento de las expresiones regulares.
8.- Caracteres especiales:
    Los caracteres especiales como . (punto), * (asterisco), + (más) y otros tienen significados específicos 
    en las expresiones regulares y se utilizan para definir patrones.
    \d -> dígito numérico
    \w -> cualquier caracter alfanumérico
    \s -> espacio en blanco
    \D -> NO es numérico
    \W -> NO es alfanumérico
    \S -> NO es un espacio en blanco
    CUANTIFICADORES
    ?   Repeción 1 vez o ninguna
    *   Repetición 0 o más veces
    +   Repetición una o más veces
    {n}  Repetición exactamente un número n de veces
    {n, m} Repetición exactamente un número de n a m veces
    {n, }  Repetición de n a infinitas veces
    LOGICOS
    |   Or
    .... Sustitucion caracteres
    ^   Al comienzo del string
    $   Al final
    [^] Se excluye   ej. [^\s]+
 '''

# EJEMPLOS DE FEDE
texto = "Si necesitas -dsdsdsd ayuda llama al 658-598-9977 las 24 horas al servicio de ayuda online 458-298-3477"

patron = r'\D{1}\w{7}'
# Otros patrones: '\d{3}-\d{3}-\d{4}' 'ayuda'  '\D{1}\w{7}'
resultado_busqueda = re.search(patron, texto)
print(resultado_busqueda)
print(resultado_busqueda.group())  #-> funciona conjuntamente con re.compile()
resultado_busqueda = re.findall(patron, texto)
print(resultado_busqueda)
for hallazgo in re.finditer(patron, texto):
    print(hallazgo)

# EJEMPLOS DE CHAT-GPT
# Validación de correo electrónico: 
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # La r indica que es una expresión regular
email = "usuario@example.com"

if re.match(email_pattern, email):
    print("Correo electrónico válido")
else:
    print("Correo electrónico no válido")

# Validación de número de teléfono
text = "Mi número de teléfono es 123-456-7890 y mi otro número es 987-654-3210."
phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)

print("Números de teléfono encontrados:", phone_numbers)

# Reemplazo de palabras ofensivas
text = "Este es un texto ofensivo con palabras inapropiadas."
clean_text = re.sub(r'palabras inapropiadas', '***', text)

print(clean_text)

# Extracción de etiquetas HTML
html = '<p>Este es un <b>párrafo</b> de ejemplo.</p>'
tags = re.findall(r'<.*?>', html)

print("Etiquetas HTML encontradas:", tags)

# Extracción de URL de un texto
text = "Visita mi sitio web en https://www.ejemplo.com y también https://www.otroejemplo.com"
urls = re.findall(r'https?://\S+', text)

print("URLs encontradas:", urls)

#Validación de fechas en formato dd/mm/aaaa
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
date = "31/12/2023"

if re.match(date_pattern, date):
    print("Fecha válida")
else:
    print("Fecha no válida")
