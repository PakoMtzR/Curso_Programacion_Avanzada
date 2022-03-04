# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Programa que al recibir un número entero positivo N, 
permita obtener la lista de número de Keith.

Fuente: https://mathworld.wolfram.com/KeithNumber.html
---------------------------------------------------------------
'''
from os import system
import preguntar


def verificar_si_es_numero_keith(num:int) -> None:

    # Guardamos los digitos del número en un a lista
    digitos = [int(i) for i in str(num)]

    suma_digitos = 0

    while suma_digitos < num:
        # Sumamos los digitos del número    
        suma_digitos = 0    # Limpiamos la variable suma 
        print('\t',end='') 
        for index, value in enumerate(digitos):
            if index != 0:
                print(' + ', end='')
            print(str(value), end='')
            suma_digitos += value
        
        print(f' = {str(suma_digitos)}\n\n')

        # Desplazamos todos los valores de la lista un lugar a la izquierda, 
        # al ultimo valor de la lista le asignaremos el valor de la suma de los digitos del número
        for i, value in enumerate(digitos):
            if i == len(digitos) - 1:
                digitos[i] = suma_digitos
            else:
                digitos[i] = digitos[i+1]
             
    # Si al final, la suma de sus digitos llega a ser igual al numero inicial entonces es un número de Keith
    if suma_digitos == num:
        print(f'    {num} es un número de Keith')
    else:
        print(f'    {num} NO es un número de Keith')
    

# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 17: Números de Keith')
        print('----------------------------------------------------------\n')
        numero = int(input(' Ingrese un número: '))
        print('\n')

        verificar_si_es_numero_keith(numero)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False
