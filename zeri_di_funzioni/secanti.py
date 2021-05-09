# -*- coding: utf-8 -*-
"""
Metodo delle secanti
"""

# Funzione di comodo per il calcolo dell'incremento d
def calcola_d(func, xm1, x0):
    return func(x0)*(x0 -xm1)/(func(x0-func(xm1)))

def secanti(func, xm1, x0, tolx, tolf, max_iterazioni):
    xks = []
    it = 0
    d = calcola_d(func, xm1, x0)
    xks.append(x0 - d)
    fxk = func(xks[it])
    it += 1
    while it < max_iterazioni and abs(fxk) > tolf and abs(d) >= tolx*abs(xks[it-1]):
        xm1 = x0
        x0 = xks[it-1]
        d = calcola_d(func, xm1, x0)
        xks.append(x0 - d)
        fxk = func(xks[it])
        it += 1
    if it == max_iterazioni:
        print("Numero massimo di iterazioni raggiunto")
    return xks[it -1],it,xks