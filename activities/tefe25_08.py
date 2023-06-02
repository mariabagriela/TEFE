# -*- coding: utf-8 -*-
"""Tefe25.08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P4Qn-W2JakTuOZlgK5gcHzsP4Op0jNGs
"""

# integração por Monte Carlo
import numpy as np
f = lambda x: np.exp(np.sin(x))

def IntegraExpSeno():
  xi = 0
  xf = 2*np.pi
  ymax = np.exp(1)
  N = 10_000
  n = 0
  for i in range(N):
    x = xi + (xf-xi)*np.random.rand()
    y = ymax * np.random.rand()
    if y<=f(x):
      n+=1
  Area = (n/N)*(xf-xi)*ymax
  print(Area)
IntegraExpSeno()