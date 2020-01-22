#!/usr/bin/env python
# coding: utf-8

# Interpolação


# importação de bibliotecas
from __future__ import division
import numpy as np
from numpy import linalg
from numpy.polynomial import polynomial as poly
import matplotlib.pyplot as plt


# listas com valores de x e y para cada uma das coordenadas
xi = np.array([0,1,2,3], dtype='double')
yi = np.array([1,6,5,-8], dtype='double')


# In[80]:


# Interpolação polinomial
"""
Através das coordenadas x e y, calcula-se a função polinomial 
A: matriz de constantes
a: constantes da função polinommial
"""
A = np.array([xi**3,xi**2,xi**1,xi**0]).transpose()
a = np.linalg.inv(A).dot(yi);
a
# -x**3 +6x +1

# Plotando o gráfico
"""
linspace: espaço em x onde a função será localizada
plot: plota a função
grid: mostra as grades
"""
xx = np.linspace(-0.5,3.25);
plt.plot(xi,yi,'ro',xx,np.polyval(a,xx))
plt.grid()
plt.show()