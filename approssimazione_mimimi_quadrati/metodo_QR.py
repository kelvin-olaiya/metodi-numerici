# -*- coding: utf-8 -*-
"""
Approssimazione con metodo QR
"""
import numpy as np
import scipy.linalg as spl
from sistemi_lineari import solveU

def metodoQR(x,y,n):
    Q,R = spl.qr(np.vander(x,n+1))
    ys = np.dot(Q.T,y)
    return solveU(R[:n+1],ys[:n+1])
