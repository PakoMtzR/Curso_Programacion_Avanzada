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
from os import system
import preguntar


from itertools import permutations

def posibles_permutaciones(lista_de_datos:list) -> None:
    permutaciones = list(permutations(lista_de_datos))

    print(f'\nPosibles permutaciones -> {len(permutaciones)}\n')
    for permutacion in permutaciones:
        print(f'\t{permutacion}')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        lista = []
        otra_vez = True
        i = 0
        
        while otra_vez == True:
            system('cls')   # Limpiamos la consola

            print('----------------------------------------------------------')
            print(' Programa 30: Permutaciónes de una Lista')
            print('----------------------------------------------------------')
            print(' Generacion de lista, ingrese un valor:\n')
            lista.append(input(f' x[{i}] = '))
            print('\n')
            otra_vez = preguntar.quieres_volver_a_intentarlo(' ¿Deseas ingresar otro valor? [s/n]: ')  # True / False
            i += 1
        
        posibles_permutaciones(lista)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

'''
colores = ['rojo', 'azul', 'verde']
numeros = [0, 8, 9, 1]
posibles_permutaciones(numeros)
'''

