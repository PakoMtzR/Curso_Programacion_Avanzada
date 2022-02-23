# -*- coding: utf-8 -*-
'''
Fecha de creación: 17/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema:  Desarrollar un programa que permita ingresar una 
frase solo texto y espacios de no más de 100 caracteres y que 
imprima la frase en cada línea eliminando los espacios, 
de la siguiente forma:

La frase que se ingreso tiene menos de cien caracteres
La frase que se ingreso tiene menos de cien
La frase que se ingreso tiene menos de
La frase que se ingreso tiene menos
La frase que se ingreso tiene
La frase que se ingreso
La frase que se
La frase que
La frase
La
---------------------------------------------------------------
'''

# hay que mejorarla
def otra_funcion_rara(cadena:str):
    lista = cadena.split(' ')
    for i in range(len(lista)):
        for j in range(len(lista)-i):
            print(lista[j], end=' ')
        print('\n')

'''
def otra_funcion_rara(cadena:str):
    lista = cadena.split(' ')
    for i, value in enumerate(lista):
'''
    

otra_funcion_rara('La frase que se ingreso tiene menos de cien caracteres')