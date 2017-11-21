# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:15:08 2017

@author: Ricardo
"""
import random

I = 3 #number of input nodes
M = 10 #number of middle nodes
O = 3 #number of output nodes

brain = [False for i in range(I+M+O)]

def random_dna(I, M, O):
    dna = []
    for i in range(M+O):
        dna.append((random.choice(range(I+i)), random.choice(range(I+i))))
    return dna
    
def nand(t, brain):
    return not(brain[t[0]] and brain[t[1]])
    
def run(dna, brain, I, M, O):
    for i in range(len(dna)):
        brain[i+I] = nand(dna[i], brain)
    return brain
        
def fitness_rps(dna, brain, I, M, O): #RPS answers with RPS (rock, papers, scissors)
    fit = 0
    brain[:3] = [True, False, False]
    if((brain[0+I+M] is False) and (brain[1+I+M] is True) and (brain[2+I+M] is False)):
        fit += 1
    brain[:3] = [False, True, False]
    run(dna, brain, I, M, O)
    if((brain[1+I+M] is False) and (brain[2+I+M] is True) and (brain[1+I+M] is False)):
        fit += 1
    brain[:3] = [False, False, True]
    run(dna, brain, I, M, O)
    if((brain[1+I+M] is False) and (brain[0+I+M] is True) and (brain[2+I+M] is False)):
        fit += 1
    return fit




dna = random_dna(I, M, O)
run(dna, brain, I, M, O)
print(fitness_rps(dna, brain, I, M, O))
    