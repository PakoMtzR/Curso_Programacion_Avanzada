# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: Generar un programa que permita al usuario ingresar 
una lista de entre 2 y 6 números enteros y mostrar todas las 
posibles permutaciones de la lista
----------------------------------------------------------
'''

from itertools import permutations

def posibles_permutaciones(lista_de_datos:list) -> None:
    permutaciones = list(permutations(lista_de_datos))

    print(f'Posibles permutaciones -> {len(permutaciones)}')
    for permutacion in permutaciones:
        print(permutacion)

colores = ['rojo', 'azul', 'verde']
numeros = [0, 8, 9, 1]
posibles_permutaciones(numeros)
