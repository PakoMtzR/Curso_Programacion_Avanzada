# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Descomponer un numero en suma de 
unidades, decenas, centenas, ...
---------------------------------------------
'''

def descomponer(num:int) -> None:
    
    num_str = str(num)
    factores = []

    for i, value in enumerate(num_str):
        factores.append(int(value)*(10**(len(num_str)-(i+1))))

    print(factores)

descomponer(3580)