# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:59:54 2017

@author: Ricardo
"""

# Returns the module of the sum of all elements in a vector

def vec_mod(v, n):
    assert (type(n) == int)
    s = 0
    for i in v:
        s = (s + i)%n
    return s


test1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(vec_mod(test1, 10))

test2 = [1 for i in range(10)]
print(vec_mod(test2, 10))
