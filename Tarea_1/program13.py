# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Imprimir numeros de la Serie de Padovan

Fuente: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Padovan
---------------------------------------------------------------
'''

from os import system
import preguntar


def serie_padovan(num:int) -> list:
    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    
    padovan = [1, 1, 1]
    
    # Si nos solicitan menos de 3 elementos de la serie, eliminaremos los valores restantes la lista.
    # Ejemplo: num = 1 --> [1], num = 2 --> [1, 1], , num = 3 --> [1, 1, 1]
    if num <= 3:
        for i in range(3-num):
            padovan.pop()   # Elimina el ultimo elemeto de la lista
    
    # Si nos solicitan más elementos de la serie, los generamos y agregamos a la lista.
    # Los demas elementos de la serie de Padovan se generan con la siguiente formula:
    # Pn = Pn-2 + Pn-3, para n >= 3
    else:
        for i in range(3, num):
            padovan.append(padovan[i-2] + padovan[i-3])
        
    return padovan


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 13: Serie de Padovan')
        print('----------------------------------------------------------\n')
        numero_de_elementos = int(input(' Ingrese el número de elementos de la serie: '))
        print('\n')

        # Obtenemos e imprimimos la serie de Padovan
        elementos = []
        elementos = serie_padovan(numero_de_elementos)
        print('\t', end='')
        for i in elementos:
            print(f'{str(i)} ', end='')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

