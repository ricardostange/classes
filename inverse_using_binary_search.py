# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 00:01:25 2017

@author: Ricardo
"""
# Given a continuous monotonic function tries to find its inverse on the point

def inverse(func, y, inf_limit=-10**100, sup_limit=10**100, error=10**(-10)):
    inf = func(inf_limit)
    sup = func(sup_limit)
    mid_point = (sup_limit+inf_limit)/2
    mid = func(mid_point)
    if(abs(mid-y) <= error):
        return mid_point
    assert (inf <= mid <= sup) or (inf >= mid >= sup)
    if((inf <= y <= mid) or (inf >= y >= mid)):
        return inverse(func, y, inf_limit, mid_point, error)
    else:
        return inverse(func, y, mid_point, sup_limit, error)
    
# Test 1
def squared(x):
    return x**2
x = 2
print(inverse(squared, x, inf_limit=0)) #limit has to be zero for monotonicity

# Test 2
def cubed(x):
    return x**3
x = 8
print(inverse(cubed, x))

# Test 3
import math
def exp(x):
    return math.e**x
x = 5
print(inverse(exp, x, sup_limit=200)) #limit prevents overflow
