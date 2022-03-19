# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:35:47 2022

@author: Usuario
"""

import numpy as np
import time



# dimensiones maximas de la matriz
matrizMax = 500

def inicializarMatriz():
    global matrizA
    global matrizB
    
  

    #Uso de numpy para generar la matriz
    matrizA = np.random.random((matrizMax,matrizMax))
    matrizA = matrizA * 10
    matrizA = matrizA.astype(int)
    
    #imprimirMatriz(matrizA)   
    
    matrizB = np.random.random((matrizMax,matrizMax))
    matrizB = matrizB * 10
    matrizB = matrizB.astype(int)
    
    #imprimirMatriz(matrizB)
    
    matrizC = np.zeros((matrizMax,matrizMax))
    matrizC = matrizC.astype(int)


#Impresion de las mnatrices
def imprimirMatriz(matrizImpresion):
    #global matrizC
    
    for r in matrizImpresion:
        print(r)
    print()  # nueva linea

def multiplicar():
    res = [[0 for x in range(matrizMax)] for y in range(matrizMax)]
     
    # explicit for loops
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizB)):
     
                # resulted matrix
                res[i][j] += matrizA[i][k] * matrizB[k][j]
     
    #print (res)    
    imprimirMatriz(res)

#ejecucion de main
if __name__=='__main__':   
    
    tiempo_inicio = time.time()
    
    inicializarMatriz()
    multiplicar()
    
    tiempo_fin = time.time()
    
    print("Tiempo de ejecucion : " + str(tiempo_fin - tiempo_inicio) + " segundos")
        
    