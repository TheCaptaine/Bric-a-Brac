#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:28:40 2019

@author: 3872558
"""
import numpy as np

k = 9.81**0.5

def F(x):   
    return np.array([list(x)[0], -k**2*np.sin(list(x)[1])])
