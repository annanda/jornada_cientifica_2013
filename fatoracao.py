# -*- coding: utf-8 -*-
from math import sqrt

def mdc(a,b):
    """
    Para calcular o mdc entre dois números inteiros a e b
    Exemplo:
        mdc(3,12)
            retorna 3
    """
    r1 = a % b
    while r1 is not 0:
        r2 = b % r1
        b = r1
        r1 = r2
    return b


def fatoracao_trivial(n):
    """
    Calcula o menor fator inteiro de um numero inteiro composto
    Exemplo:
        fatoracao_trivial(15)
            retorna 3
    """
    F = 2
    while F <= (int)(sqrt(n)):
        if n % F is 0:
            return F
        else:
            F = F+1
    return n #nesse caso ele é primo



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
    Para fatorar o numero inteiro pelo algoritmo de fatoracao trivial completo
    Retorna uma instância da classe RetornoTrivialCompleta.
    Exemplo:
        retorno_fatoracao = fatoracao_trivial_completa(10)
            Para acessar a lista de fatores: retorno_fatoracao.list_fatores
                [2,5]
            Para acessar a lista de expoentes: retorno_fatoracao.list_expoentes
                [1,1]
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
    Para fatorar o numero inteiro pelo algoritmo de fermat
    Retorna dois números
    Exemplo:
        fermat(15)
            retorna [3,5]
    """
    y = 0
    while n % 2 is 0:
        n = n/2
    if n is 1:
        return [1,1]
    x = (int)(sqrt(n))

    while n is not ((x**2) - (y**2)):
        x = x+1
        y = (int)(sqrt(x**2 - n))
        if x is ((n+1) / 2):
            return [1,n]
    return [x+y, x-y]


def crivo(n):
    """
    Calcula uma lista de primos de 2 até o número passado como parâmetro.
    Exemplo:
        crivo(10)
            retorna [2,3,5,7]
    """
    x = []
    y = 3
    z = 1
    auxiliar = 0 #no axiom aqui era 1, pois o indice começava em 1
    lista_final = [2]

    while y <= n:
        x.append(y)
        y = y + 2

    y2 = x[z-1]

    while y2 <= (int)(sqrt(n)):
        z = auxiliar
        while z < len(x):
            z = z + y2
            if z < len(x):
                x[z] = 0
        y2 = y2 + 2
        auxiliar += 1
    z = 0

    while z < len(x):
        if x[z] is not 0:
            lista_final.append(x[z])
        z = z + 1
    return lista_final
