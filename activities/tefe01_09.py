# -*- coding: utf-8 -*-
"""Tefe01.09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15sqxPd7GFmX22EsPaDBj9MetmST-4H_Y
"""

import numpy as np
import matplotlib as plt

np.random.seed(12803112)
x0 = 100
s0 = 10
n = 25
N = 100
NRep = 10000

def simExpA(N, s0, x0):
  x = []
  for i in range(N):
    erroAleat = s0*np.random.randn()
    x.append(x0 + erroAleat)
  media =  np.mean(x)
  mediana = np.median(x)
  dsvpad = np.std(x)

  return media, mediana, dsvpad

X = [[],[],[]]
for j in range(NRep):
  xmedia,xmediana,xdsvpad = simExpA(25,10,100)
  values = [xmedia, xmediana, xdsvpad]
  for k in range(3):
    X[k].append(values[k])
  
smedia = np.std(X[0], ddof = 1)
smediana = np.std(X[1], ddof = 1)
sdsvpad = np.std(X[2], ddof = 1)

print(f'Desvio da média = {smedia:.4f} \n Desvio da mediana = {smediana:.4f} \n Desvio padrão amostral = {sdsvpad:.4f}' )