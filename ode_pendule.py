#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:20:41 2019

@author: 3872558
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
L = 1
k = (g/L)**0.5
N = 1000
tf = 3*(2*np.pi/k)
ti = 0
dt = (tf-ti)/N

omega = np.empty(N+1);omega[0]=0
theta = np.empty(N+1);theta[0]=np.pi/4

for j in range(N):
    theta[j+1] = theta[j]+omega[j]*dt
    omega[j+1] = omega[j]-k**2*np.sin(theta[j])*dt
    

plt.subplot(211)
plt.ylabel('angle (rad)')
plt.plot(np.linspace(ti,tf,N+1),theta)

plt.subplot(212)
plt.ylabel('vitesse angulaire (rad/s)')
plt.xlabel('temps (s)')
plt.plot(np.linspace(ti,tf,N+1),omega)

print(list(np.array([2,3,6])))