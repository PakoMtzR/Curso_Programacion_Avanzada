# -*- coding: utf-8 -*-

# Script pa crear los archivos de python porque me da flojera andar creando uno por uno :v
import os

for i in range(1,22):
    if i < 10:
        num = '0' + str(i)
    else:
        num = str(i)
    
    file = open('D:/UPIIH/4_Semestre/Programacion_Avanzada/Tarea_2/program{0}.py'.format(num), 'w')
    file.write("'''\n")
    file.write('# -*- coding: utf-8 -*-\n')
    file.write('Fecha de creacion: 17/03/2022\n')
    file.write('autor: PakoMtz \n')
    file.write(' \n')
    file.write('---------------------------------------------------------------\n')
    file.write('Problema:\n')
    file.write('\n')
    file.write('Fuentes: \n')
    file.write('---------------------------------------------------------------\n')
    file.write("'''\n")
    file.close()

