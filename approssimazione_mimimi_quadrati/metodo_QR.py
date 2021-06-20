# -*- coding: utf-8 -*-
"""
Approssimazione con metodo QR
"""
import numpy as np
import scipy.linalg as spl

def Usolve(U, b):
    m,n = U.shape
    if m != n and not np.all(U.diag()):
        print("Metodo non applicabile")
        return []
    x = np.zeros((n,1))
    for k in reversed(range(n)):
        sommatoria = np.dot(U[k,k+1:], x[k+1:])
        x[k] = (b[k] - sommatoria) / U[k,k]
    return x

def metodoQR(x,y,n):
    Q,R = spl.qr(np.vander(x,n+1))
    ys = np.dot(Q.T,y)
    return Usolve(R[n+1:],ys[n+1:])
