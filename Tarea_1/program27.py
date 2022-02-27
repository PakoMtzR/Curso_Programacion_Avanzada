# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: Verificar si una palabra o frase es palindromo
----------------------------------------------------------
'''

def palindromo(frase:str) -> bool:

    # Quitamos los espacios que pueda tener la frase (si es palabra entonces no le hara cambios)
    frase_sin_espacios = frase.replace(' ', '').lower() 
    
    # Comparamos si la frase se lee igual de izquierda a derecha que de derecha a izquierda
    if frase_sin_espacios == frase_sin_espacios[::-1]:
        return True
    else:
        return False


x = palindromo('Sé verlas al revés')
print(x)