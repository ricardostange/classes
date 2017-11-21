# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:55:03 2017

@author: Ricardo
"""

import hashlib
import time

def hash_str(s):
    assert type(s) == str
    h = hashlib.sha256(s.encode('ascii'))
    return h.hexdigest()
    
def find_8_numerals_pass(passHash):
    for i in range(10**9):
        p = format(i, '08d')
        if(hash_str(p) == passHash):
            return p
            
A = '7f4517e023a3fb705c4c2e7ab2994bf4d2f3e3bfa5dbdbed1f22b71c0100a1b7'
t0 = time.clock()
print("pass A:" + find_8_numerals_pass(A) + " time: " + str(time.clock()-t0))

B = '975445a166a4c3b4844de4d36919ed8ba2988bfdfe9d644fe72a029d71801b49'
t0 = time.clock()
print("pass B:" + find_8_numerals_pass(B) + " time: " + str(time.clock()-t0))

C = '3f08d8fadb4b67fb056623565edbbc2c788091d78fd24cbc473fce3043ce3473'
t0 = time.clock()  # This will take a while
print("pass C:" + find_8_numerals_pass(C) + " time: " + str(time.clock()-t0))
        