# -*- coding: utf-8 -*-
"""
Metodo d'iterazione
"""

def iterazione(gfunc, x0, tolx, max_iterazioni):
    xks = []
    it = 0
    xks.append(x0)
    xks.append(gfunc(xks[it]))
    it += 1
    d = xks[it] - xks[it-1]
    while it < max_iterazioni and abs(d) >= tolx*abs(xks[it]):
        xks.append(gfunc(xks[it]))
        it += 1
        d = xks[it] - xks[it-1]
    if it == max_iterazioni:
        print("Raggiunto numero massimo di iterazioni")
    return xks[it-1],it,xks