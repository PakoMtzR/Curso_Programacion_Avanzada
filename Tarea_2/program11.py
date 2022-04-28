'''
# -*- coding: utf-8 -*-
Fecha de creacion: 06/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que pemita obtener el RFC con homoclave de 
una persona, solicitando los datos necesarios 
(Nombre, Apellidos, Fecha de Nacimiento), siguiendo para ello 
las instrucciones proporcionadas por la SHCP 
¿Cómo generar el RFC? utilizar, de ser posible, el paradigma 
de programación orientado a objetos 

Fuentes: https://www.dropbox.com/s/knefl1rxxgu36wu/IFAI%200610100135506%20065%20Algoritmo%20para%20generar%20el%20RFC%20con%20homoclave%20para%20personas%20fisicas%20y%20morales.odt?dl=0
---------------------------------------------------------------
'''

from os import system
import preguntar

tabla1 = {
    ' ' : '00', '0' : '00', '1' : '01', '2' : '02', '3' : '03', '4' : '04', 
    '5' : '05', '6' : '06', '7' : '07', '8' : '08', '9' : '09', '&' : '10',
    'A' : '11', 'B' : '12', 'C' : '13', 'D' : '14', 'E' : '15', 'F' : '16',
    'G' : '17', 'H' : '18', 'I' : '19', 'J' : '21', 'K' : '22', 'L' : '23',
    'M' : '24', 'N' : '25', 'O' : '26', 'P' : '27', 'Q' : '28', 'R' : '29',
    'S' : '32', 'T' : '33', 'U' : '34', 'V' : '35', 'W' : '36', 'X' : '37',
    'Y' : '38', 'Z' : '39', 'Ñ' : '40'
}

tabla2 = {
     0 : '1',  1 : '2',  2 : '3',  3 :  '4', 4 :  '5', 5 : '6',  6 : '7',  7 : '8', 8 : '9', 
     9 : 'A', 10 : 'B', 11 : 'C', 12 : 'D', 13 : 'E', 14 : 'F', 15 : 'G', 16 : 'H',
    17 : 'I', 18 : 'J', 19 : 'K', 20 : 'L', 21 : 'M', 22 : 'N', 23 : 'P', 24 : 'Q',
    25 : 'R', 26 : 'S', 27 : 'T', 28 : 'U', 29 : 'V', 30 : 'W', 31 : 'X', 32 : 'Y', 33 : 'Z'
}

def primera_vocal(texto:str) -> str:
    vocales = ('A', 'E', 'I', 'O', 'U')
    for letra in texto:         
        if letra in vocales:    # Si la letra se encuentra en la tupla de vocales
            return letra
    
def convertir_2digitos(num:int) -> str:
    num = str(num)
    if len(num) > 2:        # Anno
        num = num[2::]
    elif len(num) < 2:      # 4 -> 04, 9 -> 09
        num = '0' + num
    else:
        pass
    return num

def generar_homoclave(nombre_completo:str) -> str:
    suma_numeros_nombre = 0
    numeros_nombre = '0'
    for letra in nombre_completo:
        if letra in tabla1:
            numeros_nombre += tabla1[letra]
    
    suma = 0
    for i in range(len(numeros_nombre) -1 ):
        suma += int(numeros_nombre[i] + numeros_nombre[i+1]) * int(numeros_nombre[i+1])
    
    suma_numeros_nombre = int(str(suma)[-3::])    # Tomamos los ultimos tres numeros

    digitos = [int(suma_numeros_nombre / 34), suma_numeros_nombre % 34]
    homoclave = ''
    if digitos[0] in tabla2:
        homoclave += tabla2[digitos[0]]
    if digitos[1] in tabla2:
        homoclave += tabla2[digitos[1]]
    
    return homoclave



class Persona():
    def __init__(self, nombre, apellido_paterno, apellido_materno, anno, mes, dia) -> None:
        self.nombre = nombre.upper()
        self.apellido_paterno = apellido_paterno.upper()
        self.apellido_materno = apellido_materno.upper()
        self.nombre_completo = self.apellido_paterno + ' ' + self.apellido_materno + ' ' + self.nombre
        self.anno = convertir_2digitos(anno)
        self.mes = convertir_2digitos(mes)
        self.dia = convertir_2digitos(dia)
        self.rfc =  self.apellido_paterno[0] + \
                    primera_vocal(self.apellido_paterno) + \
                    self.apellido_materno[0] + \
                    self.nombre[0] + \
                    self.anno + \
                    self.mes + \
                    self.dia + \
                    generar_homoclave(self.nombre_completo)


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 11: Generador de RFC')
        print('----------------------------------------------------------\n')
        nombre = input('Ingrese su nombre: ')
        apellido_paterno = input('Ingrese su apellido paterno: ')
        apellido_materno = input('Ingrese su apellido materno: ')
        anno = input('Ingrese su año de nacimiento (####): ')
        mes = input('Ingrese su mes de nacimiento (formato numerico ##): ')
        dia = input('Ingrese su dia de nacimiento (##): ')

        x = Persona(nombre, apellido_paterno, apellido_materno, anno, mes, dia)
        print('\n' + 'RFC --> ' + x.rfc)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False







