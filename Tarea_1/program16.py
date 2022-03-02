# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Obtener la lista de números narcisistas que existan 
en un intervalo dado por el usuario

Fuente: https://mathworld.wolfram.com/NarcissisticNumber.html
---------------------------------------------------------------
'''

from os import system
import preguntar


def verificar_si_es_narcisista(num:int) -> None:
    
    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    
    num_str = str(num)
    suma_de_cubos = 0
    
    # Un número es narcisista cuando la suma de los cubos de cada uno de los digitos es igual al mismo numero.
    # Ejemplo: 407 = 4^3 + 0^3 + 7^3
    for i in num_str:
        suma_de_cubos += (int(i) ** 3)
    
    # Imprimimos la demostracion
    print('\t', end='')
    for i , value in enumerate(num_str):
        if i != 0:
            print(' + ', end='')
        print(f'{str(value)}³', end='')
    print(f' = {str(suma_de_cubos)}')

    # Validamos si es número narcisista
    if num == suma_de_cubos:
        print(f'\n   {str(num)} es un número narcisita')
    else:
        print(f'\n   {str(num)} NO es un número narcisita')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------')
        print(' Programa 16: Número Narcisista')
        print('-----------------------------------------\n')
        numero = int(input(' Ingrese un número: '))
        print('\n')

        verificar_si_es_narcisista(numero)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False