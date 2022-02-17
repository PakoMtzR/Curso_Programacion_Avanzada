'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Invertir un numero
---------------------------------------------
'''

def invertir(num):
    num = str(num)
    aux = ''
    for i in range(len(num)):
        aux = aux + num[-1-i]
    num = aux
    print(num)

invertir(812)