'''
# -*- coding: utf-8 -*-
Fecha de creacion: 03/03/2022
autor: PakoMtz 
 
-----------------------------------------------------------------------------
Problema: Utilizando recursividad, generar un programa que calcule la suma
 harmónica de un número entero positivo N ingresado por el usuario

Fuentes: https://es.wikipedia.org/wiki/Serie_arm%C3%B3nica_(matem%C3%A1tica)
-----------------------------------------------------------------------------
'''

def suma_armonica(n:int) -> float:
    if n > 1:
        return (1/n) + suma_armonica(n-1)
    else:
        return 1

def imprimir_problema(n:int, suma_armonica:float) -> None:
    for i in range(1, n+1):
        print(f'1/{i}', end='')
        if i < n:
            print(' + ', end='')
        else:
            print(' = ', end='')
    print(str(suma_armonica))

suma = round(suma_armonica(7), 4)
imprimir_problema(7, suma)


