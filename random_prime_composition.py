# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 00:23:32 2017

@author: Ricardo
"""
import random
import math

probElem = 0.5
novoPrimo = 0.5


def nextPrime(now):
    for i in (range(2,now+1)):
        if((now+1)%i==0):
            return nextPrime(now+1)
    return(now+1)
        

def gen_composite(probElem, novoPrimo):
    num = 1
    while(random.random()<novoPrimo):
        primo = 2
        while(random.random()<probElem):
            primo = nextPrime(primo)
        num *= primo
    return num
    
import matplotlib.pyplot as plt
x = [gen_composite(0.70, 0.9) for i in range(10000)]
y = sorted([math.log(i) for i in x])
plt.plot(y)
