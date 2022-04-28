'''
# -*- coding: utf-8 -*-
Fecha de creacion: 09/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Generar un programa que simule la entrega de un a 
mano de cartas de la baraja inglesa (5 cartas en total) a dos 
jugadores (debe mostrarse las dos manos en la consola). 
Utilizar la programación orientada a objetos para resolver 
este programa.

Fuentes: 
---------------------------------------------------------------
'''
from os import system
import preguntar
import random

numeros = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']
simbolos = ['Treboles', 'Diamantes', 'Corazones', 'Picas']

class baraja():
    # Generamos las cartas de la baraja
    def __init__(self):
        self.cartas = []
        for simbolo in simbolos:
            for numero in numeros:
                self.cartas.append(f'{numero} de {simbolo}')
    
    def barajear_cartas(self):
        self.cartas_barajeadas = []     # Creamos una lista que guardara las cartas que selecionaremos al azar del mazo principal
        for i in range(52):             # Seleccionaremos 52 cartas (cartas totales del mazo) al azar y las iremos agregando a la lista anterior 
            carta_aleatoria = random.choice(self.cartas)    # Seleccionamos una carta aleatoria
            self.cartas_barajeadas.append(carta_aleatoria)  # Lo agregamos a la lista de cartas barajeadas
            self.cartas.remove(carta_aleatoria)             # Eliminamos la carta del mazo principal
        self.cartas = self.cartas_barajeadas                # Cuando termine el ciclo for, el mazo principal ya no tendra cartas.
                                                            # Por lo tanto, asignaremos los valores de la lista de las cartas barajeadas al mazo principal
    
    def repartir_cartas(self, cant_jugadores = 2, numero_de_cartas_por_jugador = 5):
        if cant_jugadores*numero_de_cartas_por_jugador < len(self.cartas):  # Verificamos si se puede repartir las cartas entre la cantidad de jugadores indicados
            for jugador in range(1, cant_jugadores + 1):
                print(f' Jugador {jugador}:')
                print('----------------------------')
                for i in range(numero_de_cartas_por_jugador):
                    print(self.cartas[0])                   # Tomamos la primera carta del mazo
                    self.cartas.pop(0)                      # Eliminamos esa carta del mazo principal
                print('----------------------------\n')
        
        else:
            print(f' No se puede repartir las cartas para {cant_jugadores} jugadores. ')


# ---------------------------------------------------------------------------- #
#                                Programa Principal
# ---------------------------------------------------------------------------- #
volver_a_intentar = True

while volver_a_intentar == True:
    try:
        system('cls')   # Limpiamos la consola

        print('----------------------------------------------------------')
        print(' Programa 09: Baraja inglesa')
        print('----------------------------------------------------------\n')
        cant_jugadores = int(input(' Cuantos le van a entrar? : '))
        cartas_por_jugador = int(input(' De a cuantas cartas por jugador? : '))

        mi_baraja = baraja()
        mi_baraja.barajear_cartas()
        mi_baraja.repartir_cartas(cant_jugadores, cartas_por_jugador)

    except:
        print('\n')
        print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

    finally:
        print('\n')
        volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False

