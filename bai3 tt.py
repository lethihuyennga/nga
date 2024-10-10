# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:30:04 2024

@author: PC
"""

def tinh_gia_tri_giua(seqB):
  N = len(seqB)
  if N % 2 == 0:
    mid1 = N // 2 - 1
    mid2 = mid1 + 1
    return (seqB[mid1] + seqB[mid2]) / 2
  else:     
    mid = N // 2
    return seqB[mid]

def tinh_khoang_cach_max_min(danh_sach):
  if len(danh_sach) == 0:
    return None  
  else:
    gia_tri_max = max(danh_sach)
    gia_tri_min = min(danh_sach)    
    khoang_cach = gia_tri_max - gia_tri_min
    return khoang_cach
   
def so_sanh_khoang_cach(seqA, seqB):
  def tinh_khoang_cach(danh_sach):
    return max(danh_sach) - min(danh_sach)

  khoang_cach_A = tinh_khoang_cach(seqA)
  khoang_cach_B = tinh_khoang_cach(seqB)
  nguong_so_sanh = 0.1  
  return abs(khoang_cach_A - khoang_cach_B) / max(khoang_cach_A, khoang_cach_B) < nguong_so_sanh