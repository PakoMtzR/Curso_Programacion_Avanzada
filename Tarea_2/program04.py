'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema:

Fuentes: 
---------------------------------------------------------------
'''
from math import *
from io import open


cala3=open("archivo de ejercicio numerico 4.txt","w")#para archivo de texto
def f(x):
    return cos(x)-pow(x,2)#variables
a = float(input("Ingresa el interbalo a: ")) 
b = float(input("Ingresa el intervalo b: ")) 
n= int(input("Ingresa el numero del intervalo: ")) 
cala3.write("n=%s\n"%n)
h = (b-a)/n#se inicia el metodo del trapezio
cala3.write("h=%s\n"%h)
sum=0.0
for i in range(1,n):
    x=a+i*h
    sum=sum+f(x)
    
trap=h*(f(a)+2*sum+f(b))/2#formula
cala3.write("trap=%s\n"%trap)
print("valor integral",trap)
cala3.close()