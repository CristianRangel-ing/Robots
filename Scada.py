import roboticstoolbox as rt
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

# #Graficar la matriz de traslación
T0= transl2(0, 0) #Funcion para crear matriz de traslación en el inicio del plano
trplot2(T0, frame='0', color='k') #Dibujar en plot

TA= trot2(45,"deg") #Matriz de transformación combinada (traslación + rotación)
print(TA)
trplot2(TA, frame='A', color='b') #Dibujar en plot
plot_circle(4, (0,0), "b--") #Dibujar un círculo en el punto (1,2) con radio 0.5

TBA= TA @ transl2(4,0) @ trot2(60,"deg") #Matriz de transformación combinada (traslación + rotación)
trplot2(TBA, frame='B', color='g') #Dibujar en plot
origin_TBA=TBA[:2,2]
plot_circle(3, (origin_TBA[0], origin_TBA[1]), "g--") #Dibujar un círculo en el punto (1,2) con radio 0.5

TCBA=TBA @ transl2(3,0) #Matriz de transformación combinada (traslación + rotación)
trplot2(TCBA, frame='C', color='y') #Dibujar en plot
print(TCBA)

origin_TCBA=TCBA[:2,2]
P=np.array([origin_TCBA[0], origin_TCBA[1]]) #Punto a transformar
plot_point(P, 'ko', text='P') #Dibujar el punto original
print("Coordenadas de T0: {:.4f}, {:.4f}".format(P[0], P[1]))

# Calcular la transformación inversa de TA y TBA
P_TA=homtrans(np.linalg.inv(TA), P) #Como llegar al punto P desde A
print("Coordenadas de P en el marco A: {:.4f}, {:.4f}".format(P_TA[0,0], P_TA[1,0]))
P_TBA=homtrans(np.linalg.inv(TBA), P) #Como llegar al punto P desde B
print("Coordenadas de P en el marco B: {:.4f}, {:.4f}".format(P_TBA[0,0], P_TBA[1,0]))

plt.axis('equal') #Mantener proporciones iguales
plt.grid(True) #Agregar cuadrícula
plt.xlabel('X') #Etiqueta del eje X
plt.ylabel('Y') #Etiqueta del eje Y
plt.title('Transformación Combinada 2D') #Título del gráfico
plt.show() #Mostrar el gráfico