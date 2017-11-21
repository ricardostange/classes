# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:51:45 2017

@author: Ricardo
"""

# Given a directed graph of transfers, return the net flow


def net_flow(g):
    for k in g.keys():
        for pair in g[k]:
            assert pair[0] in g.keys()
    net_amount = dict()
    for k in g.keys():
        net_amount[k] = 0
    for k in g.keys():
        for pair in g[k]:
            net_amount[pair[0]] += pair[1]
            net_amount[k] -= pair[1]
    net_total = 0
    for k in net_amount.keys():
        if net_amount[k] > 0:
            net_total += net_amount[k]
    return net_total
    
g = {"A":[("B",500)],
     "B": [("C", 300)],
     "C": [("A",200)]}
print(net_flow(g))

g = {"A":[("A",300)],
     "B": [("B", 300)],
     "C": [("C",300)]}
print(net_flow(g))

g = {"A":[("A",300),("B",300),("C",300)],
     "B": [("A",200),("B",200),("C",200)],
     "C": [("A",100),("B",100),("C",100)]}
print(net_flow(g))