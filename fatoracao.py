# -*- coding: utf-8 -*-
import math

def mdc(a,b):
    """
    Para calcular o mdc entre dois números a e b
    """
    r1 = a % b
    while r1 is not 0:
        r2 = b % r1
        b = r1
        r1 = r2
    return b

def fatoracao_trivial(n):
    """
    Calcula o menor fator de um numero composto
    """
    F = 2
    while F <= n and n > 1:
        if n % F is 0:
            return F
        else:
            F = F+1


class RetornoTrivialCompleta(object):
    """
    Classe criada para tratar com o retorno da funcao
    fatoracao_trivial_completa que tem como atribulos as listas de fatores:
    list_fatores e de expoentes: list_expoentes
    """
    def __init__(self,list_fatores, list_expoentes):
        """
        Contrutor parametrizado da classe
        """
        self.list_fatores = list_fatores
        self.list_expoentes = list_expoentes
    def __str__(self):
        """
        Método To String
        """
        return "Fatores: %s, Expoentes: %s" % (list_fatores,list_expoentes)

def fatoracao_trivial_completa(n):
    """
    Para fatorar o numero pelo algoritmo de fatoracao trivial completo
    """

    expoente = 0
    list_fatores = []
    list_expoentes = []

    while n > 1:
        f = fatoracao_trivial(n)
        while n % f is 0:
            expoente += 1
            n = n/f
        list_fatores.append(f)
        list_expoentes.append(expoente)
        expoente = 0
    return RetornoTrivialCompleta(list_fatores,list_expoentes)

def fermat(n):
    """
    Para fatorar o numero pelo algoritmo de fermat
    """
    y = 0
    while n % 2 is 0:
        n = n/2
    if n is 1:
        return [1,1]
    x = (int)(math.sqrt(n))

    while n is not ((x**2) - (y**2)):
        x = x+1
        y = (int)(math.sqrt(x**2 - n))
        if x is ((n+1) / 2):
            return [1,n]
    return [x+y, x-y]

def crivo(n):
    """
    Calcula uma lista de primos de 2 até o número passado como parâmetro.
    """
    x = []
    y = 3
    z = 1
    auxiliar = 1
    lista_final = [2]

    while y <= n:
        x.append(y)
        y = y + 2
    y = x*z

    while y < (int)math.sqrt(n):
        z = auxiliar
        while z <= len(x):
            z = z + y
            if z <= len(x):
                x[z] = 0 #onde comeca o indice no axiom
        y = y + 2
        auxiliar += 1
    z = 1

    while z <= len(x):
        if x[z] is not 0:
            lista_final.append(x[z])
        z = z + 1
    return lista_final
