# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Imprimir numeros de la Serie de Padovan

Fuente: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Padovan
---------------------------------------------------------------
'''

def serie_padovan(num:int):
    padovan = [1, 1, 1]
    if num <= 3:
        for i in range(3-num):
            padovan.pop(i)
    else:
        for i in range(num-3):
            padovan.append(padovan[i] + padovan[i+1])
    
    # print(padovan)
    return padovan


elementos = []
elementos = serie_padovan(15)
print(elementos)