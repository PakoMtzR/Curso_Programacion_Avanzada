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

def invertir(num:int):
    num = str(num)[::-1]
    print(num)

invertir(81285)


'''
    aux = ''
    for i in range(len(num)):
        aux = aux + num[-1-i]
    num = aux
'''