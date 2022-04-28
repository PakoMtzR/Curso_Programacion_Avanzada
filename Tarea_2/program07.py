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
from os import system
import preguntar

def suma_armonica(n:int) -> float:
    if n > 1:
        return (1/n) + suma_armonica(n-1)
    else:
        return 1

def imprimir_problema(n:int, suma_armonica:float) -> None:
    print('\n Suma armonica: ')
    for i in range(1, n+1):
        print(f'1/{i}', end='')
        if i < n:
            print(' + ', end='')
        else:
            print(' = ', end='')
    print(str(suma_armonica))



# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 07: Suma armonica (recursividad)')
        print('----------------------------------------------------------\n')
        numero = int(input('Ingrese un numero: '))

        suma = round(suma_armonica(numero), 4)
        imprimir_problema(numero, suma)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False