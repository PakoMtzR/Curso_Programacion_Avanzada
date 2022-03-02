# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: Verificar si una palabra o frase es palindromo
----------------------------------------------------------
'''

from os import system
import preguntar


def palindromo(frase:str) -> bool:

    # Quitamos los espacios que pueda tener la frase (si es palabra entonces no le hara cambios)
    frase_sin_espacios = frase.replace(' ', '').lower() 
    
    # Comparamos si la frase se lee igual de izquierda a derecha que de derecha a izquierda
    if frase_sin_espacios == frase_sin_espacios[::-1]:
        return True
    else:
        return False


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 27: Verificar Palindromo')
        print('----------------------------------------------------------\n')
        frase = input(' Ingrese una frase o palabra: ')
        print('\n')

        if palindromo(frase) == True:
            print(f' {frase} --> Es un palindromo')
        else:
            print(f' {frase} --> NO es un palindromo')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un texto')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False
'''
x = palindromo('Sé verlas al revés')
print(x)
'''
