# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

------------------------------------------------------------------------
Problema: Desarrollar un programa que permita ingresar cualquier tipo 
de texto y que cuente la frecuencia de aparición de cada letra del 
alfabeto latino, esto el número de cuántas a, b, c, d, ... hay en 
el texto ingresado.
------------------------------------------------------------------------
'''

def contar_palabras(texto:str) -> None:

    # Creamos una variable el cual contenga todas las letras del abecedario
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    contador = 0    # Creamos un contador para guardar el número de veces que 
                    # aparece una palabra en el texto.

    print(texto)    # Imprimimos el texto original

    # Recoremos cada letra del abecedario
    for letra_abecedario in abecedario:

        contador = 0    # Limpiamos el contador
        
        # Recoremos cada letra que exista en el texto
        for letra_texto in texto:
            # Si la letra del abecedario coincide con una letra del texto, el contador incrementa 1
            if letra_texto == letra_abecedario:
                contador += 1
        
        # Imprimimos las veces que aparece una letra del abecedario en el texto
        print(f'{letra_abecedario} -> {contador}')


contar_palabras('hola soy pakito y no hare travesuras jsjsjsjsjs')