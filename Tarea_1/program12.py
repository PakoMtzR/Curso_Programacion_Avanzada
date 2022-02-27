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

def cosa_rara() -> None:

    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    # Guardamos una copia del abecedario excluyendo los valores que ocupen las posiciones múltiplos de 3
    abecedario_copia = [val for i, val in enumerate(abecedario) if (i+1)%3 != 0]
    
    # Guardamos el abecedario original como una lista
    abecedario = list(abecedario)
    
    print(abecedario)
    print(abecedario_copia)


cosa_rara()