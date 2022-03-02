# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

--------------------------------------------------------------
Problema: Desarrollar un programa que muestre la serie de 
números de Pell que el usuario solicite.

Fuente:
https://es.wikipedia.org/wiki/N%C3%BAmero_de_Pell
--------------------------------------------------------------
'''

from os import system
import preguntar


def serie_pell(num:int) -> list:

    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    
    pell = [0, 1]
    
    # Si nos solicitan menos de 2 elementos de la serie, eliminaremos los valores restantes la lista.
    # Ejemplo: num = 1 --> [0], num = 2 --> [0, 1]
    if num <= 2:
        for i in range(2-num):
            pell.pop()  # Elimina el ultimo elemeto de la lista
    
    # Si nos solicitan más elementos de la serie, los generamos y agregamos a la lista.
    # Los demas elementos de la serie de Pell se generan con la siguiente formula:
    # Pn = 2Pn-1 + Pn-2, para n >= 2
    else:
        for i in range(2, num):
            pell.append(2*pell[i-1] + pell[i-2])

    return pell


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 19: Serie de Pell')
        print('----------------------------------------------------------\n')
        numero_de_elementos = int(input(' Ingrese el número de elementos de la serie: '))
        print('\n')

        pell = []
        pell = serie_pell(numero_de_elementos)
        print('\t', end='')
        for i in pell:
            print(i, end=' ')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False
