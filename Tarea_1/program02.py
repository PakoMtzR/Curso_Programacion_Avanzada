# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: imprimir tablas de multiplicar
---------------------------------------------
'''

def imprimir_tabla(num:int):
    for i in range(10):
        print(f'{i+1} * {num} = {(i+1)*num}')

imprimir_tabla(8)