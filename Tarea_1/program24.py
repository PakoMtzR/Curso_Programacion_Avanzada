# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema:  Desarrollar un programa que permita ingresar una 
frase solo texto y espacios de no más de 100 caracteres y que 
imprima la frase en cada línea eliminando los espacios, 
de la siguiente forma:

La frase que se ingreso tiene menos de cien caracteres
La frase que se ingreso tiene menos de cien
La frase que se ingreso tiene menos de
La frase que se ingreso tiene menos
La frase que se ingreso tiene
La frase que se ingreso
La frase que se
La frase que
La frase
La
---------------------------------------------------------------
'''

from os import system
import preguntar


# Hay que mejorarla porque mal documentado
def otra_funcion_rara(frase:str) -> None:

    # Separamos la frase mediante los espacios y los guardamos en una lista
    frase_lista = frase.split(' ')   

    for i in range(len(frase_lista)):
        for j in range(len(frase_lista)-i):
            print(frase_lista[j], end=' ')
        print('\n')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 24: Nosé como llamar a este programa, tu solo')
        print('              ingresa una frase y wacha')
        print('----------------------------------------------------------\n')
        frase = input(' Ingrese una frase: ')
        print('\n')

        otra_funcion_rara(frase)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar una frase')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

'''
def otra_funcion_rara(cadena:str):
    lista = cadena.split(' ')
    for i, value in enumerate(lista):
'''
#otra_funcion_rara('La frase que se ingreso tiene menos de cien caracteres')