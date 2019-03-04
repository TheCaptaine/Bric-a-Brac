#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:55:56 2019

@author: 3872558
"""

import numpy as np

def euler_2D(F, U0, ti, tf, N):
    dt = (tf-ti)/N
    tk, uk = np.empty(N+1), np.empty(N+1)
    tk[0], uk[0] = 0, U0
    
    for j in range(N):
        tk[j+1] = ti+j*dt 
        uk[j+1] = uk[j]+F(uk[j])*dt
        
    return np.array([tk, uk])