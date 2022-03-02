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
from os import system
import preguntar


# Criba de Sundaram
# i, j E Naturales
# 1 <= i <= j
# i + j + 2ij <= lim
def criba_sundaram(lim:int) -> list:
	
    # Creamos una lista de números naturales que se encuentran en el intervalo de 1 al limite dado [1, lim]
    lista_numeros = [num for num in range(1, lim + 1)]
    
    # Creamos una lista donde guardaremos los numeros primos
    numeros_primos = []
    
    # Condiciones Iniciales
    i = 1; j = 1

    # Generamos la base para generar numeros primos (eliminamos candidatos no posibles)
    for i in range(1, (lim-j)//(1+2*j)):
        for j in range(1, (lim-i)//(1+2*i)):
            numero_a_eliminar = i + j + (2*i*j)
            if numero_a_eliminar in lista_numeros:
                lista_numeros.remove(numero_a_eliminar)
        j = i + 1

    # Generacion de numeros primos
    # 2n + 1 --> Donde n es un elemento en la Lista Base de Numeros Primos
    # Si el resultado es menor al limite dado, lo guardamos en la lista de numeros primos
    for i in lista_numeros:
        numero_primo = (2*i) + 1
        if numero_primo <= lim:
            numeros_primos.append(numero_primo)
    
    return numeros_primos


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 22: Obtener los números primos con el uso de la')
        print('              Criba de Sundaram')
        print('----------------------------------------------------------------\n')
        limite = int(input(' Obtener número primos inferiores a: '))
        print('\n')

        primos = criba_sundaram(limite)
        print(f' Existen {len(primos)} numeros primos entre 3 y {limite}:\n\t')
        for i in primos:
            print(f' {str(i)}', end='')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un numero entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()

'''
n = int(input(' Ingrese el limite: '))
x = criba_sundaram(n)
print(f' Existen {len(x)} numeros primos entre 3 y {n}')
print(x)
'''