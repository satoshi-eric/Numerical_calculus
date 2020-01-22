import numpy as np
import scipy
from math import sqrt

def integrar_multi(x):
    yinf = 0.650
    b = yinf
    a = 0
    n = 100
    h = (b - a)/n
    integral = 0
    integral += (h/2)*(a**2)/sqrt(x**2 + a**2)
    integral += (h/2)*(b**2)/sqrt(x**2 + b**2)
    for y in np.arange(a + h, b, h):
        integral += h*(y/sqrt(x**2 + y**2))
    return integral

x0 = 0.005
yinf = 0.650

f = lambda x: x - x0 - 3*integrar_multi(x)

print(f(0.43116952523245355))



