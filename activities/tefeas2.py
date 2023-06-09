# -*- coding: utf-8 -*-
"""TefeAs2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17fm9jF4LAW50MAbLj_M6BtCuFVqwhW9A
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

#Questão 1
np.random.seed(12557077)

N = 10000
K = M = 1000 

x0 = 50
s0 = 15

def med(N=10000, x0=50, s0=15): 
  x = np.random.randn(N)*s0 + x0

  media = np.mean(x)
  desvio = np.std(x,ddof=1)

  F =[]  
  n = 0  
  for j in range(1,4):
    n = sum([1 if (i >= (x0 - j*s0) and i <= (x0 +j*s0)) else 0 for i in x])
    F.append(n/N)
    n = 0
  return media, desvio, F , x

def Bootstrap(x):
  xB = []
  INDs= np.random.randint( 0, N, size=N)
  for ind in INDs:
    xB.append( x[ind] )
  return xB

m = [] 
d = [] 
fm = [] 
for i in range(M): 
  mdia, dvp, Fn , x = med()
  m.append(mdia)
  d.append(dvp)
  fm.append(Fn)

media, desv, F, x = med(N, x0, s0)
print(f"xm = {media:.5g}, sx = {desv:.5g}\n freq. rel. (1) = {F[0]:.5g} \n freq. rel. (2) = {F[1]:.5g} \n freq. rel. (3) = {F[2]:.5g} ")

m = np.array(m)
d = np.array(d)
fm = np.array(fm)
print(f'\n std_xm = {m.std():.5g} \n std_sx = {d.std():.5g}\n std_n1 = {N*np.std([x[0] for x in fm], ddof = 1):.5g}\n std_n2 = {N*np.std([x[1] for x in fm], ddof = 1):.5g}\n std_n3 = {N*np.std([x[2] for x in fm], ddof = 1):.5g}')

mB = []
dB = []
FB = [[],[],[]]

for i in range(K):
  xB = Bootstrap(x)
  mB.append(np.mean(xB))
  dB.append(np.std(xB, ddof = 1))
  n = 0  
  for j in range(1,4):
    n = sum([1 if (i >= (x0 - j*s0) and i <= (x0 +j*s0)) else 0 for i in xB])
    FB[j-1].append(n/N)
    n = 0

stdmB = np.std(mB,ddof = 1)
stddB = np.std(dB, ddof = 1)
stdFB = []
for j in range(1,4):
  stdFB.append(N*np.std(FB[j-1], ddof = 1))

print(f'\n stdm = {stdmB:.5g} \n stddB = {stddB:.5g}')
for i in range(0,3):
  print(f'stdnB = {N*np.std(FB[i],ddof = 1):.5g}')

#Questão 2
np.random.seed(12803112)
G = np.arange(0.1,10.1,0.1)
sig0 = (np.sqrt((1+G)/((9+3*G))))

plt.figure()
plt.xlabel('G')
plt.ylabel('$\sigma_0$')
plt.title('Gráfico de $\sigma_0$ por G')
plt.plot(G,sig0)
plt.plot(3,0.47,marker = '*', label = 'G = 3')
plt.legend()
plt.show()

P1 = (sig0/G * ((G+1)- (sig0)**G))
plt.figure()
plt.xlabel('G')
plt.ylabel('$\sigma_0$')
plt.title('Gráfico de $P_1$ por G')
plt.plot(G,P1)
plt.plot(3,0.61,marker = '*', label = 'G = 3')
plt.legend()
plt.show()

bsig0 = 2*sig0
bsig0[bsig0 > 1] = 1
P2 = ((bsig0/G) * ((G+1) - (bsig0)**G))
plt.figure()
plt.xlabel('G')
plt.ylabel('$\sigma_0$')
plt.title('Gráfico de $P_2$ por G')
plt.plot(G,P2)
plt.plot(3,0.994,marker = '*', label = 'G = 3')
plt.legend()
plt.show()

asig0 = 3*sig0
asig0[ asig0 >= 1] = 1
P3 = (((asig0)/G) * ((G+1)- (asig0)**G))
plt.figure()
plt.xlabel('G')
plt.ylabel('$\sigma_0$')
plt.title('Gráfico de $P_3$ por G')
plt.plot(G,P3)
plt.plot(3,1,marker = '*', label = 'G = 3')
plt.legend()
plt.show()

def geraDados(N=1, f=lambda x:(2-2*np.abs(x)**3)/3, xI=-1, xS=1, yMax=2/3 ):
  x = []
  while( len(x)<N ):
    xc = np.random.rand()*(xS-xI) + xI
    yv = yMax * np.random.rand()
    if yv<=f(xc):
      x.append(xc)
  return x
N = 10000
x = geraDados(N)
xm = np.mean(x)
sx = np.std(x,ddof=1)
n1 = n2 = n3 = 0

for i in range(len(x)):
  if np.abs(x[i]) <= sx:
    n1 += 1 ; n2 += 1 ; n3 += 1
  elif np.abs(x[i]) <= 2*sx:
    n2 += 1 ; n3 += 1
  elif np.abs(x[i]) <= 3*sx:
    n3 += 1

F1 = n1/N ; F2 = n2/N ; F3 = n3/N

print(f'xm = {xm:.5g}')
print(f'sx = {sx:.5g}')
print(f'n1 = {n1}, com F1 = {F1} \nn2 = {n2}, com F2 = {F2} \nn3 = {n3}, com F3 = {F3} \n')

x0 = 0
s0 = np.sqrt(2)/3

sxm , ssx , sF1 , sF2 , sF3  = [] , [] , [] , [], []
for i in range(1000):
  valor = geraDados(N,f=lambda x:(2-2*np.abs(x)**3)/3, xI=-1, xS=1, yMax=2/3)
  sxm.append(np.mean(valor))
  ssx.append(np.std(valor, ddof=1))
  for j in range (1,4):
    n = 0
    n = sum([1 if (k >= (x0 - j*s0) and k <= (x0 +j*s0)) else 0 for k in valor])
    if j == 1:
      sF1.append(n/N)
    elif j == 2:
      sF2.append(n/N)
    elif j == 3:
      sF3.append(n/N)


sigxm = np.std(sxm, ddof=1)
sigsx = np.std(ssx,ddof=1)
sigF1, sigF2, sigF3 = np.std(sF1, ddof=1),np.std(sF2, ddof=1),np.std(sF3, ddof=1)

print(f'sigma_xm = {sigxm:.5g} \nsigma_sx = {sigsx:.5g} \nsigmaF1 = {sigF1:.5g} \nsigmaF2 = {sigF2:.5g} \nsigmaF3 = {sigF3:.5g} ')

#Questão 3
np.random.seed(12803112)
def dados(N=10000):
  x = []
  y = []
  c = 0 #contador
  while c < N:
    x_a = np.random.uniform(low = -1, high = 1)
    y_a = np.random.uniform(low = 0, high = 3/2)
    if 3*(x_a**2)/2 > y_a:
      x.append(x_a)
      y.append(y_a)
      c +=1
  return x,y

M=[1,2,3,5,10,100]
tab = [1, 1.5, 2, 2.5, 3]

for M in M:
  valor, aux = dados(M*10_000)

  y_b = np.empty(10000)
  aux_b = np.empty(10000)

  for i in range(10000):
    y_b[i] = sum(valor[M*i:(i+1)*M])
    aux_b[i] = sum(aux[M*i: M*(i+1)])

  N_b = []
  std_yb = y_b.std()
  for j in tab:
    num = 0
    for i in y_b:
      if abs(i) < j*std_yb:
        num += 1
    N_b.append(num)
  print(f'Resultado para M = {M}')

  for k in N_b:
    print(f'N = {k}')

  skew_b = sp.skew(y_b)
  kurt_b = sp.kurtosis(y_b)

  print(f'Skew = {skew_b:.2f},Kurtosis = {kurt_b:.2f}, média =  {np.mean(y_b)} , desvio = {std_yb} ')

#Questão 4
np.random.seed(12803112)

def dados4(N=10000):
  x = []
  y = []
  count = 0
  while count < N:
    g = np.random.uniform()  
    x_aux = -np.log(1 - g)
    y_aux = np.exp(-x_aux)
    x.append(x_aux)
    y.append(y_aux)
    count +=1
  return x,y

M=[1,2,3,5,10,100]
table = [1, 1.5, 2, 2.5, 3]

for M in M:
  valor, aux = dados4(M*10_000)

  y_b = np.empty(10000)
  aux_b = np.empty(10000)

  for i in range(10000):
    y_b[i] = sum(valor[M*i:(i+1)*M])
    aux_b[i] = sum(aux[M*i: M*(i+1)])


  N_b = []
  std_yb = y_b.std()
  mean_yb = y_b.mean()
  for j in table:
    num = 0
    for i in y_b:
      if abs(i) < mean_yb + j*std_yb:
        num += 1
    N_b.append(num)
  print(f'Resultados para M = {M}')


  for k in N_b:
    print(f'N = {k}')

  skew_b = sp.skew(y_b)
  kurt_b = sp.kurtosis(y_b)

  print(f'Skew = {skew_b:.2f},Kurtosis = {kurt_b:.2f} , média =  {np.mean(y_b)}, desvio = {std_yb}')