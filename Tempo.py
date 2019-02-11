# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import fmin, fsolve

""" Paramètres """

Kb = 1.38064852e-23     # J.K^-1
n0 = 2e25			     # m^-3
m = 4.8e-26			# kg
g = 9.81				    # m.s^-2
T = 300			       # Kelvin
Io = 400				    # W.m-2
sigma = 4e-22 		 # m^2
k = 0.2					 # J^-1

H = Kb*T/(m*g)
z = np.linspace(100000, 300000, 1000)

n_funct = lambda z : n0*np.exp(-z/H)
I_funct = lambda n : Io*np.exp(-sigma*n*H)
q_funct = lambda n, I : k*sigma*n*I

q = lambda z : k*sigma*n0*np.exp(-z/H)*Io*np.exp(-sigma*n0*np.exp(-z/H)*H)

moinsq = lambda z : -k*sigma*n0*np.exp(-z/H)*Io*np.exp(-sigma*n0*np.exp(-z/H)*H)
zmax = fmin(moinsq, 10**5)[0]
print("zmax = {}, q(zmax) = {}".format(zmax, q(zmax)))

d = q(zmax)/1000
z1 = fsolve(lambda z : q(z)-d, 150000)
z2 = fsolve(lambda z : q(z)-d, 250000)  
print("q = qmax/1000 = {}, z1 = {}, z2 = {}".format(d, z1, z2))

plt.xscale('log')
plt.yscale('log')
plt.plot(q(z), z, 'k-', q(zmax), zmax, 'rx', q(z1), z1, 'r.', q(z2), z2, 'r.', ) 
plt.axis([10**-11, 10**-0, 10**5, 4*10**5])
plt.show()
