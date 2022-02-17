# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

-----------------------------------------------------
Problema: Evaluar si un año es bisiesto

Un año es bisiesto si es múltiplo de 4, exceptuando 
los múltiplos de 100, que sólo son bisiestos cuando 
son múltiplos además de 400, por ejemplo el año 1900 
no fue bisiesto, pero el año 2000 si lo es. 
-----------------------------------------------------
'''

def bisiesto(year:int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False

x = bisiesto(2000)
print(x)