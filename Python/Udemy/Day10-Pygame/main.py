'''Juego creado con fines educativos siguiendo curso Udemy de Federico Garay'''
 
# Esta línea evita un error lanzado por pylint
# pylint: disable=E1101  
import pygame
# Se inicia el módulo pygame para hacerlo accesible
pygame.init()
# Instancia de la pantalla, con valores iniciales ancho y alto
pantalla = pygame.display.set_mode((800,600))

# Bucle principal mientras se ejecuta el juego
se_ejecuta = True
while se_ejecuta:
    # Identifica los eventos que sucedan en cada bucle
    for evento in pygame.event.get():
        # Se detecta el evento QUIT (al cerrar la ventana)
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
