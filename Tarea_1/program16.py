# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Obtener la lista de números narcisistas que existan 
en un intervalo dado por el usuario

Fuente: https://mathworld.wolfram.com/NarcissisticNumber.html
---------------------------------------------------------------
'''

def verificar_si_es_narcisista(num:int) -> bool:
    
    num_str = str(num)
    suma_de_cubos = 0
    
    # Un número es narcisista cuando la suma de los cubos de cada uno de los digitos es igual al mismo numero.
    # Ejemplo: 407 = 4^3 + 0^3 + 7^3
    for i in num_str:
        suma_de_cubos += (int(i) ** 3)
    
    if num == suma_de_cubos:
        return True
    else:
        return False
    
print(verificar_si_es_narcisista(153))