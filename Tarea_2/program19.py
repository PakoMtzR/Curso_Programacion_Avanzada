'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
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

p = pyaudio.PyAudio()

CHANNELS = 1
RATE = 44100

def callback(in_data, frame_count, time_info, flag):
    audio_data = np.fromstring(in_data, dtype=np.float32)
    x = np.linspace(0, np.pi*2, audio_data.shape[0])
    funamental = np.cos(10*x)
    audio_data *= funamental

    return audio_data.astype(np.float32), pyaudio.paContinue

stream = p.open(
    format=pyaudio.paFloat32,
    channels=CHANNELS,
    rate=RATE,
    output=True,
    input=True,
    stream_callback=callback,
)

stream.start_stream()
sleep(30)
stream.close()