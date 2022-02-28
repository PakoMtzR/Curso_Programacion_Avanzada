# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

----------------------------------------------------------
Problema: Desarrollar un programa que permita el ingreso 
de números por parte del usuario (dejar que ingrese un 
número indefinido de números y en cada uno de ellos 
preguntar si se desea agregar más o ya es el último a 
agregar), guardarlos en una lista y mostrar en pantalla, 
el número de datos ingresados, el promedio, y la desviación 
estándar de los datos.
----------------------------------------------------------
'''


# Esta función recibe una lista de datos y con base a ella, determina:
# 1) La cantidad de datos ingresados
# 2) El promedio
# 3) La desviacion estandar
def analisis_de_datos(lista_de_datos:list) -> None:
    
    numero_de_datos = len(lista_de_datos)    # Determina la cantidad de datos ingresados
    
    # Calculamos el promedio
    suma_de_datos = 0
    for dato in lista_de_datos:
        suma_de_datos += dato
    
    promedio = suma_de_datos / numero_de_datos

    # Calculamos la desviacion estandar
    suma_desviaciones = 0
    for dato in lista_de_datos:
        suma_desviaciones += (dato - promedio)**2
    
    desviacion_estandar = round((suma_desviaciones / (numero_de_datos - 1)) ** 0.5, 3)

    # Imprimimos los calculos obtenidos
    print(lista_de_datos)
    print(f' Datos ingresados -> {numero_de_datos}')
    print(f' Promedio = {promedio}')
    print(f' Desviacion estandar = {desviacion_estandar}')


analisis_de_datos([5,15,12,18,28])