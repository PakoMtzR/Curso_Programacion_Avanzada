# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

------------------------------------------------------
Problema: Calcular el doble factorial (n!!) 
de un número entero positivo

fuente: https://es.wikipedia.org/wiki/Doble_factorial
------------------------------------------------------
'''

from os import system
import preguntar


def calcular_doble_factorial(num:int) -> int:
    
    dobleFactorial = 1
    
    # La formula del doble factorial de un número par es diferente que al de un número impar (consulte el link)
    if num % 2 == 0:
        for k in range(num // 2):   # a // b --> División entera
            dobleFactorial *= 2 * (k+1)
    else:
        for k in range((num + 1) // 2):
            dobleFactorial *= ((2*(k+1)) - 1)
    
    return dobleFactorial


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('--------------------------------------------------')
        print(' Programa 10: Calcular el doble factorial (n!!) ')
        print('--------------------------------------------------\n')
        numero = int(input(' Ingrese un número: '))
        print('\n')

        if numero < 0: numero *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
        
        doble_factorial = calcular_doble_factorial(numero)

        print(f'\t {str(numero)}!! = {doble_factorial}')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()
#print(doble_factorial(9))
'''
ejemplos:
9!! = 945
4!! = 8
'''
