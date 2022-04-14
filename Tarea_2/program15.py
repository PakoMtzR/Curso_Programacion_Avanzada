'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita calcular n números de la serie 
de Fibonacci, con valores de n en el intervalo [1, 10000] 

Fuentes: 
---------------------------------------------------------------
'''

def fibonacci(num:int) -> int:

    if num == 0 or num == 1:
        return num
    
    return fibonacci(num-1) + fibonacci(num-2)

for i in range(20):
    print(fibonacci(i), end=' ')