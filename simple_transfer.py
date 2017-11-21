# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:53:26 2017

@author: Ricardo
"""

def transfer(data, owner, to, amount):
    assert data['A'] >= amount
    data[owner] -= amount
    data[to] += amount
    
data = dict()
data['A']=10
data['B']=0
transfer(data, 'A', 'B', 5)
print(data)

data['A']=15
data['B']=2
transfer(data, 'A', 'B', 5)
print(data)