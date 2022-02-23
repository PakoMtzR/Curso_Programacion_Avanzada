# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Descomponer un numero en suma de 
unidades, decenas, centenas, ...
---------------------------------------------
'''

def descomponer(num:int):
    num = str(num)
    factores = []

    '''
    for i in range(len(num)):
        factores.append(int(num[i])*(10**(len(num)-(i+1))))
    '''
    for i, value in enumerate(num):
        factores.append(int(value)*(10**(len(num)-(i+1))))

    print(factores)

descomponer(3580)