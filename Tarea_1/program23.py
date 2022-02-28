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

def ordenar_alfabeticamente_directa(frase:str) -> list:
    palabras = frase.split()    # Separa las palabras de la frase y los guarda en una lista
    palabras.sort()             # Ordena las palabras de la lista en orden alfabetico
    return palabras             # Retorna una lista con las palabras de la frase ordenadas conforme el alfabeto

def ordenar_alfabeticamente_inversa(frase:str) -> list:
    # Primero ordenamos la lista de manera directa con ayuda de la funcion anterior
    # luego, le revertimos con la funcion reversed() y lo guardamos en la lista 'palabras'
    palabras = [palabra for palabra in reversed(ordenar_alfabeticamente_directa(frase))]
    return palabras     # Retorna una lista con las palabras de la frase ordenadas conforme el alfabeto de manera inversa

frase = 'hola soy pakito y no hare travesuras'
x = ordenar_alfabeticamente_directa(frase)
y = ordenar_alfabeticamente_inversa(frase)
print(x)
print(y)


