'''Juego creado con fines educativos siguiendo curso Udemy de Federico Garay'''

from pathlib import Path
import os
import random
# pylint: disable=E1101
import pygame

# Establecer el directorio de trabajo en el directorio del archivo
file_diretory = os.path.dirname(__file__)
os.chdir(file_diretory)

# Se inicia el módulo pygame para hacerlo accesible
pygame.init()

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


# Variables Manejo del jugador
jugador_img = pygame.image.load(Path(".") / "files" / "cohete.png") # Instancia del jugador
jugador_pos_x = 368
jugador_pos_y = 530
jugador_pos_cambio = 0
velocidad_jugador = 0.7
tecla_left = False
tecla_right = False
ultima_tecla = None

# Variables enemigo
enemigo_img = pygame.image.load(Path(".") / "files" / "enemigo.png") # Instancia del enemigo
enemigo_pos_x = random.randint(0,736)
enemigo_pos_y = random.randint(50,300)
enemigo_x_velocidad = 0.5
enemigo_y_velocidad = 20
enemigo_acelaracion = 0.05


def jugador(x, y):
    '''Actualiza parametros del jugador'''
    pantalla.blit(jugador_img,(x, y))  # Posicionamiento en pantalla

def enemigo(x, y):
    '''Actualiza parametros del enemigo'''
    pantalla.blit(enemigo_img,(x, y))  # Posicionamiento en pantalla



# Bucle principal mientras se ejecuta el juego
se_ejecuta = True
while se_ejecuta:
    # Color del fondo de pantalla
    # pantalla.fill((205,144,228))
    # Imagen de fondo
    pantalla.blit(fondo,(0,0))

    # Identifica los eventos que sucedan en cada bucle
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

    # Movimiento jugador
    if ultima_tecla == pygame.K_RIGHT:
        jugador_pos_cambio += velocidad_jugador
    if ultima_tecla == pygame.K_LEFT:
        jugador_pos_cambio -= velocidad_jugador
    if not tecla_right and not tecla_left:
        jugador_pos_cambio = 0
    ultima_tecla = None

    # Actualiza posicion del jugador:
    nueva_posicion = jugador_pos_x + jugador_pos_cambio
    if  0 <= nueva_posicion <= 736:  # Se mantiene en los bordes
        jugador_pos_x = nueva_posicion
    # Situa al jugador
    jugador(jugador_pos_x, jugador_pos_y)

    # Actualizar posición del enemigo
    nueva_posicion = enemigo_pos_x + enemigo_x_velocidad
    if  nueva_posicion <= 0:   # Toca la izquierda
        enemigo_x_velocidad = abs(enemigo_x_velocidad - enemigo_acelaracion)  # Se mueve a la derecha y acelera
        enemigo_pos_y += enemigo_y_velocidad  # Baja una posición
    if nueva_posicion >= 736:  # Toca la derecha
        enemigo_x_velocidad = -abs(enemigo_x_velocidad + enemigo_acelaracion)  # Se mueve a la izquierda y acelera
        enemigo_pos_y += enemigo_y_velocidad  # Baja una posición
    # Aquí se crea el movimiento
    enemigo_pos_x = nueva_posicion
    # Sitúa al enemigo
    enemigo(enemigo_pos_x, enemigo_pos_y)

    # Actualiza lo que se muestra en la pantalla
    pygame.display.update()






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