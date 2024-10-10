# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:48:29 2024

@author: PC
"""

def ktra_gtri():
    n = input("nhập n:")
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
    if -89<=n<=90:
        return n
    print("ko hợp lệ. nhập lại")
    return ktra_gtri()
print(ktra_gtri())