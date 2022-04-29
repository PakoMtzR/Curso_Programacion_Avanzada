'''
# -*- coding: utf-8 -*-
Fecha de creacion: 25/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Generar un programa que obtenga una señal de audio 
mediante el micrófono o un archivo de audio (mp3, wav, etc) 
y permitir al usuario seleccionar el intervalo de frecuencias 
que desea escuchar, esto es, aplicar un filtro en un cierto 
intervalo de frecuencias, permitir escuchar el resultado y 
guardar el resultado en un archivo

Fuentes: 
---------------------------------------------------------------
'''
import pyaudio
import numpy as np
from time import sleep
from os import system
import preguntar
from tqdm import tqdm

p = pyaudio.PyAudio()

CHANNELS = 1
RATE = 44100

def callback(in_data, frame_count, time_info, flag):
    audio_data = np.fromstring(in_data, dtype=np.float32)   #np.fromstring buffer
    x = np.linspace(0, np.pi*2, audio_data.shape[0])
    funamental = np.cos(0.8*x)
    audio_data *= funamental

    return audio_data.astype(np.float32), pyaudio.paContinue



if __name__ == '__main__':

    # ---------------------------------------------------------------------------- #
    #                                Programa Principal
    # ---------------------------------------------------------------------------- #

    stream = p.open(
    format=pyaudio.paFloat32,
    channels=CHANNELS,
    rate=RATE,
    output=True,
    input=True,
    stream_callback=callback,
    )
    volver_a_intentar = True

    while volver_a_intentar == True:
        try:
            system('cls')   # Limpiamos la consola

            print('----------------------------------------------------------')
            print(' Programa 19: Distorsionar voz (para extorsionar gente)')
            print('----------------------------------------------------------\n')
            tiempo = int(input('Ingrese el tiempo [s]: '))
            print('\n Granbando...')
            
            stream.start_stream()

            # Barra de progreso
            delta_t = 0.1
            for i in tqdm(range(int(tiempo/delta_t))):
                sleep(delta_t)

            stream.close()

        except:
            print('\n')
            print(' ¿Tas tonto o qué?, sigue las instrucciones... menso!!!')

        finally:
            print('\n')
            volver_a_intentar = preguntar.quieres_volver_a_intentarlo() # True / False
