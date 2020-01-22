import numpy
import matplotlib.pyplot as plot

variavel = []
funcao = []

f = lambda x: 1/x**2
n = 100.0
a = 1.0
b = 7.0
h = (b - a)/n
integral = 0

for i in numpy.arange(a + h, b, h):
    integral += h * (f(i))
integral += (h/2) * (f(a) + f(b))

for i in numpy.arange(a, b, h):
    variavel.append(i)
    funcao.append(f(i))

plot.plot(variavel, funcao)

print(integral)