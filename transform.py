import roboticstoolbox as rt
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

# Crear una matriz de transformación homogénea (rotacional)
# from sympy import Symbol, Matrix  #Biblioteca para simbolos 
# theta=Symbol('theta')
# R=Matrix(rot2(theta))
# print(R)
#Conversion de grados a radianes
theta_deg=30
theta_rad=np.deg2rad(theta_deg)

R=rot2(theta_rad)
print(R)
# Matriz de traslación 
R2=trot2(theta_rad)
print(R2)

# trplot2(R) #Dibujar en plot
# plt.axis('equal') #Mantener proporciones iguales}
# plt.grid(True) #Agregar cuadrícula
# plt.xlabel('X') #Etiqueta del eje X
# plt.ylabel('Y') #Etiqueta del eje Y
# plt.title(f'Rotación 2D') #Título del gráfico
# plt.show() #Mostrar el gráfico

# #Graficar la matriz de traslación
Tr= transl2(0, 0) #Funcion para crear matriz de traslación en el inicio del plano
trplot2(Tr, frame='0', color='k') #Dibujar en plot
# T1= transl2(1, 2) #Funcion para crear matriz de traslación en el punto (1,2)
# print(T1)
# trplot2(T1, frame='A', color='b') #Dibujar en plot
# plt.axis('equal') #Mantener proporciones iguales
# plt.grid(True) #Agregar cuadrícula
# plt.xlabel('X') #Etiqueta del eje X
# plt.ylabel('Y') #Etiqueta del eje Y
# plt.title('Traslación 2D') #Título del gráfico
# plt.show() #Mostrar el gráfico

TA= transl2(1, 2) @ trot2(30,"deg") #Matriz de transformación combinada (traslación + rotación)
print(TA)
trplot2(TA, frame='A', color='b') #Dibujar en plot
plot_circle(4, (0,0), "b--") #Dibujar un círculo en el punto (1,2) con radio 0.5
P=np.array([4,3]) #Punto a transformar
plot_point(P, 'ko', text='P') #Dibujar el punto original
TB= trot2(30,"deg") @ transl2(1, 2) #Matriz de transformación combinada (traslación + rotación)
print(TB)
trplot2(TB, frame='B', color='r') #Dibujar en plot
P1=homtrans(np.linalg.inv(TA), P) #Como llegar al punto P desde A 
print(P1)
plt.axis('equal') #Mantener proporciones iguales
plt.grid(True) #Agregar cuadrícula      
plt.xlabel('X') #Etiqueta del eje X
plt.ylabel('Y') #Etiqueta del eje Y
plt.title('Transformación Combinada 2D') #Título del gráfico
plt.show() #Mostrar el gráfico