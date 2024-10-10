# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:45:39 2024

@author: PC
"""

import math
def chuvi_dt(hinh,pheptinh, *args, **kwargs):
    if hinh == "vuong":
        canh = args[0]
        return 4*canh if pheptinh == "chuvi" else canh**2
    #if pheptinh == "chuvi:"
    #   return 4*canh
    #else:
    #   return canh**2
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) if pheptinh == "chuvi" else dai*rong
    elif hinh == "tron":
        bk = args [0]
        return 2*math.pi*bk if pheptinh == "chuvi" else math.pi*bk
    else:
        return "hinh khong hop le"
    
if __name__=="__main__":
    print("chu vi hinh vuong:", chuvi_dt('vuong','chuvi',3))
    print("dien tich hinh vuong:", chuvi_dt('vuong','dientich',3))
    print("chu vi hinh chu nhat:", chuvi_dt('chunhat','chuvi',3,4))
    print("dien tich hinh chu nhat:", chuvi_dt('chunhat','dientich',3,4))
    print("chu vi hinh tron:", chuvi_dt('tron','chuvi',3))
    print("dien tich hinh tron:", chuvi_dt('tron','dientich',3))