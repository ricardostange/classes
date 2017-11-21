# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:57:14 2017

@author: Ricardo
"""


def new_base(number, base):
    nNumber = []    #number will be represented as a list of numbers
    assert ((number > 1) and (number%1) == 0)
    while number > 0:
        c = number % base
        number -= c
        number /= base
        nNumber.insert(0,int(c))
    return nNumber



number = 42
base = 5
print(new_base(number, base))

number = 23
base = 7
print(new_base(number, base))
