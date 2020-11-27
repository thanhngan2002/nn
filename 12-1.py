# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:33:06 2020

@author: Admin
"""

import random
n=random.randrange(50,1000)
print(n)
print('ket thuc bai 1')

list1=list()
for i in range(n):
    list1.append(random.randrange(-1000,1000))
print(list1)
print('ket thuc bai 2')
list2=list()
for i in range(n):
    list2.append(random.triangular(-1000.0,1000.0))
print(list2)
print('ket thuc bai 3')



