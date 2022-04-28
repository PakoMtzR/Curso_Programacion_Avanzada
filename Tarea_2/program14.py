'''
# -*- coding: utf-8 -*-
Fecha de creacion: 27/04/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Programa que permita obtener diversas soluciones de 
el problema de las 8 reinas. El programa debe permitirle al 
usuario seleccionar la posición inicial de una de las reinas y 
de ahí mostrarle la(s) posible(s) solución(es).

Fuentes: 
---------------------------------------------------------------
'''
class chess():
    # Creamos el tablero Vacio
    def __init__(self):
        self.tablero = []
        self.posiciones_reinas = []
        for i in range(8):
            fila = [' ' for i in range(8)]
            self.tablero.append(fila)

    # Funcion para imprimir el tablero
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(fila)
    

    def reina_en_fila(self, fila):
        if 'Q' in self.tablero[fila]:
            return True
        else:
            return False    


    def reina_en_columna(self, columna):
        for fila in self.tablero:
            if 'Q' in fila[columna]:
                return True
        return False


    def reina_en_diagonal(self, fila, columna):
        
        fila_copia, columna_copia = fila, columna   # Creamos una copia de la posicion a evaluar
        
        # Verificar si hay reina en la diagonal de derecha hacia abajo
        while (fila <= 7) and (columna <= 7):
            if self.tablero[fila][columna] == 'Q':
                return True
            fila += 1
            columna += 1

        fila, columna = fila_copia, columna_copia   # Resetamos los valores
        
        # Verificar si hay reina en la diagonal de izquierda hacia arriba
        while (fila >= 0) and (columna >= 0):
            if self.tablero[fila][columna] == 'Q':
                return True
            fila -= 1
            columna -= 1
        
        fila, columna = fila_copia, columna_copia   # Resetamos los valores
        
        # Verificar si hay reina en la diagonal de derecha hacia arriba
        while (fila >= 0) and (columna <= 7):
            if self.tablero[fila][columna] == 'Q':
                return True
            fila -= 1
            columna += 1
        
        fila, columna = fila_copia, columna_copia   # Resetamos los valores
        
        # Verificar si hay reina en la diagonal de izquierda hacia abajo
        while (fila <= 7) and (columna >= 0):
            if self.tablero[fila][columna] == 'Q':
                return True
            fila += 1
            columna -= 1
        
        return False    # Si despues de todo no encuentra reinas entonces retorna False


    def poner_reina(self, fila, columna):
        self.tablero[fila][columna] = 'Q'
        self.posiciones_reinas.append([fila, columna])  # Guardamos la posicion de la reina

    def quita_reina(self, fila, columna):
        self.tablero[fila][columna] = ' '
        self.posiciones_reinas.pop()
    
    def colocar_reinas(self, fila_inicial = 0, columna_inicial = 0):
        for fila in range(fila_inicial, 8):
            for casilla in range(columna_inicial, 8):
                if not((self.reina_en_fila(fila)) or (self.reina_en_columna(casilla)) or (self.reina_en_diagonal(fila,casilla))):
                    self.poner_reina(fila,casilla)
                    self.posiciones_reinas.append([fila,casilla])
            columna_inicial = 0
        
        '''
        for i, fila in enumerate(self.tablero):
            for j, casilla in enumerate(fila):
                if (self.reina_en_fila(i)) or (self.reina_en_columna(j)) or (self.reina_en_diagonal(i,j)):
                    pass
                else:
                    self.colocar_una_reina(i,j)
                    self.posiciones_reinas.append([i,j])
        
        '''
        if len(self.posiciones_reinas) < 8:
            ultima_reina = self.posiciones_reinas[-1]   # Ultima reina colocada
            ultima_fila, ultima_columna = ultima_reina[0], ultima_reina[1]
            self.quita_reina(ultima_fila, ultima_columna)
            if ultima_columna == 7: 
                ultima_columna = -1
            self.colocar_reinas(ultima_fila, ultima_columna+1)






my_chess = chess()
#my_chess.colocar_una_reina(5,6)
#my_chess.imprimir_tablero()
my_chess.colocar_reinas()
print('\n')
my_chess.imprimir_tablero()
'''
if my_chess.reina_en_diagonal(5,4):
    print('hay reina')
else:
    print('no hay')
'''
