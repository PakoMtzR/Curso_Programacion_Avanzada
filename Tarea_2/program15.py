'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita calcular n números de la serie 
de Fibonacci, con valores de n en el intervalo [1, 10000] 

Fuentes: 
---------------------------------------------------------------
'''
from os import system
import preguntar


def fibonacci(num:int) -> int:
    if num == 0 or num == 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 15: Fibonacci')
        print('----------------------------------------------------------\n')
        n = int(input('Ingrese la cantidad elementos que quiera imprimir de la serie: '))
        print('\n')
        # Imprimimos n elementos de la serie Fibonacci
        for i in range(n):
            print(fibonacci(i), end=' ')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

