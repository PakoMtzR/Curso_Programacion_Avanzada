# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: Verificar si una palabra o frase es palindromo
----------------------------------------------------------
'''

def palindromo(cadena:str):
    x = cadena.replace(' ', '').lower()
    if x == x[::-1]:
        return True
    else:
        return False


x = palindromo('Sé verlas al revés')
print(x)