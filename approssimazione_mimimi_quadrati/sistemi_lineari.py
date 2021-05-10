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

# scambia la k-esima riga con la p-esima
def SwapRows(M, k, p):
    M[[k,p],:] = M[[p,k],:]

def fattorizzazioneLU(A, pivoting = 0):
    m,n = A.shape
    if m != n:
        print("Matrice non quadrata:")
        return [],[],[],1 # P,L,U,flag
    P = np.eye(n)
    U = A.copy()
    for k in range(n-1):
        # Test su elemento pivotale
        if U[k,k] == 0:
            print("Elemento pivotale nullo")
            return [],[],[],1
        p = np.argmax(abs(U[k,k])) + k
        if pivoting and p != k:
            SwapRows(U,k,p)
            SwapRows(P,k,p)
        # Eliminazione gaussiana
        U[k+1:n,k] = U[k+1:n,k]/U[k,k] # Memorizzo i moltiplicatori della k-esima colonna
        U[k+1:n,k+1:n] = U[k+1:n,k+1:n] - np.outer(U[k+1:n,k],U[k,k+1:n]) # El. gaussiana sulla matrice
    L = np.tril(U,-1) + np.eye(n)
    U = np.triu(U) # estrae la triangolare superiore, con diagonale
    return P,L,U,0

def solveLU(P,L,U,b):
    y,flag = solveL(L,np.dot(P,b))
    if flag:
        return [],1
    return solveU(U,y)