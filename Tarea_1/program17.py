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

def verificar_si_es_numero_keith(num:int) -> bool:

    # Guardamos los digitos del número en un a lista
    digitos = [int(i) for i in str(num)]

    suma_digitos = 0

    while suma_digitos < num:
        # Sumamos los digitos del número    
        suma_digitos = 0    # Limpiamos la variable suma  
        for i in digitos:
            suma_digitos += i

        # Desplazamos todos los valores de la lista un lugar a la izquierda, 
        # al ultimo valor de la lista le asignaremos el valor de la suma de los digitos del número
        for i, value in enumerate(digitos):
            if i == len(digitos) - 1:
                digitos[i] = suma_digitos
            else:
                digitos[i] = digitos[i+1]
             
    # Si al final, la suma de sus digitos llega a ser igual al numero inicial entonces es un número de Keith
    if suma_digitos == num:
        return True
    else:
        return False
    

print(verificar_si_es_numero_keith(197))