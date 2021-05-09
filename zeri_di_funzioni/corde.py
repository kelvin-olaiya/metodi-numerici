# -*- coding: utf-8 -*-
"""
Metodo delle corde
"""

def corde(func, dfunc, x0, tolx, tolf, max_iterazioni):
    xks = []
    it = 0
    m = dfunc(x0)
    d = func(x0)/m # corrisponde all' "incremento"
    xks.append(x0 - d) # x1
    fxk = func(xks[it]) # fx1
    it += 1
    while it < max_iterazioni and abs(fxk) >= tolf and abs(d) >= tolx*abs(xks[it]):
        x0 = xks[it-1] # it-1 perche parto xks parte da x1
        d = func(x0)/m
        xks.append(x0 -d)
        fxk = func(xks[it])
        it += 1
    if it == max_iterazioni:
        print("Numero massimo di iterazioni raggiunto")
    return xks[it-1],it,xks
    
