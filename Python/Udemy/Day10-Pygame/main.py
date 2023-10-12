'''Juego creado con fines educativos siguiendo curso Udemy de Federico Garay'''
from pathlib import Path
import os
import random
# pylint: disable=E1101
import pygame
from pygame import mixer

# ****************************************************************************
# DECLARACIÓN DE VARIABLES
# ****************************************************************************
# Establecer el directorio de trabajo en el directorio del archivo
file_diretory = os.path.dirname(__file__)
os.chdir(file_diretory)

# Se inicia el módulo pygame para hacerlo accesible
pygame.init()

# Variables para el control de tiempo
clock = pygame.time.Clock()
last_time = pygame.time.get_ticks()
juego_pausado = False

# Instancia de la pantalla, con valores iniciales ancho y alto
# Ambas coordenadas se inician en la esquina superior izquierda
pantalla = pygame.display.set_mode((800,600))

# Otras configuraciones iniciales
# Título
pygame.display.set_caption("Invasión Espacial")
# Icono
icono = pygame.image.load(Path(".") / "files" / "ovni.png")  # Instancia del icono
pygame.display.set_icon(icono)  # Asignando instancia del icono a la pantalla
# Fondo
fondo = pygame.image.load(Path(".") / "files" / "Fondo.jpg")
# Contadores y texto
fuente = pygame.font.Font('freesansbold.ttf', 32)
fuente_final = pygame.font.Font('freesansbold.ttf', 40)
texto_x = 10
texto_y = 10
# Música
mixer.music.load(Path(".") / "files" / "MusicaFondo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)
sonido_proyectil = mixer.Sound(Path(".") / "files" / "disparo.mp3")
sonido_colision = mixer.Sound(Path(".") / "files" / "Golpe.mp3")
sonido_explosion = mixer.Sound(Path(".") / "files" / "explosion.mp3")

# Variables Manejo del jugador
jugador_img = pygame.image.load(Path(".") / "files" / "cohete.png") # Instancia del jugador
jugador_pos_x = 368
jugador_pos_y = 530
jugador_pos_cambio = 0
velocidad_jugador = 450
tecla_left = False
tecla_right = False
ultima_tecla = None

# Variables enemigo
enemigo_img = pygame.image.load(Path(".") / "files" / "enemigo.png") # Instancia del enemigo
enemigo_pos_x = random.randint(0,736)
enemigo_pos_y = random.randint(50,200)
enemigo_x_velocidad = 500
enemigo_y_velocidad = 50
enemigo_acelaracion = 100

# Variables proyectil
proyectil_img = pygame.image.load(Path(".") / "files" / "bala.png") # Instancia del enemigo
proyectil_pos_x = 0
proyectil_pos_y = 0
proyectil_y_velocidad = 600
proyectil_visible = False

# Variables contadores
vidas = 3
puntos = 0

# ****************************************************************************
# DECLARACIÓN DE FUNCIONES
# ****************************************************************************
def jugador(x, y):
    '''Actualiza parametros del jugador'''
    pantalla.blit(jugador_img,(x, y))  # Posicionamiento en pantalla

def enemigo(x, y):
    '''Actualiza parametros del enemigo'''
    pantalla.blit(enemigo_img,(x, y))  # Posicionamiento en pantalla

def disparar_proyectil(x, y):
    '''Actualiza parametros del enemigo'''
    global proyectil_visible
    proyectil_visible = True
     # Posicionamiento en pantalla, incluye offset en relación a la nave
    pantalla.blit(proyectil_img,(x + 16, y))

def detectar_colision(coord_obj1, coord_obj2):
    '''Devuelve True si la distancia entre objetos es menor que 40 pixeles'''
    distancia = ((coord_obj2[0] - coord_obj1[0])  ** 2 +
                 (coord_obj2[1] - coord_obj1[1])  ** 2) ** (1/2)
    if distancia <= 35:
        return True
    return False

def mostrar_puntuacion (x, y):
    '''Muestra la puntuación en la pantalla'''
    texto = fuente.render(f"Puntos: {puntos}", True,(255,255,255))
    pantalla.blit(texto,(x,y))

def texto_final():
    '''Muestra texto final juego'''
    texto = fuente_final.render("¿Otra partida? (S / N)", True,(255,255,255))
    pantalla.blit(texto,(60,200))

# ****************************************************************************
# Bucle principal mientras se ejecuta el juego
# ****************************************************************************
se_ejecuta = True
while se_ejecuta:
    # Color del fondo de pantalla
    # pantalla.fill((205,144,228))

    # Imagen de fondo
    pantalla.blit(fondo,(0,0))

    # *************************************
    # Identifica los eventos que sucedan en cada bucle
    # *************************************
    for evento in pygame.event.get():
        # Se detecta el evento QUIT (al cerrar la ventana)
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # Evento pulsar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                tecla_left = True
                ultima_tecla = pygame.K_LEFT
            if evento.key == pygame.K_RIGHT:
                tecla_right = True
                ultima_tecla = pygame.K_RIGHT
            if evento.key == pygame.K_SPACE:
                if not proyectil_visible and not juego_pausado:
                    sonido_proyectil = mixer.Sound(Path(".") / "files" / "disparo.mp3")
                    sonido_proyectil.play()
                    proyectil_pos_x = jugador_pos_x
                    proyectil_pos_y = jugador_pos_y
            if evento.key == pygame.K_s and juego_pausado:
                # Se reinicia el jugador y el enemigo
                jugador_pos_x = 368
                jugador_pos_y = 530
                enemigo_pos_x = random.randint(0,736)
                enemigo_pos_y = random.randint(50,300)
                enemigo_x_velocidad = 500
                puntos = 0
                juego_pausado = False
            if evento.key == pygame.K_n and juego_pausado:
                se_ejecuta = False
        # Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                tecla_left = False
                if tecla_right:
                    ultima_tecla = pygame.K_RIGHT
            if evento.key == pygame.K_RIGHT:
                tecla_right = False
                if tecla_left:
                    ultima_tecla = pygame.K_LEFT

    # Obten el tiempo transcurrido desde el último fotograma
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000.0  # Convierte a segundos
    last_time = current_time

    if not juego_pausado:
        
        # *************************************
        # LÓGICA DEL JUGADOR
        # *************************************
        if ultima_tecla == pygame.K_RIGHT:
            jugador_pos_cambio += velocidad_jugador
        if ultima_tecla == pygame.K_LEFT:
            jugador_pos_cambio -= velocidad_jugador
        if not tecla_right and not tecla_left:
            jugador_pos_cambio = 0
        ultima_tecla = None
        # Actualiza posicion del jugador:
        nueva_posicion = jugador_pos_x + jugador_pos_cambio * delta_time
        if  0 <= nueva_posicion <= 736:  # Se mantiene en los bordes
            jugador_pos_x = nueva_posicion
        # Situa al jugador
        jugador(jugador_pos_x, jugador_pos_y)

        # *************************************
        # LÓGICA DEL ENEMIGO
        # *************************************
        nueva_posicion = enemigo_pos_x + enemigo_x_velocidad * delta_time
        if  nueva_posicion <= 0:   # Toca la izquierda
             # Se mueve a la derecha y acelera
            enemigo_x_velocidad = abs((enemigo_x_velocidad - enemigo_acelaracion))
            enemigo_pos_y += enemigo_y_velocidad  # Baja una posición
        if nueva_posicion >= 736:  # Toca la derecha
             # Se mueve a la izquierda y acelera
            enemigo_x_velocidad = -abs((enemigo_x_velocidad + enemigo_acelaracion))
            enemigo_pos_y += enemigo_y_velocidad  # Baja una posición
        # Aquí se crea el movimiento
        enemigo_pos_x = nueva_posicion
        # Sitúa al enemigo
        enemigo(enemigo_pos_x, enemigo_pos_y)

        # *************************************
        # LÓGICA DEL PROYECTIL
        # *************************************
        proyectil_pos_y -= proyectil_y_velocidad * delta_time
        if proyectil_pos_y <= 0:
            proyectil_visible = False
        else:
            disparar_proyectil(proyectil_pos_x, proyectil_pos_y)

        # *************************************
        # COLISIONES
        # *************************************
        # Colisión entre bala y enemigo
        colision = detectar_colision((proyectil_pos_x, proyectil_pos_y),
                                     (enemigo_pos_x, enemigo_pos_y))
        if colision:
            sonido_colision.play()
            # Suma un punto
            puntos += 1
            # Se reinicia el proyectil
            proyectil_visible = False
            proyectil_pos_y = 0
            proyectil_pos_x = 0
            # Se reinicia el enemigo
            enemigo_pos_x = random.randint(0,736)
            enemigo_pos_y = random.randint(50,300)
            enemigo_x_velocidad = 500 + puntos * 30

        # Colisión entre jugador y enemigo
        colision = detectar_colision((jugador_pos_x, jugador_pos_y), (enemigo_pos_x, enemigo_pos_y))
        if colision:
            sonido_explosion.play()
            texto_final()
            juego_pausado = True

        # MARCADOR
        mostrar_puntuacion (texto_x, texto_y)

        # Actualiza lo que se muestra en la pantalla
        pygame.display.update()

        # Controla la velocidad de fotogramas
        clock.tick(60)

## ESTE ES UN CÓDIGO QUE DECIDÍ CONSERVAR PARA EL MANEJO CON RATÓN
'''# El jugador se mueve por el eje x junto con el movimiento del mouse
        if evento.type == pygame.MOUSEMOTION:
            mouse_x_pos = evento.dict["pos"][0]
            mouse_y_pos = evento.dict["pos"][1]
            if mouse_x_pos <= 736 and mouse_y_pos > 300:  # Área de actuación del mouse
                jugador_pos_x = mouse_x_pos
        # Cuando el rato sale de la pantalla el jugador se sitúa en el borde derecho
        if evento.type == pygame.WINDOWLEAVE:
            if jugador_pos_x > 500:
                jugador_pos_x = 736'''