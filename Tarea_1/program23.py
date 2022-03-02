# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

--------------------------------------------------------
Problema: Generar un programa que permita ingresar una 
frase y también solicite la forma de ordenarla, 
alfabéticamente directa o inversa.
--------------------------------------------------------
'''
from os import system
import preguntar


def ordenar_alfabeticamente_directa(frase:str) -> list:
    palabras = frase.split()    # Separa las palabras de la frase y los guarda en una lista
    palabras.sort()             # Ordena las palabras de la lista en orden alfabetico
    return palabras             # Retorna una lista con las palabras de la frase ordenadas conforme el alfabeto

def ordenar_alfabeticamente_inversa(frase:str) -> list:
    # Primero ordenamos la lista de manera directa con ayuda de la funcion anterior
    # luego, le revertimos con la funcion reversed() y lo guardamos en la lista 'palabras'
    palabras = [palabra for palabra in reversed(ordenar_alfabeticamente_directa(frase))]
    return palabras     # Retorna una lista con las palabras de la frase ordenadas conforme el alfabeto de manera inversa


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('---------------------------------------------------------------------')
        print(' Programa 23: Ordenar una frase alfabéticamente directa o inversa ')
        print('---------------------------------------------------------------------\n')
        frase = input(' Ingrese la frase: ')
        print('---------------------------------------------------------------------')
        print(' 1) Ordenarla de forma DIRECTA')
        print(' 2) Ordenarla de forma INVERSA\n')
        forma_de_ordenarla = int(input(' Escriba la opcion: '))
        print('\n')

        if forma_de_ordenarla == 1:
            palabras = ordenar_alfabeticamente_directa(frase)
        elif forma_de_ordenarla == 2:
            palabras = ordenar_alfabeticamente_inversa(frase)
        else:
            pass

        for i in palabras:
            print(f'\t - {i}')
        
    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo()    

'''
frase = 'hola soy pakito y no hare travesuras'
x = ordenar_alfabeticamente_directa(frase)
y = ordenar_alfabeticamente_inversa(frase)
print(x)
print(y)
'''



