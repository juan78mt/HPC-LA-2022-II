# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:40:21 2022

@author: Usuario
"""
from threading import Thread
import random
import math
import numpy as np
import threading
import time

matrizA = []
matrizB = []
matrizC = []

paso_i = 0

dimension = 2 # dimensiones por defecto de matrices de 2X2

numHilos = 1   #probar primero con un hilo

# ---------------------------------------------------------------------------------
def ingresoMatriz():
    global dimension
    global numHilos
    print("MULTIPLICACION DE MATRICES PARALELAS CUADRADAS NXN ")
    print()
    
    
    
    dimension = int(input("INGRESAR EL NUMERO N PARA UNA MATRIZ DE NXN : "))
    numHilos = int(input("INGRESAR EL NUMERO DE HILOS : "))
    
# ---------------------------------------------------------------------------------    
    
def inicializarMatriz():
    global matrizA
    global matrizB
    global matrizC

    matrizA = np.random.random((dimension,dimension))
    matrizA = matrizA * 10
    matrizA = matrizA.astype(int)
    
    imprimirMatriz(matrizA)
        
    matrizB = np.random.random((dimension,dimension))
    matrizB = matrizB * 10
    matrizB = matrizB.astype(int)
    
    imprimirMatriz(matrizB)
    
    #inicializacion de la matriz matrizC para el resultado    
    #matrizC = [[0 for x in range(dimension)] for y in range(dimension)]
    matrizC = np.zeros((dimension,dimension))
    matrizC = matrizC.astype(int)

# -------------------------------------------------------------------------

def multMatrizParalela(inicio,fin):
    for i in range(inicio,fin):
        for j in range(dimension):
            for k in range(dimension):
                matrizC[i][j] += int(matrizA[i][k] * matrizB[k][j])

# ------------------------------------------------------------------------
#Impresion de las mnatrices
def imprimirMatriz(matrizImpresion):
    #global matrizC
    
    for r in matrizImpresion:
        print(r)
    print()  # nueva linea

# ------------------------------------------------------------------


def multiplicarSerial():
        
    # multiplicacion de AXB de forma serial
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizB)):     
                # matriz resultado
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
     
    #print (res)    
    #imprimirMatriz(matrizC)

# ------------------------------------------------------------------

def multi():
    #global paso_i
    paso_i = 0
    paso_i = paso_i + 1
    
    i = paso_i    # i se refiere al numero de renglon de la matrizC resultante
    n = dimension  #dimension de la matriz
      
    for j in range(0,dimension):
        for k  in range(0,dimension):
            matrizC[i][j] += int(matrizA[i][k] * matrizB[k][j])
            

# ---------------------------------------------------------    
def manejoHilos():
    global numHilos
    
    #arreglo de hilos
    manejoHilos = []
        

    for j in range(0,numHilos):
        
        #obtener rangos para repartir el trabajo entre los hilos disponibles 
        #en caso de que los hilos ingresados sobrepasen los que pueda tener el procesador
        #se asignara la mayor cantidad de hilos disponibles
        rangoInicio = int((dimension/numHilos) * j)
        rangoFin = int((dimension/numHilos) * (j+1))
        
        t = Thread(target = multMatrizParalela, args=(rangoInicio, rangoFin))
        
        manejoHilos.append(t)
        t.start()   
        
    #uso de join para unir los resultados obtenidos por medio de hilos
    for j in range(0,numHilos):
        manejoHilos[j].join()
        
    imprimirMatriz(matrizC)
            
if __name__=="__main__":
    
    ingresoMatriz()
    inicializarMatriz()
    
    tiempo_inicio = time.time()
    manejoHilos()
    tiempo_fin = time.time()
    
    print("Tiempo de ejecucion : " + str(tiempo_fin - tiempo_inicio) + " segundos")
    
# -------------------------------------------------------------------------------------


