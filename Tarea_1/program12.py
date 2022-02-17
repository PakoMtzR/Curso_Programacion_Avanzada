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

def cosa_rara():
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    abecedario_copia = [val for i, val in enumerate(abecedario) if (i+1)%3 != 0]
    abecedario = list(abecedario)
    print(abecedario)
    print(abecedario_copia)


cosa_rara()