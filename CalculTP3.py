import matplotlib.pyplot as plt 
import numpy as np 
import pylab

def _fit():
	return

""" Paramètres """

Kb = 1.38064852*10**-23  # J.K^-1
n0 = 2*10**25			 # m^-3
m = 4.8*10**-26			 # kg
g = 9.81				 # m.s^-2
T = 300					 # Kelvin
Io = 400				 # W.m-2
sigma = 4*10**-22 		 # m^2
k = 0.2					 # J^-1

H = Kb*T/(m*g)
z = np.linspace(100000, 200000, 1000)
n = n0*np.exp(-z/H)
I = Io*np.exp(-sigma*n0*np.exp(-z/H)*H)
q = k*sigma*n*I


z = np.linspace(0, 300000, 1000)
plt.plot(q, z)  
plt.axis([10**-11, 10**-1, 10**5, 4*10**5])
pylab.ticklabel_format(axis='y',style='sci',scilimits=(1,4))
plt.show()