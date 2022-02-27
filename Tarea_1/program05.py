# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

----------------------------------------------------------------------------
Problema: Generar un triángulo de Pascal

Fuente: https://www.estadisticaparatodos.es/taller/triangulo/triangulo.html
----------------------------------------------------------------------------
'''

# Función para calcular el factorial de un número
def factorial(num:int) -> int:
    factorial = 1
    if num != 0:
        for i in range(num):
            factorial *= (i+1)
        return factorial
    else:
        return factorial

# Función para calcular la combinatoria de dos numeros    
def combinatoria(a:int, b:int) -> int:
    return factorial(a) // (factorial(b) * factorial(a-b))

# Función para imprimir el triángulo de Pascal
def triangulo_pascal(num:int) -> None:
    for i in range(num):
        for k in range(i+1):
            print(combinatoria(i, k), end=' ')
        print('\n')

triangulo_pascal(5)