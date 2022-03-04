# -*- coding: utf-8 -*-
'''
Fecha de creación: 27/02/2022
autor: PakoMtz 

------------------------------------------------------------------------
Problema: Desarrollar un programa que permita ingresar cualquier tipo 
de texto y que lo encripte utilizando para ello la Encriptación o 
Cifrado César, por lo que se debe también solicitar cuántas posiciones 
se debe mover en el alfabeto para realizar la encriptación.

Fuente: https://www.youtube.com/watch?v=-PZSeh52n7A


Información Importante:
----------------------------------------------------------------------------------------
Para encriptar un mensaje se sigue la siguiente formula:
C = M + [k mod |A|]

donde:
C -> Es el caracter encriptado del mensaje
M -> Es el caracter del mensaje
k -> Es la llave (número entero)
A -> Es la cardinalidad de los caracteres con los que voy a trabajar (es la cantidad de caracteres disponibles o con los que vamos a trabajar)
        len(caracteres)

----------------------------------------------------------------------------------------
Para desencriptar un mensaje se sigue la siguiente formula:
M = C - [k mod |A|]

donde:
C -> Es el caracter encriptado del mensaje
M -> Es el caracter del mensaje
k -> Es la llave (número entero)
A -> Es la cardinalidad de los caracteres con los que voy a trabajar (es la cantidad de caracteres disponibles o con los que vamos a trabajar)
        len(caracteres)
----------------------------------------------------------------------------------------
'''
from os import system
import preguntar


# Definimos una variable global el cual contenga los caracteres con los que vamos a trabajar
caracteres = 'abcdefghijklmñnopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ1234567890_-+,#$%&/()=¿?¡!|,.;:{}[] '

def encriptar(mensaje:str, key:int) -> str:
    
    mensaje_encriptado = ''     # Generamos una variable donde guardaremos nuestro mensaje encriptado

    # Tomamos cada letra (o espacio) del mensaje y lo buscamos en la lista de caracteres
    # y obtenemos la posicion de esa letra en la lista de caracteres
    for letra in mensaje:
        for i, caracter in enumerate(caracteres):
            if letra == caracter:

                # Obtenemos la posicion del caracter para el mensaje encriptado
                index = i + key%len(caracteres)

                # Si la posicion sobre pasa el indice de la lista de caracteres, regresaremos a la posicion 0
                # de la lista de caracteres y seguimos contando hasta obtener la posicion del caracter encriptado
                if index > len(caracteres):
                    index -= len(caracteres)

                # Una vez tengamos la posicion del caracter encriptado, agregaremos este caracter al mensaje encriptado
                mensaje_encriptado += caracteres[index]
    
    return mensaje_encriptado   # Mensaje encriptado final


def desencriptar(mensaje_encriptado:str, key:int) -> str:
    
    mensaje_desencriptado = ''      # Generamos una variable donde guardaremos nuestro mensaje desencriptado

    # Tomamos cada letra (o espacio) del mensaje encriptado y lo buscamos en la lista de caracteres
    # y obtenemos la posicion de esa letra en la lista de caracteres
    for letra in mensaje_encriptado:
        for i, caracter in enumerate(caracteres):
            if letra == caracter:

                # Obtenemos la posicion del caracter del mensaje original
                index = i - key%len(caracteres)

                # Si la posicion sobre pasa el indice de la lista de caracteres, regresaremos a la posicion 0
                # de la lista de caracteres y seguimos contando hasta obtener la posicion del caracter del mensaje original
                if index > len(caracteres):
                    index -= len(caracteres)

                # Una vez tengamos la posicion del caracter original, agregaremos este caracter al mensaje desencriptado
                mensaje_desencriptado += caracteres[index]
    
    return mensaje_desencriptado    # Mensaje desencriptado final


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('------------------------------------------')
        print(' Programa 26: Cifrado de César')
        print('------------------------------------------')
        print(' 1) Encriptar un texto')
        print(' 2) Desencriptar un texto')
        print('------------------------------------------')
        opcion = int(input(' Opcion: '))
        while(opcion != 1 and opcion != 2):
            opcion = int(input(' Opcion: '))
        print('------------------------------------------')
        texto = input(' Ingrese el texto: ')
        key = int(input(' Ingrese la llave: '))

        if opcion == 1:
            texto_encriptado = encriptar(texto, key)
            print('\n\t', texto_encriptado)
        if opcion == 2:
            texto_desencriptado = desencriptar(texto, key)
            print('\n\t',texto_desencriptado)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

'''
mensaje = 'hola soy pakito'
key = 8

mensaje_encriptado = encriptar(mensaje, key)

print(f'   mensaje encriptado -> {mensaje_encriptado}')
print(f'mensaje desencriptado -> {desencriptar(mensaje_encriptado, key)}')
'''