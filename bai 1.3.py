# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:17:54 2024

@author: PC
"""

n=int(input("Nhập số = "))
def chanam(a):
    return a < 0 and a % 2 == 0
print(chanam(n))