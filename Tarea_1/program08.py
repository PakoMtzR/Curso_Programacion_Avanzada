# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Invertir un numero.

Ejemplo: Si ingresa N = 5243, 
el programa debe mostrar 3425
---------------------------------------------
'''
from os import system
import preguntar


def invertir_numero(num:int) -> int:
    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    num_str = str(num)[::-1] # Convertimos el número en un string y lo invertimos
    return int(num_str)


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------------------')
        print(' Programa 8: Invertir un numero')
        print('-----------------------------------------------------\n')
        numero = int(input(' Ingrese el número a invertir: '))
        print('\n')

        numero_invertido = invertir_numero(numero) 
        print(f' {numero} --> {numero_invertido}')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()