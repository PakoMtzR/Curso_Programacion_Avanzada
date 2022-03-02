# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

----------------------------------------------------------------------------
Problema: Generar un triángulo de Pascal

Fuente: https://www.estadisticaparatodos.es/taller/triangulo/triangulo.html
----------------------------------------------------------------------------
'''
from os import system
import preguntar

# Función para calcular el factorial de un número
def factorial(num:int) -> int:
    factorial = 1
    if num != 0:
        for i in range(num):
            factorial *= (i+1)
        return factorial
    else:
        return factorial

# Función para calcular la combinatoria de dos numeros    
def combinatoria(a:int, b:int) -> int:
    return factorial(a) // (factorial(b) * factorial(a-b))

# Función para imprimir el triángulo de Pascal
def triangulo_pascal(num:int) -> None:

    if num < 0: num *= -1   # Si el número que ingreso es negativo, lo convertimos a positivo

    for i in range(num):
        for k in range(i+1):
            print(combinatoria(i, k), end=' ')
        print('\n')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('-----------------------------------------------------')
        print(' Programa 5: Generar Triangulo de Pascal')
        print('-----------------------------------------------------\n')
        niveles = int(input(' Ingrese el número de niveles: '))
        print('\n')

        triangulo_pascal(niveles)   # Imprimimos el triangulo de pascal

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un número entero!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()