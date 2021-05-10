# -*- coding: utf-8 -*-
"""
Approssimazione con metodo QR
"""
import numpy as np
import scipy.linalg as spl

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

def metodoQR(x,y,n):
    Q,R = spl.qr(np.vander(x,n+1))
    ys = np.dot(Q.T,y)
    return solveU(R[:n+1],ys[:n+1])
