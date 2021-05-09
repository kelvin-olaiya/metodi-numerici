# -*- coding: utf-8 -*-
"""
Metodo di falsa posizione
"""
import numpy as np
import math

def sign(x):
    return math.copysign(1, x)

def regula_falsi(func, a, b, tol, max_iterazioni):
    # Verifico che il metodo sia applicabile
    if sign(func(a)) == sign(func(b)):
        return [],0,[]
    
    xks = []
    it = 0
    eps = np.spacing(1)
    fxk = func(a) # Qui ne ho bisogno per il controllo sul residuo
    while it < max_iterazioni and abs(fxk) >= tol and abs(b-a) >= tol + eps*max(abs(a), abs(b)):
        fa = func(a)
        fb = func(b)
        xks.append(a - fa*(b-a)/(fb-fa))
        fxk = func(xks[it])
        if fxk == 0:
            break
        elif sign(fxk) == sign(fa):
            a = xks[it]
        elif sign(fxk) == sign(fb):
            b = xks[it]
        it += 1
    if it == max_iterazioni:
        print("Raggiunto il massimo numero di iterazioni")
    return xks[it-1],it,xks
    

