# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

-------------------------------------------------------------
Problema: Almacenar en una lista las letras del abecedario, 
elimine de la lista las letras que ocupen las posiciones 
múltiplos de 3 y muestre en pantalla ambas listas, 
la original y la resultante 
-------------------------------------------------------------
'''
from os import system

def cosa_rara() -> None:

    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    # Guardamos una copia del abecedario excluyendo los valores que ocupen las posiciones múltiplos de 3
    abecedario_copia = [val for i, val in enumerate(abecedario) if (i+1)%3 != 0]
    
    # Guardamos el abecedario original como una lista
    abecedario = list(abecedario)
    
    print(f'    Original --> {abecedario}')
    print(f'  Resultante --> {abecedario_copia}')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
system('cls')   # Limpiamos la consola

print('------------------------------------------------------------------')
print(' Programa 12: Almacenar en una lista las letras del abecedario,') 
print('              elimine de la lista las letras que ocupen las ')
print('              posiciones múltiplos de 3 y muestre en pantalla ')
print('              ambas listas, la original y la resultante')
print('------------------------------------------------------------------\n')

cosa_rara()