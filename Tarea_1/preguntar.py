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

def quieres_volver_a_intentarlo() -> bool:

    opcion = input(' ¿Quieres volver a intentarlo? [s/n]: ')
    
    while(opcion != 's' and opcion != 'n'):
        opcion = input(' ¿Quieres volver a intentarlo? [s/n]: ')
    
    if opcion == 's':
        return True
    else:
        return False
    
if __name__ == 'main':
    quieres_volver_a_intentarlo()

