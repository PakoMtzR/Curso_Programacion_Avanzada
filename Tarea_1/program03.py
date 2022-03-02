# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

-----------------------------------------------------
Problema: Evaluar si un año es bisiesto

Un año es bisiesto si es múltiplo de 4, exceptuando 
los múltiplos de 100, que sólo son bisiestos cuando 
son múltiplos además de 400, por ejemplo el año 1900 
no fue bisiesto, pero el año 2000 si lo es. 
-----------------------------------------------------
'''
from os import system
import preguntar


def es_bisiesto(year:int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
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
        print(' Programa 3: Evaluar si un año es bisiesto')
        print('-----------------------------------------------------\n')
        year = int(input(' Ingrese un año: '))
        print('\n')

        if es_bisiesto(year) == True:
            print(f' {year} es un año bisiesto')
        else:
            print(f' {year} NO es un año bisiesto')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, te pedí que ingresaras un añoooo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()