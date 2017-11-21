# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:34:04 2017

@author: Ricardo
"""
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED

X =  [(2,3), (3,5), (4,6.5)]

x = [[2],[3],[4]]
y = [[3],[5],[6.5]]

def product(list1, list2):
    assert len(list1) == len(list2)
    return sum([a*b for (a,b) in zip(list1, list2)])

def gradient(x,y,w):
    grad = [0 for i in range(len(w))]
    for l in x:
        for k in range(len(l)):
            for r in range(len(w)):
                grad[k] += 2*w[r]*l[r]l[k]
            grad[k] -= 2*y[]

def linear_fit(x,y):
    assert len(x) == len(y)
    x = [[1] + line for line in x]  # insert column of 1's for independent coeficient
    w = [[0], [0]]
    gradient(x, y, w)
    

### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED
### THIS IS NOT FINISHED