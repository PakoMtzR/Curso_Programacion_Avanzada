# -*- coding: utf-8 -*-
'''
Fecha de creación: 28/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Programa que obtenga el Máximo Común Divisor (MCD) 
y el mínimo común múltiplo (mcm) de un par de números enteros 
positivos. (Existe un algoritmo ya establecido para este caso, 
se le conoce como algoritmo de Euclídes).
---------------------------------------------------------------
'''
from os import system
import preguntar


def mcd(a:int, b:int) -> int:
    
    # Casos Triviales
    if a == 0 or b == 0:
        return 0

    # Buscamos que 'a' siempre sea mayor que 'b'
    if a <= b:
        a, b = b, a
    
    # Seguimos el algoritmo de Euclides hasta que el residuo sea 0
    residuo = a % b
    while residuo != 0:
        a, b = b, residuo
        residuo = a % b
    
    return b

def mcm(a:int, b:int) -> int:
    if a == 0 or b == 0:
        return 0
    else: 
        return (a*b)//mcd(a,b)


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------------')
        print(' Programa 15: Obtener el MCM y MCD de un par de números (a,b)')
        print('----------------------------------------------------------------\n')
        num_a = int(input(' Ingrese el valor de a: '))
        num_b = int(input(' Ingrese el valor de b: '))
        print('\n')

        minimo_comun_multiplo = mcm(num_a, num_b)
        maximo_comun_divisor = mcd(num_a, num_b)

        print(f'\t mcm = {minimo_comun_multiplo}\n\t mcd = {maximo_comun_divisor}')

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, tienes que ingresar un numero entero positivo!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()


'''
a = 1032
b = 180

print(mcd(a,b))
print(mcm(a,b)) 
'''