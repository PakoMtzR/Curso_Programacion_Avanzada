# -*- coding: utf-8 -*-
'''
Fecha de creación: 18/02/2022
autor: PakoMtz 

------------------------------------------------------------------------
Problema: Calcular el dígito de control del código de barras EAN-8

Fuente: https://www.dropbox.com/s/jkl97z04rkepmdz/Ejercicio.docx?dl=0
------------------------------------------------------------------------
'''
from os import system
import preguntar

# Para entender mejor el algoritmo, consulte el link en donde se explica mejor los pasos
def generar_numero_control(codigo:int) -> int:
    
    if codigo < 0: codigo *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo
    
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


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 11: Calcular el dígito de control del código ')
        print('              de barras EAN-8')
        print('----------------------------------------------------------------\n')
        codigo = int(input(' Ingresa el codigo: '))
        print('\n')

        num_control = generar_numero_control(codigo)
        print(f'\t{codigo} {num_control} <-- # de control')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un numero entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()
'''
x = generar_numero_control(12345678)    # --> 4
print(x)
'''
