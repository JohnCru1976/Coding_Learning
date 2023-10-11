'''Juego creado con fines educativos siguiendo curso Udemy de Federico Garay'''

# Esta línea evita un error lanzado por pylint

from pathlib import Path
import os
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
pygame.display.set_caption("Invasión Espacial")  # Título de la ventana
# Icono y título
icono = pygame.image.load(Path(".") / "files" / "ovni.png")  # Instancia del icono
pygame.display.set_icon(icono)  # Asignando instancia del icono a la pantalla
# Manejo del jugador
jugador_img = pygame.image.load(Path(".") / "files" / "cohete.png") # Instancia del jugador
jugador_pos_x = 368
jugador_pos_y = 530
jugador_pos_cambio = 0
velocidad = 0.8
tecla_left = False
tecla_right = False
ultima_tecla = None

def jugador(x, y):
    '''Actualiza parametros del jugador'''
    pantalla.blit(jugador_img,(x, y))  # Posicionamiento en pantalla

# Bucle principal mientras se ejecuta el juego
se_ejecuta = True
while se_ejecuta:
    # Color del fondo de pantalla
    pantalla.fill((205,144,228))
    
    # Identifica los eventos que sucedan en cada bucle
    for evento in pygame.event.get():
        # Se detecta el evento QUIT (al cerrar la ventana)
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                tecla_left = True
                ultima_tecla = pygame.K_LEFT
            if evento.key == pygame.K_RIGHT:
                tecla_right = True
                ultima_tecla = pygame.K_RIGHT
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                tecla_left = False
                if tecla_right:
                    ultima_tecla = pygame.K_RIGHT
            if evento.key == pygame.K_RIGHT:
                tecla_right = False
                if tecla_left:
                    ultima_tecla = pygame.K_LEFT
        
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

    # Movimiento jugador
    if ultima_tecla == pygame.K_RIGHT:
        jugador_pos_cambio += velocidad
    if ultima_tecla == pygame.K_LEFT:
        jugador_pos_cambio -= velocidad
    if not tecla_right and not tecla_left:
        jugador_pos_cambio = 0
    ultima_tecla = None 
    
    # Posicion del jugador:
    jugador_pos_x += jugador_pos_cambio
    jugador(jugador_pos_x, jugador_pos_y)
    pygame.display.update()  # Actualiza lo que se muestra en la pantalla
