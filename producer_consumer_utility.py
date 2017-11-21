# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:53:13 2017

@author: Ricardo
"""

def inv_demand(y):
    return 400-2*y
    
def total_cost(y):
    return 40*y

def consumer_surplus(inv_demand, y):
    util = 0
    p = inv_demand(y)
    for i in range(1,y+1):
        util += inv_demand(i) - p
    return util

def producer_surplus(inv_demand, y, total_cost):
    p = inv_demand(y)
    util = p*y - total_cost(y)
    return util
    

y = 90
print("y = 90")
print("Consumer Surplus: " + str(consumer_surplus(inv_demand, y)))
print("Producer Surplus: " + str(producer_surplus(inv_demand, y, total_cost)))
y = 176
print("y = 176")
print("Consumer Surplus: " + str(consumer_surplus(inv_demand, y)))
print("Producer Surplus: " + str(producer_surplus(inv_demand, y, total_cost)))