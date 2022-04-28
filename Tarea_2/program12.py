'''
# -*- coding: utf-8 -*-
Fecha de creacion: 06/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita obtener el CURP completo de una 
persona, solicitando los datos necesarios (Nombre, Apellidos, 
Fecha de Nacimiento, lugar de nacimiento), siguiendo para ello 
las instrucciones proporcionadas en el DOF Normativa para 
generar el CURP, DOF utilizar, de ser posible, el paradigma de 
programación orientado a objetos. Omitir los dos últimos 
dígitos asignados por el RENAPO

Fuentes: https://www.dof.gob.mx/nota_detalle.php?codigo=5526717&fecha=18/06/2018
---------------------------------------------------------------
'''
from os import system
import preguntar

vocales = ('A', 'E', 'I', 'O', 'U')
estados = {
        "BAJA CALIFORNIA": "BC",
        "BAJA CALIFORNIA SUR": "BS",
        "CAMPECHE": "CC",
        "CHIAPAS": "CS",
        "CHIHUAHUA": "CH",
        "COAHUILA": "CL",
        "COLIMA": "CM",
        "CIUDAD DE MEXICO": "DF",
        "DURANGO": "DG",
        "GUANAJUATO": "GT",
        "GUERRERO": "GR",
        "HIDALGO": "HG",
        "JALISCO": "JC",
        "ESTADO DE MEXICO": "MC",
        "MICHOACAN": "MN",
        "MORELOS": "MS",
        "NAYARIT": "NT",
        "NUEVO LEON": "NL",
        "OAXACA": "OC",
        "PUEBLA": "PL",
        "QUERETARO": "QT",
        "QUINTANA ROO": "QR",
        "SAN LUIS POTOSI": "SP",
        "SINALOA": "SL",
        "SONORA": "SR",
        "TABASCO": "TC",
        "TAMAULIPAS": "TS",
        "TLAXCALA": "TL",
        "VERACRUZ": "VZ",
        "YUCATAN": "YN",
        "ZACATECAS": "ZS"
        }

def primera_vocal(texto:str) -> str:
    for letra in texto:
        if letra in vocales:
            return letra

def lugar_nacimiento(estado_nacimiento:str) -> str:
    for estado in estados:
        if estado_nacimiento == estado:
            return estados[estado]

def convertir_2digitos(num:int) -> str:
    num = str(num)
    if len(num) > 2:        # Anno
        num = num[2::]       # Ultimos dos digitos del numero
    elif len(num) < 2:      # 4 -> 04, 9 -> 09
        num = '0' + num
    else:
        pass
    return num
    
def primera_consonante_interna(texto:str) -> str:
    texto = texto[1::]  # Quitamos la primera letra del texto
    for letra in texto:
        if letra in vocales:    # si no es vocal, entonces es consonante
            pass
        else:
            return letra

class Persona():
    def __init__(self, nombre, apellido_paterno, apellido_materno, anno, mes, dia, sexo, estado_nacimiento) -> None:
        self.nombre = nombre.upper()
        self.apellido_paterno = apellido_paterno.upper()
        self.apellido_materno = apellido_materno.upper()
        self.anno = convertir_2digitos(anno)
        self.mes = convertir_2digitos(mes)
        self.dia = convertir_2digitos(dia)
        self.sexo = sexo.upper()
        self.estado = lugar_nacimiento(estado_nacimiento.upper())
        self.rfc = self.apellido_paterno[0] + primera_vocal(self.apellido_paterno) + self.apellido_materno[0] + self.nombre[0] + self.anno + self.mes + self.dia
        self.curp = self.rfc + self.sexo + self.estado + primera_consonante_interna(self.apellido_paterno) + primera_consonante_interna(self.apellido_materno) + primera_consonante_interna(self.nombre)



# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 12: Generador de CURP')
        print('----------------------------------------------------------\n')
        nombre = input('Ingrese su nombre: ')
        apellido_paterno = input('Ingrese su apellido paterno: ')
        apellido_materno = input('Ingrese su apellido materno: ')
        anno = input('Ingrese su año de nacimiento (####): ')
        mes = input('Ingrese su mes de nacimiento (formato numerico ##): ')
        dia = input('Ingrese su dia de nacimiento (##): ')
        sexo = input('Indique su sexo [H/M]: ')
        estado = input('Ingrese su estado natal (sin acentos): ')

        ciudadano = Persona(nombre, apellido_paterno, apellido_materno, anno, mes, dia, sexo, estado)
        print('\n' + 'CURP --> ' + ciudadano.curp)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

