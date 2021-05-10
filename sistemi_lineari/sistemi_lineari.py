# -*- coding: utf-8 -*-
"""
Sistemi lineari
"""
import numpy as np
def solveL(L,b):
    # L matrice triangolare inferiore
    m,n = L.shape
    if m != n:
        print("matrice non quadrata")
        return [],1
    # Test singolarita, se L e triangolare non singolare
    # Nella diagonale tutti gli elementi sono non nulli
    # --------------------------------------------------
    # np all verifica che tutti gli elementi lungo un asse siano "True", 
    # diag restituisce un array [...] like
    if np.all(np.diag(L)) != True:
        print("elemento diagonale nullo")
        return[],1
    x = np.zeros((n,1))
    for i in range(n):
        sommatoria = np.dot(L[i,:i],x[:i])
        x[i] = (b[i] - sommatoria)/L[i,i]
    return x,0    

def solveU(U,b):
    # U matrice triangolare superiore
    m,n = U.shape
    if m != n:
        print("matrice non quadrata")
        return [],1
    if np.all(np.diag(U)) != True:
        print("elemento diagonale nullo")
        return[],1
    x = np.zeros((n,1))
    for i in reversed(range(n)):
        sommatoria = np.dot(U[i,i:i+1], x[:i])
        x[i] = (b[i] - sommatoria)/U[i:i]
    return x,0