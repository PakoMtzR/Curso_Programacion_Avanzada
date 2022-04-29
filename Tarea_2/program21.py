'''
# -*- coding: utf-8 -*-
Fecha de creacion: 29/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Utilizando la librería PYAUTOGUI, generar una buena broma 
(conocidas como prank) en la que el programa de Python tome el 
control ya sea del ratón o del teclado o de ambos, para confundir al usuario...

Fuentes: jsjsjsjs
---------------------------------------------------------------
'''
import pyautogui
import requests
from time import sleep
import webbrowser
import random

# Buzzzlight year!!!! :0
buzz_img = 'https://th.bing.com/th/id/OIP.C8AuVqwtr-Je7ssyUeY6lwAAAA?pid=ImgDet&rs=1'
response = requests.get(buzz_img)
for i in range(10000):
    with open(f'buzz{i}.jpg','wb') as img:
        img.write(response.content)

# Obtener el alto y ancho de la pantalla
ancho, alto = pyautogui.size()

# Reproducir video de youtube
webbrowser.open('https://www.youtube.com/watch?v=uxODMpZxMzg')
#pyautogui.press('k')


# Subir volumen al maximooooo!!!!
for i in range(100):
    pyautogui.press('volumeup')

#contador = 0
while True:    
    '''
    contador += 1
    if contador == 6:
        break   
    '''    

    # Mover mouse
    pos_x = random.randint(0, ancho-1)
    pos_y = random.randint(0, alto-1)
    pyautogui.moveTo(pos_x, pos_y, duration=0.1)

    # Subir volumen
    pyautogui.press('volumeup')
    
    # Abrir ventanas del explorador de archivos
    pyautogui.hotkey('win', 'e')
    sleep(0.2)