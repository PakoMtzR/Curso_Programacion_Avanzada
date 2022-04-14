'''
# -*- coding: utf-8 -*-
Fecha de creacion: 13/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Generar un programa que lea de la internet el 
siguiente texto: Romeo and Juliet by William Shakesperare y 
obtenga la estadítica, junto con su respectivo histograma, del 
número de letras que aprecen en el texto (esto es cuantas a's, 
cuántas b's, cuántas c's y así sucesivamente).

Fuentes: https://automatetheboringstuff.com/files/rj.txt
---------------------------------------------------------------
'''
import requests
import matplotlib.pyplot as plot

# De request lo que se hace es usar el método get para obtener algún archivo que este en línea
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# En caso de que se haya localizado el archivo se coloca el código de estátus como OK
res.status_code == requests.codes.ok

abecedario = 'abcdefghijklmnopqrstuvwxyz'   
texto = res.text[1810:159850]               # Seleccionamos un pedazo del texto localizado
contadores = [0] * len(abecedario)          # Creamos un arreglo el cual llevara el conteo de cuantas letras hay en el texto

# Contamos la cantidad de veces que aparece cada letra en el texto y la guardamos en el arreglo 'contadores'
for letra in texto:
    for i, value in enumerate(abecedario):
        if value == letra.lower():
            contadores[i] += 1

# Imprimimos la cantidad de veces que aparece cada letra en el texto
for i, value in enumerate(abecedario):
    print(f' {value} ---> {contadores[i]}')

# Generamos el histograma o la grafica de barras del paso anterior
plot.bar(list(abecedario), contadores)
plot.title('Letras en el texto')
plot.xlabel('Caracteres')
plot.ylabel('# de veces que aparecen')
plot.show() #dibujamos el histograma
