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

def convertir_a_romano(num:int) -> str:

    # Definomos los numeros con sus respectivos numerales romanos
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


print(convertir_a_romano(123)) # 'CXXIII'