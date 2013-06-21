# -*- coding: utf-8 -*-
import math

def mdc(a,b):
    "Para calcular o mdc entre dois números a e b"
    r1 = a % b
    while r1 is not 0:
        r2 = b % r1
        b = r1
        r1 = r2
    return b

def fatoracao_trivial_completa(n):
    "Para fatorar o numero pelo algoritmo de fatoracao trivial completo"
    pass

def fermat(n):
    "Para fatorar o numero pelo algoritmo de fermat"
    y = 0
    while n % 2 is 0:
        n = n/2
    if n is 1:
        return [1,1]
    x = (int)(math.sqrt(n))

    while n is not (x**2) - (y**2):
        x = x+1

        y = (int)(math.sqrt(x**2 - n))

        if x is (n+1 / 2):
            return [1,n]

    return [x+y, x-y]
