# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: imprimir tablas de multiplicar
---------------------------------------------
'''
from os import system
import preguntar

def imprimir_tabla(num:int) -> None:
    for i in range(10):
        print(f'\t{i+1} * {num} = {(i+1)*num}')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------------------')
        print(' Programa 2: Imprimir tabla de multiplicar')
        print('-----------------------------------------------------\n')
        n = int(input(' Ingrese un número entero: '))
        print('\n')

        imprimir_tabla(n)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, te pedí un número ENTEROOOO!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()