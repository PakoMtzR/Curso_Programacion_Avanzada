'''
# -*- coding: utf-8 -*-
Fecha de creacion: 08/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema:
Generar un programa que acepte una cadena de texto que representan una constraseña; 
el programa debe revisar que la contraseña sea válida, tomando en cuenta los 
siguientes criterios:

    Debe contener al menos una letra minúscula [a-z]
    Debe contener al menos un número [0-9]
    Debe contener al menos una letra mayúscula [A-Z], no en la primera posición
    Debe contener al menos un caracter especial [$, #, @, _]
    Longitud mínima - máxima de la contraseña, 6-12 caracteres

Sólo hasta que se ingresa la contraseña correcta, el programa debe permitir continuar. 
Una vez que se ingrese una contraseña válida, el programa guardará la contraseña 
cifrada mediante el algoritmo César del grupo de ejercicios I (problema 26), 
seleccionando de manera aleatoria entre [0,20], el número de posiciones a mover, 
y guardando primero dicho número seguido de la contraseña en el archivo de texto (.txt). 
Este archivo debe irse actualizando con todas las contraseñas que se vayan ingresando 
en el programa.

Fuentes: 
---------------------------------------------------------------
'''

import random

# Definimos una variable global el cual contenga los caracteres con los que vamos a trabajar
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890|°¬!"#$%&/\()=?¿@*+~{}[^`],;.:-_\'<> '
abecedario = 'abcdefghijklmnopqrstuvwxyz'

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


# Criterios para validar la contraseña
def criterio_1(password:str) -> bool:   # Debe contener al menos una letra minúscula
    for letra in password:
        if letra in abecedario:
            return True
        else: pass
    return False

def criterio_2(password:str) -> bool:   # Debe contener al menos un número
    numeros = [str(i) for i in range(10)]
    for letra in password:
        if letra in numeros:
            return True     # Si la letra es un numero entonces el criterio se cumple
        else: pass
    return False    # Si al final de recorrer toda la contraseña no encuentra un numero, entonces retorna False

def criterio_3(password:str) -> bool:   # Debe contener al menos una letra mayúscula [A-Z], no en la primera posición
    password = password[1::]    # Quitamos la primera letra de la contraseña
    for letra in password:
        if letra in abecedario.upper():
            return True
        else: pass
    return False

def criterio_4(password:str) -> bool:   # Debe contener al menos un caracter especial [$, #, @, _]
    caracteres_especiales = '|°¬!"#$%&/\()=?¿@*+~{}[^`],;.:-_\'<>'
    for letra in password:
        if letra in caracteres_especiales:
            return True
        else: pass
    return False

def criterio_5(password:str) -> bool:   # Longitud mínima - máxima de la contraseña, 6-12 caracteres
    if len(password) >= 6 and len(password) <= 12:
        return True
    else:
        return False


print("""
Ingrese una contraseña con los siguientes criterios:
-----------------------------------------------------------------------------------------
    (1)... Debe contener al menos una letra minúscula [a-z]
    (2)... Debe contener al menos un número [0-9]
    (3)... Debe contener al menos una letra mayúscula [A-Z], no en la primera posición
    (4)... Debe contener al menos un caracter especial [$, #, @, _]
    (5)... Longitud mínima - máxima de la contraseña, 6-12 caracteres
-----------------------------------------------------------------------------------------
""")

password_invalido = True
while password_invalido:
    password = input('  Ingrese la contraseña: ')
    if criterio_1(password) and criterio_2(password) and criterio_3(password) and criterio_4(password) and criterio_5(password):
        key = random.randint(1,20)
        password_cifrado = encriptar(password, key)

        with open('passwords.txt', 'a') as lista:
            lista.write(f'\n {str(key)} ---> {password_cifrado}')
        
        print('     [Contraseña Guardada]\n')
        password_invalido = False
    else: 
        print('     [Contraseña invalida, intentelo de nuevo]\n')


