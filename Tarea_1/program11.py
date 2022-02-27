# -*- coding: utf-8 -*-
'''
Fecha de creación: 18/02/2022
autor: PakoMtz 

------------------------------------------------------------------------
Problema: Calcular el dígito de control del código de barras EAN-8

Fuente: https://www.dropbox.com/s/jkl97z04rkepmdz/Ejercicio.docx?dl=0
------------------------------------------------------------------------
'''

# Para entender mejor el algoritmo, consulte el link en donde se explica mejor los pasos
def generar_numero_control(codigo:int) -> int:
    
    codigo_str = str(codigo)
    numero = 0
    acumuladorPar = 0
    acumuladorImpar = 0
    numeroControl = 0

    for i, value in enumerate(codigo_str):
        
        numero = int(value)

        if i % 2 != 0:
            acumuladorImpar += numero
        else:
            acumuladorPar += numero
    
    acumuladorImpar *= 3
    numeroControl = 10 - ((acumuladorImpar + acumuladorPar) % 10)

    return numeroControl

x = generar_numero_control(12345678)
print(x)