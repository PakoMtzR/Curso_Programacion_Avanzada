# -*- coding: utf-8 -*-
'''
Fecha de creación: 22/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: ingresar un intervalo mediante dos números 
enteros y positivos [a,b] y que obtenga tanto la suma 
como el producto de todos los números intermedios, 
incluyendo a & b
----------------------------------------------------------
'''

# No esta completo
def suma_intermedios(num_a:int, num_b:int) -> None:
    suma = 0

    if (num_b - num_a) % 2 == 0:
        suma = 2*num_a + 2*((num_b - num_a) // 2)
        print(suma)
    else:
        print('no se puede')
    '''
    for i in range(3,10,2):
        print(i)
    '''
    
suma_intermedios(0,10)

