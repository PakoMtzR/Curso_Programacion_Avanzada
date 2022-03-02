# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Evaluar si un numero es par o impar
---------------------------------------------
'''
from os import system
import preguntar

# Si el número a evaluar es divisible por 2 entonces es par
def evaluar_par(num:int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------------------')
        print(' Programa 1: Evaluar si un número es par o impar')
        print('-----------------------------------------------------\n')
        n = int(input(' Ingrese un número entero: '))
        print('\n')

        if evaluar_par(n) == True:
            print(f" '{n}' es un número par")
        else:
            print(f" '{n}' es un número impar")

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, te pedí un número ENTEROOOO!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True o False