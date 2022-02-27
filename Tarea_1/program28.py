# -*- coding: utf-8 -*-
'''
Fecha de creación: 22/02/2022
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

# No esta completo

def ingreso_de_datos() -> None:

    continuar = True
    datos = []
    
    while continuar == True:
        num = int(input('ingresa un numero: '))
        datos.append(num)

        opcion = input('deseas agregar otro numero? [y/n]: ').lower()
        
        if opcion == 'y':
            pass
        elif opcion == 'n':
            continuar = False
        else:
            opcion = input('deseas agregar otro numero? [y/n]: ').lower()
            
    print(datos)


ingreso_de_datos()