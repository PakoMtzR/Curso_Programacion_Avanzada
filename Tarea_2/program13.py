'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Generar un programa que mediante recursividad permita 
resolver el problema de las Torres de Hanoi, permitir que el 
usuario ingrese el número de discos que se deben de mover 
(cerrar el intervalo de 3 a 15 discos) y mostrar los movimientos 
que se deben de realizar (todo puede ser en texto, aunque, de 
ser posible, mostrar los discos y los movimientos)

Fuentes: https://es.wikipedia.org/wiki/Torres_de_Han%C3%B3i
---------------------------------------------------------------
'''
from os import system
import preguntar

def torreHanoi(disco_i, origen, destino, auxiliar):
    
    # Caso trivial: Un solo disco
    if disco_i == 1:
        
        print(f' Mover el disco 1 de {origen} a {destino}')
        return
    
    torreHanoi(disco_i - 1, origen, auxiliar, destino)
    print(f' Mover el disco {disco_i} de {origen} a {destino}')
    torreHanoi(disco_i - 1, auxiliar, destino, origen)


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 13: Torres de Hanoi')
        print('----------------------------------------------------------\n')
        cant_discos = int(input('Ingrese la cantidad de discos: '))
        print('\n Instrucciones:')
        print('-----------------------------------------------')
        torreHanoi(cant_discos, 'A', 'B', 'C')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False