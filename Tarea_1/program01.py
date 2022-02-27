# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Evaluar si un numero es par o impar
---------------------------------------------
'''

def evaluar_par(num:int) -> bool:
    
    # Si el número a evaluar es divisible por 2 entonces es par
    if num % 2 == 0:
        return True
    else:
        return False

x = evaluar_par(2)
print(x)