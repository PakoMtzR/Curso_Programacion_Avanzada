# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

------------------------------------------------------------------------
Problema: Escribir un programa que pida al usuario un número entero y 
muestre en pantalla un triángulo como el siguiente (número ingresado 5):
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

* [1, 3, 5, 7, 9]
------------------------------------------------------------------------
'''

def triangulo_raro_de_impares(num:int):
    
    # Generamos una lista de impares para poder rellenar el triangulo
    impares = []
    i = 0
    while len(impares) < num:
        i = i + 1
        if i % 2 != 0:
            impares.append(i)
    
    print(impares) # <-- Temporal, es solo para verificar si se esta creando bien la lista

    # Generamos el triangulo
    for i in range(num):
        for j in range(i+1):
            print(impares[i-j], end=' ')    # Tengo que documentar esta parte porque me salio de chiripa
        print('\n')

    

triangulo_raro_de_impares(5)