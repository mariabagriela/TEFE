# -*- coding: utf-8 -*-
"""Tefe29.09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/119SIVqvL0rymGVkZGlt6QObBxnQOlFu5
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12803112)

N = 10_000
nREP = 1000

def gerador(N):
  n = 0
  for i in range(N):
    u1 = np.random.rand()
    u2 = np.random.rand()
    if (u1**2+u2**2 <= 1):
      n +=1
  return n
p = gerador(N)/N
A = 4*p
sn = np.sqrt(N*p*(1-p))
sA = 4*sn/N

print(f' A = {A:.5g} \n sA = {sA:.5g} \n p = {p:.4} \n n = {gerador(N)} \n sn = {sn:.4}')

np.random.seed(12803112)
listan = []
listaA = []
for i in range(nREP):
  listan.append(gerador(N))
  listaA.append(gerador(N)*4/N)

print(f'snMonte = {np.std(listan, ddof =1):.5} \n sA = {np.std(listaA, ddof =1):.5}')

np.random.seed(12803112)
N = 10_000
nREP = 1000

def gerador2(N):
  n2 = 0
  for i in range(N):
    u1 = np.random.rand()
    u2 = np.random.rand()
    u3 = np.random.rand()
    if (u1**2 + u2**2 + u3**2 <= 1):
      n2 +=1
  return n2

p1 = gerador2(N)/N
B = 6*p1
sn = np.sqrt(N*p1*(1-p1))
sB = 6*sn/N

print(f' B = {B:.5g} \n sB = {sB:.5g} \n p = {p1:.4} \n n = {gerador2(N)} \n sn = {sn:.4}')

np.random.seed(12803112)
listan2 = []
listaB = []
for i in range(nREP):
  listan2.append(gerador2(N))
  listaB.append(gerador2(N)*6/N)

print(f'snMonte = {np.std(listan2, ddof =1):.5} \n sB = {np.std(listaB, ddof =1):.5}')