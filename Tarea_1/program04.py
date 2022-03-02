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
from os import system
import preguntar

def triangulo_raro_de_impares(num:int) -> None:
    
    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo

    # Generamos una lista de impares para poder rellenar el triangulo
    impares = []
    i = 0
    while len(impares) < num:
        i += 1
        if i % 2 != 0:
            impares.append(i)
    
    #print(impares) # <-- Temporal, es solo para verificar si se esta creando bien la lista

    # Generamos el triangulo
    for i in range(num):
        for j in range(i+1):
            print(impares[i-j], end=' ')    # Tengo que documentar esta parte porque me salio de chiripa
        print('\n')

    
# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 4: Imprimir un triangulo bien raro de número impares')
        print('----------------------------------------------------------------\n')
        filas = int(input(' Ingrese la cantidad de filas a imprimir: '))
        print('\n')

        triangulo_raro_de_impares(filas)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un numero entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()
