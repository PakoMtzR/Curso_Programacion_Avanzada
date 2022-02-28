# -*- coding: utf-8 -*-
'''
Fecha de creación: 28/02/2022
autor: PakoMtz 

---------------------------------------------------------------------
Problema: Programa que permita obtener los números primos inferiores 
a un número entero positivo N proporcionado por el usuario, en donde 
N es un número entero positivo, el cual ingresa el usuario, esto es 
si N = 20, el programa debe desplegar la lista 2,3,5,7,11,13,17,19. 
El programa debe seguir el algoritmo propuesto por el 
matemático S.P. Sundaram

Fuente:
http://www.grupoalquerque.es/mate_cerca/paneles_2017/286_Criba_de_Sundaram.pdf
---------------------------------------------------------------------
'''
def criba_sundaram(lim:int) -> list:

    # Creamos una lista de números que se encuentran en el intervalo [1, lim]
    numeros = [num for num in range(1, lim + 1)]
    numeros_primos = []
    #print(numeros)
    i = 1
    j = 1
    tolerancia = 2
    
    while True:

        numero_a_quitar = i + j + (2*i*j)
        
        if numero_a_quitar in numeros:
            numeros.remove(numero_a_quitar)
            #print(numeros)
            j += 1
            #tolerancia += 1

        else:
            tolerancia -= 1
                   
            if tolerancia == 0:
                break
            else:
                i += 1
                j = i  

    for i in numeros:
        numero_primo = (2*i) + 1
        if numero_primo <= lim:
            numeros_primos.append(numero_primo)

    return numeros_primos


n = int(input(' Ingrese el limite: '))
x = criba_sundaram(n)
print(f' Existen {len(x)} numeros primos entre 3 y {n}')
print(x)



'''
        if numero_a_quitar > lim:
            #j_lim = j
            i += 1
            j = i
            numero_a_quitar = i + j + (2*i*j)
            #if j_lim == i:
            #    break
            if numero_a_quitar > lim:
                break
        else:
            if numero_a_quitar in numeros:
                numeros.remove(numero_a_quitar)
                print(numeros)
        j += 1
        '''