# LISTA DE OPCIONES CON MATCH (EN C SWITCH)
# EJEMPLO BÁSICO
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

# EJEMPLO MÁS COMPLEJO
cliente = {
    'nombre': 'Federico',
    'edad': 45,
    'ocupacion': 'instructor'
}

pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {
        'protagonista': 'Keanu Revees',
        'director': 'Lana y Lili Wachonsky'
    }
}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un objeto", type(e))
            print(nombre, edad, ocupacion, sep=" - ")
        case {'titulo': titulo,
              'ficha_tecnica': {
                  'protagonista': protagonista,
                  'director': director
              }}:
            print("Es un objeto", type(e))
            print(titulo, protagonista, director, sep=" - ")
        case _:
            print("No sé que es esto")