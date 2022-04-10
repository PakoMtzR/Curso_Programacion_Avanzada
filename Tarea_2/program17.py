'''
# -*- coding: utf-8 -*-
Fecha de creacion: 07/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Generar un programa que realice la simulación del 
'Juego de la vida' propuesto por el matemático John Horton Conway 
en 1970.

Fuentes: https://es.wikipedia.org/wiki/Juego_de_la_vida
---------------------------------------------------------------
'''

import pygame
#from pygame.locals import *
import numpy as np
from time import sleep

# Iniciamos una ventana de pygame
pygame.init()
pygame.display.set_caption('El juego de la vida :D')
width, height = 750, 750 # ancho y largo de 750x750 px
screen = pygame.display.set_mode((height, width))
background = 25, 25, 25     # color de fondo
screen.fill(background)

# Definimos el ancho y largo de las celulas
nxC, nyC = 45, 45   # nxC -> numero de celulas en x, nyC -> numero de celulas en y
dimCW = width / nxC     # dividimos el ancho de la pantalla en el numero de celdas en x 'dimCW = dimension Cell Width'
dimCH = height / nyC    # dividimos el largo de la pantalla con el numero de celdas en y

# Estado inicial de las celdas. Vivas = 1; Muertas = 0.
gameState = np.zeros((nxC, nyC))

pauseExect = False  # Variable que nos servira para pausar el programa

while True:

    new_gameState = np.copy(gameState)

    screen.fill(background)
    sleep(0.1)

    # Registramos eventos del teclado y mouse o si quiere salir del programa
    for evento in pygame.event.get():
        # Evento para pausar o reanudar el juego
        if evento.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
            if pauseExect == True:
                pygame.display.set_caption('El juego de la vida :D (pausa)')
            else:
                pygame.display.set_caption('El juego de la vida :D')
        
        # Evaluamos si el han dado clic con el mouse
        mouse_click = pygame.mouse.get_pressed()
        
        if sum(mouse_click) > 0:
            posX, posY = pygame.mouse.get_pos()     # Obtenemos la posicion del click
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))   # Mapeamos esa posicion en el juego 
            new_gameState[celX, celY] = not mouse_click[2]
        
        # Evento de salida
        if evento.type == pygame.QUIT:
            quit()

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:
                # Calculamos la cantidad de vecinos
                n_vecinos = gameState[(x-1) % nxC, (y-1) % nyC] + \
                            gameState[(x)   % nxC, (y-1) % nyC] + \
                            gameState[(x+1) % nxC, (y-1) % nyC] + \
                            gameState[(x-1) % nxC, (y) % nyC] + \
                            gameState[(x+1) % nxC, (y) % nyC] + \
                            gameState[(x-1) % nxC, (y+1) % nyC] + \
                            gameState[(x)   % nxC, (y+1) % nyC] + \
                            gameState[(x+1) % nxC, (y+1) % nyC]
                
                # Regla #1: Una celula 'muerta' con exactamente 3 vecinas vivas, 'revive'
                if gameState[x,y] == 0 and n_vecinos == 3:
                    new_gameState[x,y] = 1

                # Regla #2: Una celucla 'viva' con menos de 2 o mas de 3 vecinas vivas, 'muere'
                elif gameState[x,y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
                    new_gameState[x,y] = 0

            # Generamos una cuadricula en toda la pantalla  
            poly = [(x*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    (x*dimCW, (y+1)*dimCH)]
            
            # Dibujamos la celda para cada par de x e y:
            if new_gameState[x,y] == 0:
                pygame.draw.polygon(screen, (32,32,32), poly, 1)
            else:
                pygame.draw.polygon(screen, (225,225,225), poly, 0)
    
    # Actualizamos el estado del juego
    gameState = np.copy(new_gameState) 
    pygame.display.flip()

pygame.quit()    
    
    
    
