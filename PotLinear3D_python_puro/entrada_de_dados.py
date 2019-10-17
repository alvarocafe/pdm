# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:08:57 2017
@author: eder

= = = =  E X E M P L O   D E   U S O  = = = =
def dad1():
    # Nome do arquivo que contém a geometria
    arquivo = 'viga'

    # Condição de contorno de cada superfície
    # CCSup = {Superfície: [Tipo da CDC, Valor da CDC]}
    #    Tipo da CDC = 0 ==> a tempemperatura é conhecida
    #    Tipo da CDC = 1 ==> o fluxo é conhecido
    #    Tipo da CDC da superfície não definido: assumido fluxo zero por padrão
    CCSup = {0:[0,0],1:[0,1]}

    # Condutividade térmica do material [W/m²K]
    k = 1

    return arquivo,CCSup,k
"""

def dad1():
    arquivo = 'viga'
    CCSup = {0:[0,0],1:[0,1]}
    k = 1
    return arquivo,CCSup,k

def dad2():
    arquivo = 'Placa_furo'
    CCSup = {3:[0,0],1:[0,1]}
    k = 1
    return arquivo,CCSup,k

def dad3():
    arquivo = 'L'
    CCSup = {3:[0,0],1:[0,1]}
    k = 1
    return arquivo,CCSup,k

def dad4():
    arquivo = 'Tutorial_v4'
    CCSup = {12:[0,0],5:[0,1]}
    k = 1
    return arquivo,CCSup,k
