'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema:

Fuentes: 
---------------------------------------------------------------
'''
import pyautogui
import os
import requests
from time import sleep

buzz = 'https://th.bing.com/th/id/OIP.C8AuVqwtr-Je7ssyUeY6lwAAAA?pid=ImgDet&rs=1'


f = open('buzz.jpg','wb')
response = requests.get(buzz)
f.write(response.content)
f.close()
'''



def abrir_explorador():
    for i in range(5):
        pyautogui.hotkey('win', 'e')


direccion = os.path.dirname(os.path.abspath(__file__))
direccion += '\\buzz.jpg'

cambiar_fondo = f'reg add "hkcu\control panel\desktop" /v wallpaper /d "{direccion}" /f'

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
pyautogui.typewrite(cambiar_fondo)
pyautogui.press('enter')

#
#print(os.path.dirname(os.path.abspath(__file__)))
#print("download successful")

pyautogui.press('win')
#pyautogui.typewrite('edge\n')
pyautogui.write(buzz)


'''


