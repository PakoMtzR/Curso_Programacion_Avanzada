# -*- coding: utf-8 -*-
'''
Fecha de creación: 01/03/2022
autor: PakoMtz 

---------------------------------------------
Esta funcion sirve para saber si el usuario 
quiere volver a intentar correr el programa

Solo retorna True o False
---------------------------------------------
'''

def quieres_volver_a_intentarlo(mensaje = ' ¿Quieres volver a intentarlo? [s/n]: ') -> bool:

    opcion = input(mensaje)
    
    while(opcion != 's' and opcion != 'n'):
        opcion = input(mensaje)
    
    if opcion == 's':
        return True
    else:
        return False
    
if __name__ == 'main':
    quieres_volver_a_intentarlo()

