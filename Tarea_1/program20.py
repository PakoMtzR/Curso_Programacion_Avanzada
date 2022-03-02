# -*- coding: utf-8 -*-
'''
Fecha de creación: 01/03/2022
autor: PakoMtz 

---------------------------------------------
Problema: Cálculo del valor de π/4 por 
medio de una fracción continua

Fuente: https://wikimedia.org/api/rest_v1/media/math/render/svg/3268a8c94ade49b8caa85c430ea369e3c25def21
---------------------------------------------
'''
from os import system
import preguntar


# Calculamos el valor de pi con ayuda de la fracción continua
def calcular_pi(n:int) -> float:

    impares = [num for num in range(n*2) if num%2 != 0][::-1]   # Creamos una lista de n números impares y la invertimos
    cuadrados = [num**2 for num in range(1, n)][::-1]           # Creamos una lista de n-1 números cuadrados y la invertimos
    cuadrados.append(1)                                         # Agregamos un 1 al final de la lista de cuadrados  
    
    # Calculamos el valor de pi/4 mediante el uso de la fracción continua
    fraccion_continua = 0
    for i in range(n):
        fraccion_continua = cuadrados[i] / (impares[i] + fraccion_continua)

    return fraccion_continua*4  # Retornamos el valor de pi
    

# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 20: Obtener un valor aproximado de π con uso de la')
        print('              fracción continua')
        print('----------------------------------------------------------------\n')
        bucles = int(input(' Ingrese la cantidad de bucles: '))
        print('\n')

        if bucles < 0: bucles *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo

        pi_aprox = calcular_pi(bucles)
        print(f'\t π(aprox) = {pi_aprox}')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un numero entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()