# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:44:25 2024

@author: PC
"""

def ktra_so(n):
    if n<0 and n%2!=0:
        return -1
    elif n>0 and n%2==0:
        return 1
    return 0
print(ktra_so(6))