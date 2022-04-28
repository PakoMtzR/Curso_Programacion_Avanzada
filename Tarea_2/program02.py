'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema:

Fuentes: 
---------------------------------------------------------------
'''
import matplotlib.pyplot as plt # Importar módulo para graficación
import numpy as np  # Importar módulo para el uso de arreglos numéricos
import sympy as sp  # Importar módulo para el uso de matemáticas simbólicas


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
x_n = valor_inicial

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
        y_diff_xn = float(y_diff.subs(x, x_n).evalf()) # f'(xi)
        archivo.write(f'{ciclo} | {x_n} | {y_diff_xn}')
        ciclo += 1
        if (y_diff_xn >= -1*error_permisible) and (y_diff_xn <= error_permisible):
            break
        else:
            x_n = x_n - (float(y.subs(x,x_n).evalf())/float(y_diff.subs(x,x_n).evalf()))


x_valores = np.arange(x_n - 1, valor_inicial, 0.1)  # Creamos un arreglo de valores en x para evaluarlos es la funcion
y_valores = [float(y.subs(x,tmp).evalf()) for tmp in x_valores] # Evaluamos los valores de x en la funcion

# Graficamos
plt.plot(x_valores, y_valores)
plt.title('f(' + variable + ') = ' + str(y))
plt.xlabel(variable)
plt.ylabel('f(' + variable + ')')
plt.scatter(x_n, float(y.subs(x,x_n).evalf()), color = 'red')    # Punto raiz de la funcion f(x) = 0
plt.text(0.2, 0.2, f'({round(float(y.subs(x,x_n).evalf()), 4)}, {round(x_n,4)})', fontsize=10)
plt.grid()
plt.show()