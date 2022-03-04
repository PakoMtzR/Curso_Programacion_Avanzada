# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Descomponer un numero en suma de 
unidades, decenas, centenas, ...
---------------------------------------------
'''

from os import system
import preguntar


def descomponer(num:int) -> None:

    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    
    num_str = str(num)
    factores = []

    for i, value in enumerate(num_str):
        factores.append(int(value)*(10**(len(num_str)-(i+1))))

    print('\t', end='')
    for i , value in enumerate(factores):
        if i != 0:
            print(' + ', end='')

        print(str(value), end='')

    print(f' = {str(num)}')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------------------')
        print(' Programa 6: Descomponer un numero en suma de')
        print('             unidades, decenas, centenas, ...')
        print('-----------------------------------------------------\n')
        numero = int(input(' Ingrese el número a descomponer: '))
        print('\n')

        descomponer(numero)   # Descomponemos el numero y lo imprimimos

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()