# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 00:13:24 2017

@author: Ricardo
"""
import random

def price(city, demand, supply):
    assert supply[city] < demand[city][0] # makes sure price is positive
    return (demand[city][0]-supply[city])/demand[city][1]
    
def step(demand, supply):
    for city in supply.keys():
        s = supply[city]
        if(demand[city][0]-(s+1) < 0):
            supply[city] -= 1
        elif(s-1 < 0):
            supply[city] += 1
        else:
            supply[city] += random.choice([-1,1])
    return supply



class Merchant():
    def __init__(self):
        self.money = 100
        self.goods = 0
        self.city = 'A'
        self.demand = {"A":(100, 1), "B":(100,1), "C":(100,1)}
        self.supply = {"A": 50, "B": 50, "C": 50}
        self.distances = {'A':{'B':3, 'C':4},'B':{'A':3, 'C':5},'C':{'A':4, 'B':5}}
        self.walked = 0
        
    def where_am_i(self):
        return self.city
        
    def move(self, destination):
        assert destination in self.demand.keys()
        if(destination == self.city):
            return False
        for i in range(self.distances[self.city][destination]):
            self.supply = step(self.demand, self.supply)
            self.walked += 1
            self.city = destination
            
    def summary(self):
        print("Cidade: " + self.city + " Dinheiro: " + str(self.money) + " Prices: " + str(price(self.city, self.demand, self.supply)) + " Goods: " + str(self.goods))
    def buy(self, q):
        p = price(self.city, self.demand, self.supply)
        if(q*p > self.money):
            return False
        self.money -= p*q
        self.goods += q
        return True
        
    def sell(self, q):
        p = price(self.city, self.demand, self.supply)
        if(q > self.goods):
            return False
        self.goods -= q
        self.money += p*q
        return True








#print(price('A', demand, supply))
#print(price('A', demand, supply))
#step(supply)
#supply