# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 02:11:52 2017

@author: Ricardo
"""
import random
import math

def random_climb(pSubir, nPassos): #returns vector of walk path
    level = 1 # This variable is optional
    h = [level]
    for i in range(nPassos):
        if random.random() <= pSubir:
            level *= 1.001
        else:
            level /= 1.001
        h.append(level)
    return h






pSubir = 0.500
nPassos = 1000000
h1 = random_climb(pSubir, nPassos)
h2 = random_climb(pSubir, nPassos)

import matplotlib.pyplot as plt
plt.plot(h1)
plt.plot(h2)
            
