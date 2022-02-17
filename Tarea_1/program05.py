# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

----------------------------------------------------------------------------
Problema: Generar un triángulo de Pascal

Fuente: https://www.estadisticaparatodos.es/taller/triangulo/triangulo.html
----------------------------------------------------------------------------
'''

def factorial(num:int):
    factorial = 1
    if num != 0:
        for i in range(num):
            factorial = factorial * (i+1)
        return int(factorial)
    else:
        return int(factorial)
    
def combinatoria(a:int, b:int):
    return int(factorial(a) / (factorial(b) * factorial(a-b)))

def triangulo_pascal(num:int):
    for i in range(num):
        for k in range(i+1):
            print(combinatoria(i, k), end=' ')
        print('\n')

triangulo_pascal(5)