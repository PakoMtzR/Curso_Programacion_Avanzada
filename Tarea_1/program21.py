# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

---------------------------------------------------------------
Problema: Desarrollar un programa que muestre al usuario si un
 número entero positivo ingresado por el es un número feliz, 
 en caso de serlo mostrar el por que se trata de uno de ellos 
 (mostrar la relación de recurrencia que se muestra en la 
 página de referencia para el 7).

Fuente:
https://es.wikipedia.org/wiki/N%C3%BAmero_feliz
---------------------------------------------------------------
'''

def verificar_si_es_un_numero_feliz(num:int) -> bool:
    
    # Agregamos el primer número a la lista
    lista_numeros = [num]

    # Si se repite alguno de los elementos de la lista, interrumpimos el bucle
    while len(lista_numeros) == len(set(lista_numeros)):
            
        suma_de_cuadrados = 0   # Limpiamos la variable de la suma
        num_str = str(lista_numeros[-1])    # Guardamos el ultimo elemento de la lista y lo guardamos como <str>
        
        # Recorremos cada digito del ultimo elemento y sumamos sus cuadrados
        # Ejemplo: 49 --> 4² + 9² = 97 
        for i, value in enumerate(num_str):
            
            # Al principio no imprimiremos el simbolo ' + '
            if i != 0:
                print(' + ', end='')
            
            suma_de_cuadrados += (int(value)**2)
            print(f'{value}²', end='')
        
        # Imprimos al final la suma de los cuadrados de sus digitos
        print(f' = {suma_de_cuadrados}')

        # Agregamos la suma final a la lista de numeros
        lista_numeros.append(suma_de_cuadrados)
    
    # Si al final de todo el proceso el ultimo elemento de la lista de numeros es 1, 
    # entonces es un número feliz.
    if lista_numeros[-1] == 1:
        return True
    else:
        return False


x = verificar_si_es_un_numero_feliz(7) 
print(x)