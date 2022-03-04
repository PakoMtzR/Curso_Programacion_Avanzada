# -*- coding: utf-8 -*-
'''
Fecha de creación: 02/03/2022
autor: PakoMtz 

-----------------------------------------------------------------------
Problema: Generar una pequeña calculadora de números complejos 
que le permita al usuario seleccionar si realizar operaciones 
con un par de números complejos o un solo número complejo. 
En el caso de un solo número complejo, la calculadora permitirá 
mostrar tanto la parte real, como la compleja,. el valor 
absoluto o módulo y la fase . En el caso de que se permita 
ingresar un par de números complejos, estos podrán o sumarse, 
restarse, multiplicarse, dividirse o realizar el producto escalar. 
(Notar que en este ejercicio es necesario el uso de una 
instrucción switch, encontrar la forma de sustituir dicha instrucción, 
pues en Python no se dispone de ella).
-----------------------------------------------------------------------
'''
from os import system
import preguntar
import math

class complejo():
    # Crear numero imaginario
    def __init__(self, real = 0, imag = 0):         

        # Funcion para guardar numeros complejos en su forma binomica
        def forma_binomica(real, imag) -> str:
            binomica = ''
            if imag >= 0:
                binomica = str(real) + '+' + str(imag) + 'j'
            else:
                binomica = str(real) + str(imag) + 'j'
            return binomica

        # Definiendo complejo en su forma binomica
        self.real = real
        self.imag = imag
        self.binomica = forma_binomica(self.real, self.imag)

        # Definiendo complejo en su forma polar
        self.modulo = round(((real**2) + (imag**2))**0.5, 4)
        if self.real == 0 and self.imag == 0:
            self.fase = 0
        elif self.real == 0 and self.imag > 0:
            self.fase = 90
        elif self.real == 0 and self.imag < 0:
            self.fase = -90
        else:
            self.fase = round(math.degrees(math.atan(imag/real)), 4)
        self.polar = str(self.modulo) + '<' + str(self.fase) + '°'

        # Definiendo el conjugado del complejo  a+bj -> a-bj
        self.real_conjugado = self.real
        self.imag_conjugado = -1 * self.imag
        self.conjugado = forma_binomica(self.real_conjugado, self.imag_conjugado)

        # Definiendo el opuesto del complejo    a+bj -> -a-bj
        self.real_opuesto = -1 * self.real
        self.imag_opuesto = -1 * self.imag
        self.opuesto = forma_binomica(self.real_opuesto, self.imag_opuesto)

        # Definiendo el inverso del complejo
        # Sea z un complejo -> z * z_inverso = 1    donde: z_inverso = z_conjugado / z_modulo^2
        self.real_inverso = round((self.real_conjugado / (self.modulo**2)), 4)
        self.imag_inverso = round((self.imag_conjugado / (self.modulo**2)), 4)
        self.inverso = forma_binomica(self.real_inverso, self.imag_inverso)
        

# Operaciones con complejos
def suma_compleja(complejo1:object, complejo2:object) -> object:
    suma = complejo(complejo1.real + complejo2.real, complejo1.imag + complejo2.imag)
    return suma

def resta_compleja(complejo1:object, complejo2:object) -> object:
    resta = complejo(complejo1.real + complejo2.real_opuesto, complejo1.imag + complejo2.imag_opuesto)
    return resta 

def producto_complejo(complejo1:object, complejo2:object) -> object:
    producto = complejo(((complejo1.real*complejo2.real)-(complejo1.imag*complejo2.imag)) , ((complejo1.real*complejo2.imag)+(complejo1.imag*complejo2.real)))
    return producto

def division_compleja(complejo1:object, complejo2:object) -> object:
    complejo2_inverso = complejo(complejo2.real_inverso, complejo2.imag_inverso)
    division = producto_complejo(complejo1, complejo2_inverso)
    return division


