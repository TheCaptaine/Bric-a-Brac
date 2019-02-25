#Alexandre BOUGAKOV

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np 
import scipy.integrate as integration

longueur_onde = 0.5e-3
D = 10
d = 1
s = 10

#Q1
difference_de_marche = lambda ys, X : np.sqrt(X**2+(Y-d/2)**2+D**2)+np.sqrt((ys-d/2)**2+s**2)-np.sqrt(X**2+(Y+d/2)**2+D**2)-np.sqrt((ys+d/2)**2+s**2)

I = lambda x : 4*np.cos(np.pi*x/longueur_onde)**2
Y = np.linspace(-0.01, 0.01, 1000)


plt.plot(Y, I(difference_de_marche(0, 0)), 'r-', label='X=0')
plt.plot(Y, I(difference_de_marche(0, 10)), 'b-', label='X=10')
plt.xlabel('Y/mm')
plt.ylabel('Intensity/a.u')
plt.title('I(X,Y,ys)')
plt.legend(loc='upper right')
plt.xticks(np.arange(-0.01, 0.015, 0.005))
plt.axis([-0.01, 0.01, 0, 4])
plt.show()

plt.plot(Y, I(difference_de_marche(0, 0)), 'r-', label='X=0')
plt.plot(Y, I(difference_de_marche(0.001, 0)), 'k-', label='X=0.001')
plt.legend(loc='upper right')
plt.xticks(np.arange(-0.01, 0.015, 0.005))
plt.xlabel('Y/mm')
plt.ylabel('Intensity/a.u')
plt.axis([-0.01, 0.01, 0, 4])
plt.show()

#Q2
def intensity(ys, X, Y, R, d, D, s, longueur_onde):
    return 4/R*np.cos(np.pi*(np.sqrt(X**2+(Y-d/2)**2+D**2)+np.sqrt((ys-d/2)**2+s**2)-np.sqrt(X**2+(Y+d/2)**2+D**2)-np.sqrt((ys+d/2)**2+s**2))/longueur_onde)**2
def expint(X, Y, R, d, D, s, longueur_onde):
    return integration.quad(intensity, -R/2, R/2, args=(X, Y, R, d, D, s, longueur_onde))[0]

#Q3
vec_expint = np.vectorize(expint)
plt.plot(Y, vec_expint(0, Y, 1e-6, d, D, s, longueur_onde), 'r-', label='R=1e-6')
plt.plot(Y, vec_expint(0, Y, 2e-3, d, D, s, longueur_onde), 'b-', label='R=2e-3')
plt.plot(Y, vec_expint(0, Y, 3e-3, d, D, s, longueur_onde), 'k-', label='R=3e-3')
plt.plot(Y, vec_expint(0, Y, 4e-3, d, D, s, longueur_onde), 'g-', label='R=4e-3')
plt.xlabel('Y/mm')
plt.ylabel('Intensity/a.u')
plt.title('I(X,Y,R)')
plt.legend(loc='upper right')
plt.xticks(np.arange(-0.01, 0.015, 0.005))
plt.axis([-0.01, 0.01, 0, 4])
plt.show()

#Q4
X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-0.01, 0.01, 100))
Z = vec_expint(X, Y, 1e-6, d, D, s, longueur_onde)
plt.title('I(X,Y,R)')
plt.imshow(Z, cmap=plt.cm.gray, vmax=10,vmin=-10)
