# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

------------------------------------------------------
Problema: Calcular el doble factorial (n!!) 
de un número entero positivo

fuente: https://es.wikipedia.org/wiki/Doble_factorial
------------------------------------------------------
'''

def doble_factorial(num:int):
    dobleFactorial = 1
    if num % 2 == 0:
        for k in range(int(num / 2)):
            dobleFactorial = dobleFactorial * 2 * (k+1)
    else:
        for k in range(int((num + 1) / 2)):
            dobleFactorial = dobleFactorial * ((2 * (k+1)) - 1)
    
    return dobleFactorial


print(doble_factorial(9))
