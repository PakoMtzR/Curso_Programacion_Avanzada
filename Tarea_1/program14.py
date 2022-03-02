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
from os import system
import preguntar


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


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 14: Obtener una cantidad N de números pseudoaleatorios ')
        print('              utilizando para ello el método/algoritmo de')
        print('              generación de números congruencial')
        print('----------------------------------------------------------------\n')
        cant_de_numeros = int(input(' Ingresa la cantidad de numero aleatorios: '))
        print('\n')

        if cant_de_numeros < 0: cant_de_numeros *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
        generar_numeros_aleatorios(cant_de_numeros)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un numero entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()    

    
    
