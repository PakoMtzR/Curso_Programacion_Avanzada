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

from os import system
import preguntar


def contar_palabras(texto:str) -> None:

    # Creamos una variable el cual contenga todas las letras del abecedario
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    contador = 0    # Creamos un contador para guardar el número de veces que 
                    # aparece una palabra en el texto.

    #print(texto)    # Imprimimos el texto original

    # Recoremos cada letra del abecedario
    for letra_abecedario in abecedario:

        contador = 0    # Limpiamos el contador

        # Recoremos cada letra que exista en el texto
        for letra_texto in texto:
            # Si la letra del abecedario coincide con una letra del texto, el contador incrementa 1
            if letra_texto == letra_abecedario:
                contador += 1
        
        # Imprimimos las veces que aparece una letra del abecedario en el texto
        if contador != 0:
            print(f'\t{letra_abecedario} -> {contador}')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 25: Contar la frecuencia de cada letra del')
        print('              alfabeto latino dentro de un texto')
        print('----------------------------------------------------------\n')
        texto = input(' Ingrese el testo: ')
        print('\n')

        contar_palabras(texto)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un texto')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

#contar_palabras('hola soy pakito y no hare travesuras jsjsjsjsjs')