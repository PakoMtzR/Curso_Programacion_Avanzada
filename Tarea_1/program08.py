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

def invertir_numero(num:int) -> None:
    num_str = str(num)[::-1] # Convertimos el número en un string y lo invertimos
    print(num_str)
    print(type(num_str))

invertir_numero(81285)