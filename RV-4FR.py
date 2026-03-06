import sympy as sp
from sympy.matrices import rot_axis3
import matplotlib.pyplot as plt
import numpy as np
from spatialmath import *
from spatialmath.base import *
import roboticstoolbox as rtb
RV_4FR=rtb.DHRobot([
    rtb.RevoluteDH(d=0.350, a=0, alpha=-np.pi/2,qlim=[-4.189,4.189]),
    rtb.RevoluteDH(d=0, a=0.235, alpha=0, qlim=[-2.094,2.094], offset=-np.pi/2),
    rtb.RevoluteDH(d=0, a=0.05, alpha=-np.pi/2, qlim=[0,2.81]),
    rtb.RevoluteDH(d=0.275, a=0, alpha=np.pi/2,qlim=[-3.491,3.491]),
    rtb.RevoluteDH(d=0, a=0, alpha=-np.pi/2,qlim=[-2.094,2.094]),
    rtb.RevoluteDH(d=.085, a=0, alpha=0,qlim=[-6.283,6.283]),
], name='RV-4FR',base=SE3(0,0,0))
print(RV_4FR)

joint1=np.deg2rad(0) #Ángulo de la primera articulación en radianes
joint2=np.deg2rad(0) #Ángulo de la segunda articulación
joint3=np.deg2rad(0) #Ángulo de la tercera articulación en radianes
joint4=np.deg2rad(0) #Ángulo de la cuarta articulación en
joint5=np.deg2rad(0) #Ángulo de la quinta articulación en radianes
joint6=np.deg2rad(0) #Ángulo de la sexta articulación en

T06DH=RV_4FR.fkine([joint1, joint2, joint3, joint4, joint5, joint6]) #Calcular la matriz de transformación completa del robot utilizando la convención de Denavit-Hartenberg con los ángulos de las articulaciones
print(T06DH) #Imprimir la matriz de transformación completa del robot utilizando la convención de Denavit-Hartenberg con los ángulos de las articulaciones

q=np.array([[joint1, joint2, joint3, joint4, joint5, joint6],]) #Definir una configuración para el robot utilizando los ángulos de las articulaciones
q1=np.array([[0,-np.pi/2,0,0,0,0]]) #Definir una configuración para el robot utilizando los ángulos de las articulaciones
RV_4FR.teach(q1) #Dibujar la configuración del robot utilizando los ángulos de las articulaciones
