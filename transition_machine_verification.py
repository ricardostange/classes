# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:29:44 2017

@author: Ricardo
"""

# Verifies if a transiction machine is valid or not

T = dict()
T[1] = [(2,.2), (3,.8)]
T[2] = [(3,.6), (4, .4)]
T[3] = [(2,.5), (4,.5)]
T[4] = [(1,1)]


def is_valid(T):
    for k in T.keys():
        p = 0
        for i in T[k]:
            if i[0] not in T.keys():
                return False
            p += i[1]
        if(p != 1):
            return False
    return True
    



print(is_valid(T))