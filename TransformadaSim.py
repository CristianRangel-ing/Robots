import roboticstoolbox as rt
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *
np.set_printoptions(
    formatter={'float': lambda x: f"{0:8.4f}" if abs(x)<1e-10 else f"{x:8.4f}"}) # Configurar la impresión de matrices para mostrar 4 decimales y suprimir notación científica

from sympy import Symbol, Matrix, simplify  #Biblioteca para simbolos
from sympy import *
from sympy.matrices import rot_axis3

theta1,L1,theta2,L2= symbols('theta1 L1 theta2 L2') #Definir simbolos para las variables
T01=trotz(theta1) @ transl(L1,0,0) #Matriz de transformación del primer eslabón
print(f"Primera Transformacion:\n {T01}\n") #Imprimir la matriz de transformación del primer eslabón

T12=trotz(theta2) @ transl(L2,0,0) #Matriz de transformación del segundo eslabón
print(f"Segunda Transformacion:\n {T12}\n") #Imprimir la matriz de transformación del segundo eslabón

T02=T01 @ T12 #Matriz de transformación del segundo eslabón con respecto al marco base
print(f"Transformacion completa:\n {T02}\n") #Imprimir la matriz de transformación del segundo eslabón con respecto al marco base

M=Matrix(T02) #Convertir la matriz de transformación a una matriz de sympy
simplified_M=M.applyfunc(simplify) #Simplificar la matriz de transformación

#Mejor visualización de la matriz de transformación completa
def format_matrix(matrix):
    return '\n'.join([' '.join([str(entry.evalf()) for entry in row]) for row in matrix.tolist()])

#Imprimir la matriz de transformación completa simplificada
print(f"Transformacion completa simplificada:\n {format_matrix(simplified_M)}\n")

# Sustituit valores y resolver la matriz de transformación completa
M_evaluated = simplified_M.subs({theta1: np.deg2rad(30), L1: 4, theta2: np.deg2rad(0), L2: 3}).evalf()
print(f"Transformacion completa evaluada:\n {format_matrix(M_evaluated)}\n")