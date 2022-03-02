# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Programa que al ingresar un número entero positivo 
en un intervalo de 1 a 3999, muestre su representación en 
números romanos.
---------------------------------------------------------------
'''

from os import system
import preguntar


def convertir_a_romano(num:int) -> str:
    # Definimos los numeros con sus respectivos numerales romanos
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral_romano = ''
    
    i = 0

    while num > 0:
        for _ in range(num // numeros[i]):
            numeral_romano += numerales[i]
            num -= numeros[i]

        i += 1
    
    return numeral_romano


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 27: Convetir número a Romano')
        print('----------------------------------------------------------\n')
        numero = int(input(' Ingrese un número: '))
        print('\n')

        if numero < 0: numero *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
        
        print(f' {str(numero)} --> {convertir_a_romano(numero)}')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

# print(convertir_a_romano(10)) # 'CXXIII'