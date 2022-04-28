'''
# -*- coding: utf-8 -*-
Fecha de creacion: 17/03/2022
autor: PakoMtz 
 
---------------------------------------------------------------
Problema: Realizar la simulación y animación de un péndulo 
simple, pidiendo al usuario los siguientes datos: Masa del 
péndulo, aceleración de la gravedad, Longitud del péndulo, 
constante de fricción viscosa.

Fuentes: 
---------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt

# Propiedades del modelo
m, l, g = 1, 1, 9.88

# Condiciones iniciales
t = 0
omega_0 = 1.5
theta_0 = 0
u = np.array([theta_0, omega_0])

# Campo de direcciones
def f(u,t):
    return -g*np.sin(u[0])/l

def F(u,t):
    return np.array([u[1], f(u,t)])

# Solucion
t_sol = [t]
theta_sol = [u[0]]
omega_sol = [u[1]]
dt = 0.1
t_final = 10

while t < t_final:
    u = u + F(u,t) * dt
    t += dt
    theta_sol.append(u[0])
    omega_sol.append(u[1])
    t_sol.append(t)


import matplotlib.animation as animation

#thetasol=np.array(thetasol)
fig=plt.figure()
ax=fig.gca()

def actualizar(i):
    ax.clear()
    plt.plot([0,l*np.sin(theta_sol[i])],[0,-l*np.cos(theta_sol[i])],'b-')
    plt.plot(l*np.sin(theta_sol[i]),-l*np.cos(theta_sol[i]),'ro')
    plt.title('t = '+str(round(t_sol[i],3)))
    plt.xlim(-l-1,l+1)
    plt.ylim(-l-1,1)

ani=animation.FuncAnimation(fig, actualizar, range(len(t_sol)))
plt.show()