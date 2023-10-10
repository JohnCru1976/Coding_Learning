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
icono = pygame.image.load(Path(".") / "files" / "ovni.png")  # Instancia del icono
pygame.display.set_icon(icono)  # Asignando instancia del icono a la pantalla

# Bucle principal mientras se ejecuta el juego
se_ejecuta = True
while se_ejecuta:
    # Identifica los eventos que sucedan en cada bucle
    for evento in pygame.event.get():
        # Se detecta el evento QUIT (al cerrar la ventana)
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    # Color del fondo de pantalla
    pantalla.fill((205,144,228))
    pygame.display.update()  # Actualiza lo que se muestra en la pantalla
