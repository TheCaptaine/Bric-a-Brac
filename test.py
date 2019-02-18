#Alexandre BOUGAKOV

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fmin, fsolve

longueur_onde = 0.5e-3
D = 10
d = 1
s = 10

#Q1
difference_de_marche = lambda X, Y, d, D, ys, s : np.sqrt(X**2+(Y-d/2)**2+D**2)+np.sqrt((ys-d/2)**2+s**2)-np.sqrt(X**2+(Y+d/2)**2+D**2)-np.sqrt((ys+d/2)**2+s**2)

I = lambda x : 4*np.cos(np.pi*x/longueur_onde)**2
Y = np.linspace(-0.01, 0.01, 1000)


plt.plot(Y, I(difference_de_marche(0, Y, d, D, 0, 10)), 'r-', label='X=0')
plt.plot(Y, I(difference_de_marche(10, Y, d, D, 0, 10)), 'b-', label='X=10')
plt.xlabel('Y/mm')
plt.ylabel('Intensity/a.u')
plt.title('I(X,Y,)')
plt.legend(loc='upper right')
plt.xticks(np.arange(-0.01, 0.015, 0.005))
plt.axis([-0.01, 0.01, 0, 4])
plt.show()

plt.plot(Y, I(difference_de_marche(0, Y, d, D, 0, 10)), 'r-', label='X=0')
plt.plot(Y, I(difference_de_marche(0, Y, d, D, 0.001, 10)), 'k-', label='X=0.001')
plt.legend(loc='upper right')
plt.xticks(np.arange(-0.01, 0.015, 0.005))
plt.xlabel('Y/mm')
plt.ylabel('Intensity/a.u')
plt.axis([-0.01, 0.01, 0, 4])
plt.show()

