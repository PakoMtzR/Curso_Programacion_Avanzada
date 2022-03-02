# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

------------------------------------------------
Problema: Suma digitos

Ejemplo: Si se ingresa N = 1521, el resultado a 
mostrar es: Suma = 1 + 5 + 2 + 1 = 9
------------------------------------------------
'''

from os import system
import preguntar


def suma_digitos(num:int) -> None:

    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    
    num_str = str(num)
    digitos = [i for i in num_str] # Guardamos los digitos del número en una lista <str>
    
    # Sumamos los digitos del numero
    suma_de_digitos = 0
    for i in num_str:
        suma_de_digitos += int(i)
    
    print('\t', end='')
    for i , value in enumerate(digitos):
        if i != 0:
            print(' + ', end='')

        print(str(value), end='')

    print(f' = {str(suma_de_digitos)}')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------')
        print(' Programa 9: Suma de Digitos')
        print('-----------------------------------------\n')
        numero = int(input(' Ingrese un número: '))
        print('\n')

        suma_digitos(numero)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()