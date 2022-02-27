# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Imprimir numeros de la Serie de Padovan

Fuente: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Padovan
---------------------------------------------------------------
'''

def serie_padovan(num:int) -> list:
    
    padovan = [1, 1, 1]
    
    # Si nos solicitan menos de 3 elementos de la serie, eliminaremos los valores restantes la lista.
    # Ejemplo: num = 1 --> [1], num = 2 --> [1, 1], , num = 3 --> [1, 1, 1]
    if num <= 3:
        for i in range(3-num):
            padovan.pop(i)
    
    # Si nos solicitan más elementos de la serie, los generamos y agregamos a la lista.
    else:
        for i in range(num-3):
            padovan.append(padovan[i] + padovan[i+1])

    return padovan


elementos = []
elementos = serie_padovan(15)
print(elementos)