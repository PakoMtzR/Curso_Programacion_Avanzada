'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita ingresar una función f(x) cualquiera 
y mediante el Método de Newton-Raphson obtener una de las raíces 
de la función, por lo que en primer lugar se debe mostrar al 
usuario una gráfica que permita inducir el valor incial x0 que debe ingresarse. 
El programa también debe mostrar y guardar en un archivo de texto (.txt) la 
tabla con los siguientes valores: |i xi	ε|, donde i es el número de iteración, 
xi es el valor de la raíz calculado y ε el error. Finalmente se debe mostrar 
el valor de la raíz y la gráfica de la vecindad donde se localiza la raíz.

Fuentes: https://es.wikipedia.org/wiki/M%C3%A9todo_de_Newton
---------------------------------------------------------------
'''
import matplotlib.pyplot as plt # Importar módulo para graficación
import numpy as np  # Importar módulo para el uso de arreglos numéricos
import sympy as sp  # Importar módulo para el uso de matemáticas simbólicas


print('----------------------------------------------------------')
print(' Programa 02: Metodo de Newton-Raphson')
print('----------------------------------------------------------\n')

# Ingresa la variable y verificamos si es correcta
while True:
    variable = input('Ingrese la variable: ')
    if (' ' in variable) == False: break

ecuacion_bruto = input('Ingrese la ecuacion: ')                 # Ingresa la ecuacion en bruto
valor_inicial = int(input('Ingresa un valor inicial (x0): '))   # Ingresa un valor inicial

# Se establece el nivel de presicion y se determina el error permisible
presicion = int(input('Ingrese los digitos de presicion: '))
error_permisible = (1/(10**presicion))

x = sp.Symbol(variable)         # Convertimos la variable en un simbolo
y = sp.simplify(ecuacion_bruto) # Convestimos la ecuacion en algo mas chido f(x)
y_diff = sp.diff(y,x)           # f'(x)
xn = valor_inicial

# Creamos un archivo donde guardaremos los datos de cada iteracion
with open('program02_newton.txt', 'w') as archivo:
    
    # Colocar el encabezado del archivo
    archivo.write(
        f'''
    Metodo de Newton-Raphson
-------------------------------------------------
Ecuacion: {ecuacion_bruto}
Valor inicial (x0): {valor_inicial}
Presicion: {presicion}
-------------------------------------------------
 # ciclo | x_n | f'(x_n)\n
'''
    )

    # Metodo de Newton-Raphson
    ciclo = 1
    while True:
        y_diff_xn = float(y_diff.subs(x, xn).evalf()) # f'(xi)
        y_xn = float(y.subs(x, xn).evalf())

        archivo.write(f'{ciclo} | {xn} | {y_diff_xn}\n')
        ciclo += 1
        if (y_diff_xn >= -1*error_permisible) and (y_diff_xn <= error_permisible):
            break
        else:
            xn = xn - (y_xn/y_diff_xn)

# Definimos los limites de la funcion para poder graficarlo
if xn > valor_inicial:
    limite_a, limite_b = valor_inicial, xn
else:
    limite_a, limite_b =  xn, valor_inicial

# Generamos los x y y valores para poder graficar la funcion
x_valores = np.arange(limite_a - 1, limite_b, 0.1)  # Creamos un arreglo de valores en x para evaluarlos es la funcion
y_valores = [float(y.subs(x,tmp).evalf()) for tmp in x_valores] # Evaluamos los valores de x en la funcion

# Graficamos
plt.plot(x_valores, y_valores)
plt.title('f(' + variable + ') = ' + str(y))
plt.xlabel(variable)
plt.ylabel('f(' + variable + ')')
plt.scatter(xn, y_xn, color = 'red')    # Punto raiz de la funcion f(x) = 0
plt.text(0.2, 0.2, f'({round(y_xn), 4}, {round(xn,4)})', fontsize=10)
plt.grid()
plt.show()