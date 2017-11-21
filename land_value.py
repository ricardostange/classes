# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:13:54 2017

@author: Ricardo
"""
# Returns the value of the land, given rent and the probability of losing
# the asset in a unit of time. It assumes that the value of money remains constant
def land_value(rent, prob_n_loss):
    return rent*(1/(1-prob_n_loss))
    
def prob_n_loss(land_value, rent):
    return (land_value-rent)/land_value
    
    
rent = 100
pnLoss = .99
print("Rent: 100, prob not losing: .99")
print("Land Value: " + str(land_value(rent, pnLoss)))

rent = 1000
value = 400*10**3
print("Rent: 1000, Land Value: 400000")
print("Prob Not Losing: " + str(prob_n_loss(value, rent)))