# Simulamos un switch case
def switch_case_artesanal(argumento:int):
    switcher = {
        1: '(' + str(complejo1.binomica) + ')' + ' + ' + '(' + str(complejo2.binomica) + ')' + ' = ' + str(suma_compleja(complejo1, complejo2).binomica),
        2: '(' + str(complejo1.binomica) + ')' + ' - ' + '(' + str(complejo2.binomica) + ')' + ' = ' + str(resta_compleja(complejo1, complejo2).binomica),
        3: '(' + str(complejo2.binomica) + ')' + ' - ' + '(' + str(complejo1.binomica) + ')' + ' = ' + str(resta_compleja(complejo2, complejo1).binomica),
        4: '(' + str(complejo1.binomica) + ')' + ' * ' + '(' + str(complejo2.binomica) + ')' + ' = ' + str(producto_complejo(complejo1, complejo2).binomica),
        5: '(' + str(complejo1.binomica) + ')' + ' / ' + '(' + str(complejo2.binomica) + ')' + ' = ' + str(division_compleja(complejo1, complejo2).binomica),
        6: '(' + str(complejo2.binomica) + ')' + ' / ' + '(' + str(complejo1.binomica) + ')' + ' = ' + str(division_compleja(complejo2, complejo1).binomica),
    }
    return switcher.get(argumento, "[Error]: Seleccione alguna de la opciones")



# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 29: Calculadora de Números Complejos ')
        print('----------------------------------------------------------')
        print(' ================== Opciones ==================')
        print(' 1) Conocer información de un número complejo')
        print(' 2) Operar con dos números complejos')
        print('----------------------------------------------------------')
        opcion = int(input(' Opcion: '))
        
        if opcion == 1:
            system('cls')
            print('----------------------------------------------------------')
            print(' 1) Conocer información de un número complejo')
            print('                       a + bj')
            print('----------------------------------------------------------')
            real = float(input('       Ingrese la parte real (a): '))
            imag = float(input(' Ingrese la parte imaginaria (b): '))
            print('----------------------------------------------------------\n')
            num_complejo = complejo(real, imag)
            print('     Forma binomica --> ', num_complejo.binomica)
            print('        Forma polar --> ', num_complejo.polar)
            print('          Conjugado --> ', num_complejo.conjugado)
            print('            Opuesto --> ', num_complejo.opuesto)
            print('            Inverso --> ', num_complejo.inverso)

        elif opcion == 2:
            system('cls')
            print('----------------------------------------------------------')
            print(' 2) Operar con dos números complejos')
            print('                 a + bj')
            print('----------------------------------------------------------')
            print(' Primer Complejo:\n')
            real1 = float(input('       Ingrese la parte real (a): '))
            imag1 = float(input(' Ingrese la parte imaginaria (b): '))
            print('----------------------------------------------------------')
            print(' Segundo Complejo:\n')
            real2 = float(input('       Ingrese la parte real (a): '))
            imag2 = float(input(' Ingrese la parte imaginaria (b): '))
            print('----------------------------------------------------------\n')

            complejo1 = complejo(real1, imag1)
            complejo2 = complejo(real2, imag2)
            system('cls')
            print(f'\n    a = {complejo1.binomica}')
            print(f'    b = {complejo2.binomica}\n')

            print(' Operaciones:')
            print('----------------------------------------------------------')
            print(' 1) Suma [a + b]')
            print(' 2) Resta [a - b]')
            print(' 3) Resta [b - a]')
            print(' 4) Producto [a*b]')
            print(' 5) Division [a / b]')
            print(' 6) Division [b / a]')
            print('----------------------------------------------------------')
            operacion = int(input(' Seleccione una operacion: '))
            resultado = switch_case_artesanal(operacion)
            print('\n\t', resultado)

        else:
            pass
        
    except:
        print('\n')
        print(' ¿Tas tonto o qué?, lee bien las instrucciones... menso')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False