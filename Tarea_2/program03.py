'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita ingresar una función f(x) polinomial 
cualquiera y mediante el Método de Lin-Bairstow obtener todas las 
ráices de la función polinomial una de las raíces de la función, 
por lo que en primer lugar se deben introducir los valores r0 y s0 
que debe ingresarse. El programa también debe mostrar y guardar 
en un archivo de texto (.txt) la tabla con los siguientes valores: 
|i ri	si	εr	εs|, donde i es el número de iteración, factores ri y si y 
los errores de los factores εr εs

Fuentes: 
---------------------------------------------------------------
'''

import matplotlib.pyplot as plt # Importar módulo para graficación
import numpy as np  # Importar módulo para el uso de arreglos numéricos
import sympy as sp  # Importar módulo para el uso de matemáticas simbólicas


print('----------------------------------------------------------')
print(' Programa 03: Metodo de Lin-Bairstow')
print('----------------------------------------------------------\n')