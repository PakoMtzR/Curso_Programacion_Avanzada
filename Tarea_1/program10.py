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

def doble_factorial(num:int) -> int:
    
    dobleFactorial = 1
    
    # La formula del doble factorial de un número par es diferente que al de un número impar (consulte el link)
    if num % 2 == 0:
        for k in range(num // 2):   # a // b --> División entera
            dobleFactorial *= 2 * (k+1)
    else:
        for k in range((num + 1) // 2):
            dobleFactorial *= ((2*(k+1)) - 1)
    
    return dobleFactorial


print(doble_factorial(9))
'''
ejemplos:
9!! = 945
4!! = 8
'''
