# -*- coding: utf-8 -*-
"""
Metodo dei Trapezi
"""
import numpy as np

def trapezi_composita(func, a, b, n):
    h = (b-a)/n
    nodi = np.arange(a, b+h, h)
    f = func(nodi)
    return (f[0] + 2*np.sum(f[1:n]) + f[n])*h/2

def trap_toll(func, a, b, tol):
    N = 1
    err = 1
    IN = trapezi_composita(func, a, b, N)
    nmax = 2048
    while N < nmax and err > tol:
        N = 2*N
        I2N = trapezi_composita(func, a, b, N)
        err = abs(IN - I2N)/3 # ! focus here
        IN = I2N
    return IN, N