# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:36:55 2017

@author: Ricardo
"""

def function(x):
    return x**3
    
def derivative(function,delta,x):
    return (function(x+delta)-function(x-delta))/(2*delta)
    

delta = 0.001
x = 0
print("x = 0, derivative: " + str(derivative(function, delta, x)))
x = 2
print("x = 2, derivative: " + str(derivative(function, delta, x)))
x = 5
print("x = 5, derivative: " + str(derivative(function, delta, x)))
x = 4
print("x = 4, derivative: " + str(derivative(function, delta, x)))