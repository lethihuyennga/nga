# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:28:36 2024

@author: PC
"""

import random
def tao_day_ngau_nhien(N):
  seqA = []
  for i in range(N):
    kieu_du_lieu = random.choice(['int', 'float'])          
    if kieu_du_lieu == 'int':   
      so = random.randint(-79, 39)
    else:
      so = round(random.uniform(-79, 39), 2)
      seqA.append(so)
      return seqA
N = random.randint(30, 80)
seqA = tao_day_ngau_nhien(N)
print("Danh sách ngẫu nhiên:", seqA)        

def kiem_tra_kieu_du_lieu(danh_sach):
  for i, phan_tu in enumerate(danh_sach):
    print(f"Phần tử thứ {i+1}: {phan_tu}, Kiểu dữ liệu: {type(phan_tu)}")
    
def thong_ke_so_luong(danh_sach):
      return len(danh_sach) 
  
def sap_xep_tang_dan(danh_sach):
      danh_sach_sap_xep = sorted(danh_sach)
      return danh_sach_sap_xep
  
def tinh_trung_binh(danh_sach):
  if len(danh_sach) == 0:
    return None  
  else:
    tong = sum(danh_sach)
    trung_binh = tong / len(danh_sach)
    return trung_binh