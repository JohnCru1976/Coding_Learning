from functions import *

# Lista de palabras
palabras = [
    "abrir", "acceso", "agua", "aire", "amar", "amigo", "animal", "año", "apellido", "aprender",
    "arbol", "arte", "asistir", "auto", "avión", "bailar", "bajo", "belleza", "bien", "boca",
    "calle", "cama", "caminar", "canción", "carro", "casa", "cielo", "comer", "correr", "cosa",
    "criatura", "cuerpo", "dar", "decir", "deporte", "dinero", "dormir", "día", "edad", "educación",
    "ejemplo", "elección", "encontrar", "entender", "escuela", "esperar", "estar", "estudiar", "familia", "feliz",
    "fuego", "gato", "gente", "gracias", "hablar", "hacer", "hijo", "hombre", "hora", "iniciar",
    "jugar", "lago", "largo", "leer", "lugar", "luz", "mañana", "mamá", "mano", "mar",
    "mes", "mesa", "mi", "mirar", "mujer", "mundo", "música", "niño", "noche", "nombre",
    "nuevo", "ojo", "padre", "palabra", "papel", "parar", "pensar", "persona", "piedra", "pieza",
    "piso", "poder", "poner", "puerta", "querer", "rápido", "razón", "reír", "rojo", "saber",
    "seguir", "sentir", "ser", "silla", "sistema", "sobre", "sol", "sombra", "sonreír", "tardar",
    "té", "tener", "tiempo", "tocar", "trabajar", "usar", "venir", "ver", "vida", "viento",
    "vino", "vez", "voz", "vuelo", "zona", "árbol", "éxito", "ícono", "órbita", "último", "útil"
]

palabra_azar = random_word(palabras)
letras_acertadas = []
letras_falladas = []
fin = [False]
opcion = "s"
partidas_ganadas = 0

for n in range(1,rondas+1):
    palabra_azar = random_word(palabras)
    letras_acertadas = []
    letras_falladas = []
    fin = [False]

    while fin[0] is False and len(letras_falladas) < limite_fallos:        
        fin = introducir_letra(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, n)
        letras_acertadas = fin[1][1]
        letras_falladas = fin[1][2]

    #introducir_letra(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, n)
    if len(letras_falladas) >= limite_fallos:
        print("**********************")
        print("LO SIENTO, HAS PALMAO")
        print(f"LA PALABRA ES: {palabra_azar.upper()}")
        print("**********************")
    else:
        print("*****************")
        print("LO HAS CONSEGUIDO")
        print("*****************")
        partidas_ganadas += 1

    opcion = input("PULSA CUALQUIER TECLA PARA CONTINUAR")
    if palabras:
        palabras.remove(palabra_azar)

presentacion(palabra_azar, letras_acertadas, letras_falladas, partidas_ganadas, rondas + 1)
