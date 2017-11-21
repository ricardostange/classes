# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:41:19 2017

@author: Ricardo
"""
import math


def best_play(game):
    best = ("", False)
    for play in game[1].keys():
        if best[1] is False:
            best = (play, game[1][play])
            continue
        if(game[1][play][game[0]] > best[1][game[0]]):
            best = (play, game[1][play])
    return best

game1 = (1,{"a":(3,2),"b":(5,5)})
print(best_play(game1))
game2 = (1,{"a":(0,0),"b":(7,4)})
print(best_play(game2))
game3 = (0,{"A":(5,5),"B":(7,4)})
print(best_play(game3))
