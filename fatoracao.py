# -*- coding: utf-8 -*-

def mdc(a,b):
    "Para calcular o mdc entre dois números a e b"
    r1 = a % b
    while r1 is not 0:
        r2 = b % r1
        b = r1
        r1 = r2
    return b
