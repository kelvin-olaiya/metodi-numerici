# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:57:15 2021

@author: kelvi
"""

import numpy as np

# Restituisce i coefficienti del k-esimo polinomio
# di Lagrange
def polinomioLagrange(xnodi,k):
    n = xnodi.size
    if k == 0:
        xzeri = xnodi[1:n]
    else:
        xzeri = np.append(xnodi[0:k],xnodi[k+1:n])
    num = np.poly(xzeri) # np.poly restituisce i coeff. del polinomi che ha per zeri xzeri
    den = np.polyal(num,xnodi[k]) # Il denominatore e il numeratore valutato in xk --> quindi e un numero
    return num/den

def interpolazione(x, f, xx):
    n = x.size
    m = xx.size
    L = np.zeros((m,n))
    for k in range(n):
        L[k,:] = np.polyval(polinomioLagrange(x,k), xx)
    return np.dot(f,L)