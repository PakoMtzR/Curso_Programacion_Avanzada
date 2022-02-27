# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Programa que obtenga el Máximo Común Divisor (MCD) 
y el mínimo común múltiplo (mcm) de un par de números enteros 
positivos. (Existe un algoritmo ya establecido para este caso, 
se le conoce como algoritmo de Euclídes).
---------------------------------------------------------------
'''

# Falta mejorar unos detalles
def obtener_mcm_y_mcd(numA:int, numB:int) -> None:
    
    residuo = 1

    # Verificamos casos triviales
    if ((numA == 0) & (numB == 0)):
        mcd = 0
    elif numA == 0:
        mcd = numB
    elif numB == 0:
        mcd = numA
    
    # Caso no trivial
    else:
        # Buscamos que numA > numB
        if numA < numB:
            numA, numB = numB, numA     
        
        # Creamos unas copias de los números
        numA_copia = numA
        numB_copia = numB

        # Calculamos el mcd
        while residuo != 0:
            residuo = numA_copia % numB_copia
            mcd, numA_copia, numB_copia = numB_copia, numB_copia, residuo
        
    # Calculamos el mcm
    mcm = (numA * numB)//mcd

    print(f'mcm = {mcm} \nmcd = {mcd}')



obtener_mcm_y_mcd(0,0)