# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Programa que permita obtener una cantidad N de 
números pseudoaleatorios (donde N es un número entero, mayor a 0) 
utilizando para ello el método/algoritmo de generación de números 
congruencial. En el siguiente documento se encuentra información 
junto con ejemplos para probar el algoritmo.

Fuente: https://www.dropbox.com/s/c31wk8l5maltt8a/Generador%20de%20N%C3%BAmeros%20aleatorios%20congruencial.doc?dl=0
---------------------------------------------------------------
'''

def generar_numeros_aleatorios(cant:int) -> None:
    
    random = [] # Guardará los números aleatorios
    n = []      # Guardará todos los valores de Xi

    # Parametros:
    x_o = 5
    b = 0
    a = 5
    m = 13

    # Algoritmo de Congruencia Lineal:
    n.append(x_o)   # Ingresamos el valor inicial del arreglo xi
    
    for i in range(cant-1):
        n.append(((a*n[i])+b)%m)
        random.append(round(n[i]/m, 4))
        print(f'x[{i+1}] = {random[i]}')

    
generar_numeros_aleatorios(5)
    
    
