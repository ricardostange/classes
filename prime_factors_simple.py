# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:11:59 2017

@author: Ricardo
"""

# Return factorization of natural number


def factors_sub(n,a):
    if(a == n):
        return [a]
    if (n % a) == 0:
        return [a] + factors_sub(int(n/a),a)
    return factors_sub(n,a+1)
    

def factors(n):
    assert (type(n) is int) and n > 0
    if(n == 1):
        return []
    return factors_sub(n,2)
    
print(factors(30))
print(factors(7))
print(factors(42))
print(factors(1))
print(factors(16))
print(factors(1337))