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

def narcisistas(num:int):
    num = str(num)
    aux = 0
    
    for i in num:
        aux = aux + (int(i) ** 3)
    
    if num == str(aux):
        return True
    else:
        return False
    
print(narcisistas(153))