# -*- coding: utf-8 -*-
"""
Metodo di bisezione
"""
import numpy as np
import math

# funzione di utility, restituisce il segno di x
# la funzione copysign(a,b) del modulo math restituisce un numero
# che ha il modulo di a e il segno di b
def sign(x):
    return math.copysign(1,x)

def bisezione(func, a, b, tol):
    # Verifico che il metodo sia applicabile
    if sign(func(a)) == sign(func(b)):
        return [],0,[]   
    # Per il metodo di bisezione e possibile conoscere a priori
    # massimo numero di iterazioni
    max_iterazioni = int(math.ceil(math.log((b-a)/tol)/math.log(2)))
    xks = []
    it = 0
    eps = np.spacing(1)
    while it < max_iterazioni and abs(b-a) >= tol + eps*max(abs(a), abs(b)):
        xks.append(a + (b-a)*0.5)  # Per calcolare il punto medio, utilizzo la formula stabile
        fxk = xks[it]
        if func(fxk) == 0:
            return xks[it],it+1,xks
        elif sign(fxk) == sign(func(a)):
            a = xks[it]
        elif sign(fxk) == sign(func(b)):
            b = xks[it]
        it += 1
    return xks[it-1],it,xks # (zero, num_iterazioni, vettore di xk)
    
    
    