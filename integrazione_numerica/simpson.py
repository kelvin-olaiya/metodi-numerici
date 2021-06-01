# -*- coding: utf-8 -*-
"""
Metodo dei Simpson
"""
import numpy as np

def simpson_composita(func, a, b, n):
    h = (b-a)/2*n # ! focus here
    nodi = np.arange(a, b+h, h)
    f = func(nodi)
    return (f[0] + 2*np.sum(f[2:2*n:2]) + 4*np.sum(f[1:2*n:2]) + f[n])*h/3 # ! focus here

def simp_toll(func, a, b, tol):
    N = 1
    err = 1
    IN = simpson_composita(func, a, b, N)
    nmax = 2048
    while N < nmax and err > tol:
        N = 2*N
        I2N = simpson_composita(func, a, b, N)
        err = abs(IN - I2N)/15 # ! focus here
        IN = I2N
    return IN, N
