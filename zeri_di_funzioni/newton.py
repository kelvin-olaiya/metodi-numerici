# -*- coding: utf-8 -*-
"""
Metodo di newton
"""
import numpy as np

def newton(func, dfunc, x0, tolx, tolf, max_iterazioni):
    xks = []
    it = 0
    if not (abs(dfunc(x0) > np.spacing(1))): # per evitare di dividere per zero
        print("Derivata nulla in x0 - EXIT")    
        return [],it,xks
    d = func(x0)/dfunc(x0)
    xks.append(x0 - d)
    fxk = func(xks[it])
    it += 1
    while it < max_iterazioni and abs(fxk) >= tolf and abs(d) >= tolx*abs(xks[it-1]):
        x0 = xks[it-1]
        if not (abs(dfunc(x0) > np.spacing(1))):
            print("Derivata nulla in x0 - EXIT")
            return xks[it-1],it,xks
        d = func(x0)/dfunc(x0)
        xks.append(x0 - d)
        fxk = func(xks[it])
        it += 1
    if it == max_iterazioni:
        print("Numero massimo di iterazioni raggiunte")
    return xks[it-1],it,xks