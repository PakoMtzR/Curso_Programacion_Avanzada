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

def suma_digitos(num:int) -> None:
    
    num_str = str(num)
    digitos = [i for i in num_str] # Guardamos los digitos del número en una lista <str>
    
    # Sumamos los digitos del numero
    suma_de_digitos = 0
    for i in num_str:
        suma_de_digitos += int(i)
    
    print(suma_de_digitos)
    print(digitos)

suma_digitos(456)