# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

------------------------------------------------
Problema: Suma digitos

Ejemplo: Si se ingresa N = 1521, el resultado a 
mostrar es: Suma = 1 + 5 + 2 + 1 = 9
------------------------------------------------
'''

def suma_digitos(num:int):
    num = str(num)
    digitos = []
    suma = 0

    for i in num:
        suma = suma + int(i)
        digitos.append(i)
    
    print(suma)
    print(digitos)

suma_digitos(456)