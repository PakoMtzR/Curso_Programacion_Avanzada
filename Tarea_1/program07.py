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

x = suma_de_numeros_intermedios(4,6)
y = producto_de_numeros_intermedios(4,6)

print(x)
print(y)