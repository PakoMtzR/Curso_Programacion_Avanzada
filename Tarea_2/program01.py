'''
# -*- coding: utf-8 -*-
Fecha de creacion: 28/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita ingresar una función f(x) cualquiera 
y mediante el Método de bisección obtener una de las raíces de la función, 
por lo que en primer lugar se debe mostrar al usuario una gráfica 
que permita inducir el intervalo de valores [a, b] que debe ingresarse. 
El programa también debe mostrar y guardar en un archivo de texto (.txt) 
la tabla con los siguientes valores: |i a b xi	ε|, donde i es el número de iteración, 
a y b son los valores del intervalo, xi es el valor de la raíz calculado y ε el error. 
Finalmente se debe mostrar el valor de la raíz y la gráfica de la vecindad donde 
se localiza la raíz.

Fuentes: https://es.wikipedia.org/wiki/M%C3%A9todo_de_bisecci%C3%B3n
---------------------------------------------------------------
'''
import matplotlib.pyplot as plt # Importar módulo para graficación
import numpy as np  # Importar módulo para el uso de arreglos numéricos
import sympy as sp  # Importar módulo para el uso de matemáticas simbólicas


# Ingresa la variable y verificamos si es correcta
while True:
    variable = input('Ingrese la variable: ')
    if (' ' in variable) == False: break

# Ingresa la ecuacion en bruto
ecuacion_bruto = input('Ingrese la ecuacion: ')

# Ingresa y verifica los valores de los limites
while True:
    limite_a = int(input('Ingrese el limite inferior (a): '))
    limite_b = int(input('Ingrese el limite superior (b): '))
    if limite_a > limite_b:
        print(' El limite b debe ser mayor al limite a, intentelo nuevamente.')
    else: break

# Se establece el nivel de presicion y se determina el error permisible
presicion = int(input('Ingrese los digitos de presicion: '))
error_permisible = (1/(10**presicion))

x = sp.Symbol(variable)         # Convertimos la variable en un simbolo
y = sp.simplify(ecuacion_bruto) # Convestimos la ecuacion en algo mas chido

x_valores = np.arange(limite_a, limite_b, 0.1)  # Creamos un arreglo de valores en x para evaluarlos es la funcion
y_valores = [float(y.subs(x,tmp).evalf()) for tmp in x_valores] # Evaluamos los valores de x en la funcion

# Creamos un archivo donde guardaremos los datos de cada iteracion
with open('program01_biseccion.txt', 'w') as archivo:
    
    # Colocar el encabezado del archivo
    archivo.write(
        f'''
    Metodo de Biseccion
-------------------------------------------------
Ecuacion: {ecuacion_bruto}
Intervalo de busqueda: [{limite_a}, {limite_b}]
Presicion: {presicion}
-------------------------------------------------
 # ciclo | limite a | limite b | raiz\n
'''
    )

    # Metodo de biseccion
    ciclo = 1
    while True:
        punto_medio_x = (limite_a + limite_b)/2         # m
        punto_medio_y = y.subs(x,punto_medio_x).evalf() # f(m)

        archivo.write(f' {ciclo} | {limite_a} | {limite_b} | {punto_medio_y}\n')
        ciclo += 1

        if (punto_medio_y >= -1*error_permisible) and (punto_medio_y <= error_permisible):
            break
        else:
            limite_a_y = y.subs(x,limite_a).evalf()     # f(a)
            limite_b_y = y.subs(x,limite_b).evalf()     # f(b)
            
            if limite_a_y*punto_medio_y > 0:            # f(a)*f(m) > 0, entonces a = m_x
                limite_a = punto_medio_x
            else: pass

            if limite_b_y*punto_medio_y > 0:            # f(b)*f(m) > 0, entonces b = m_x
                limite_b = punto_medio_x
            else: pass

# Graficamos
plt.plot(x_valores, y_valores)
plt.title('f(' + variable + ') = ' + str(y))
plt.xlabel(variable)
plt.ylabel('f(' + variable + ')')
plt.scatter(punto_medio_x, punto_medio_y, color = 'red')    # Punto raiz de la funcion f(x) = 0
plt.text(0.2, 0.2, f'({round(punto_medio_y, 4)}, {round(punto_medio_x,4)})', fontsize=10)
plt.grid()
plt.show()



