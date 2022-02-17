'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------
Problema: Descomponer un numero en unidades, decenas, centenas, ...
---------------------------------------------
'''

def descomponer(num):
    num = str(num)
    factores = []

    for i in range(len(num)):
        factores.append(int(num[i])*(10**(len(num)-(i+1))))

    print(factores)

descomponer(3580)