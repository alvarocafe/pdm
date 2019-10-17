# -*- coding: utf-8 -*-
"""
Universidade de Brasília
Departamento de Engenharia Mecânica
Brasília, setembro de 2019

Programa de elementos de contorno aplicado a problemas de condução de
calor tri-dimensional sem fontes de calor concentradas

Tipo de elementos: Triangulares lineares contínuos

Autores: Éder Lima de Albuquerque
         Gustavo Silva Vaz Gontijo (ggontijo@gmail.com)

Última modificação: 17/09/2019 - 08h48min
"""

#%% BIBLIOTECAS E ARQUIVOS NECESSÁRIOS

#from mesh import Mesh
#import entrada_de_dados
import dad_cubo
import contorno
import sistema
import numpy as np
import resultados
import time

#%% ENTRADA DE DADOS E PRÉ-PROCESSAMENTO

t_inicio = time.time()
print('\nPrograma iniciado.')

# Lê o arquivo de entrada de dados
#arquivo, CCSup, k = entrada_de_dados.dad2()

# Cria a malha
#malha = Mesh() # Instancia a classe Mesh, criando o objeto malha
#malha.read_msh(arquivo + '.msh') # Executa o método read_msh do objeto malha
#NOS = malha.Verts
  # NOS: Matriz [NNx3] que contém as coordenadas dos vértices da malha criada,
  #      onde NN é o número de nós do problema

# Lê apenas os elementos triangulares [[physid],[nodes]]
#                       (physid is the surf of the elem)
#ELEM = malha.Elmts[2][1]-1
  # ELEM: Matriz [NEx3] que contém os números dos nós que formam cada elemento,
  #       onde NE é o número de elementos do problema

#SUP = malha.Elmts[2][0]-1
  # SUP: Matriz [NEx1] que contém o número da superfície à qual cada elemento
  #      pertence

NOS, ELEM, SUP, CCSup, k = dad_cubo.dad_cubo2()

# Cria a matriz de condições de contorno dos elementos
CDC = contorno.gera_CDC(CCSup, SUP, ELEM)
  # CDC: Matriz [NEx4] que contém a condição de contorno de cada nó dos
  #      elementos

#%% MONTAGEM E SOLUÇÃO DO SISTEMA

# Calcula as matrizes H e G
H, G = sistema.cal_HeG(NOS, ELEM, k)

  # H: Matriz [NNxNN] que contém o resultado da integração de q* no contorno
  # G: Matriz [NNx3NE] que contém o resultado da integração de T* no contorno

#A, b, T_pr = sistema.aplica_cdc(G, H, NOS, ELEM, CDC)
#
#  # A: Matriz [NNxNN] contendo colunas de H e G
#  # b: Vetor [NNx1] resultante da multiplicação de N colunas de H e G pelas
#  #    CDC's conhecidas
#
## Resolve o sistema de equações A.x = b
#x = np.linalg.solve(A, b)
#  # x: Vetor [NNx1] que contém os termos calculados (antes desconhecidos) de
#  #    temperatura e fluxo
#
## Separa os valores de temperatura e fluxo
#T, q = sistema.monta_Teq(NOS, ELEM, CDC, x, T_pr)
#  # T: Vetor [NNx1] que contém os valores de temperatura calculados
#  # q: Vetor [3NEx1] que contém os valores de fluxo calculados
##  
##  
#  
#print("T: ")
#print(T)
#print("q: ")
#print(q)

#
#
## Calcula os valores de temperatura no centróide do elemento
#T_centroide = contorno.calcTcentroide(T,ELEM,NOS)
  # T_centroide: Vetor [NEx1] que contém os valores de temperatura interpolados
  #              no centróide do elemento

# Mostra os valores de temperatura no mapa de cor
# resultados.mostra_resultados(ELEM, NOS, T_centroide)

#print('Tempo de processamento:',time.time()-t_inicio,'s.\nPrograma finalizado.')