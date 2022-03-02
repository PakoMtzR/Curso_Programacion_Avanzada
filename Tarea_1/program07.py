# -*- coding: utf-8 -*-
'''
Fecha de creación: 28/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: ingresar un intervalo mediante dos números 
enteros y positivos [a,b] y que obtenga tanto la suma 
como el producto de todos los números intermedios, 
incluyendo a & b
----------------------------------------------------------
'''

from os import system
import preguntar


def suma_de_numeros_intermedios(lim_a:int, lim_b:int) -> int:
    suma_de_intermedios = 0     # Creamos una variable donde guardaremos la suma
    
    # Recordar que range() genera un intervalo [a,b) <-- no toca el valor b, por esa razón aumentamos 1.
    for i in range(lim_a, lim_b + 1):
        suma_de_intermedios += i
    
    return suma_de_intermedios  # Retornamos la suma total de todos los números intermedios
    

def producto_de_numeros_intermedios(lim_a:int, lim_b:int) -> int:
    producto_de_intermedios = 1     # Creamos una variable donde guardaremos el producto

    for i in range(lim_a, lim_b + 1):
        producto_de_intermedios *= i
    
    return producto_de_intermedios  # Retornamos el producto de todos los números intermedios


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 7: Ingresar un intervalo [a,b] y que obtenga tanto') 
        print('             la suma como el producto de todos los números ')
        print('             intermedios, incluyendo a & b')
        print('----------------------------------------------------------\n')
        a = int(input(' Ingrese el valor inicial: '))
        b = int(input(' Ingrese el valor final: '))
        print('\n')

        suma = suma_de_numeros_intermedios(a, b)
        producto = producto_de_numeros_intermedios(a, b)

        print(f' La suma de los números en el intervalo de [{str(a)}, {str(b)}] = {suma}')
        print(f' El producto de los números en el intervalo de [{str(a)}, {str(b)}] = {producto}')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()