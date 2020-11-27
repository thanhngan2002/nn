# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:33:06 2020

@author: Admin
"""

import random
n=random.randrange(50,1000)
print(n)
print('ket thuc bai 1')

apple1=list()
for i in range(n):
    apple1.append(random.randrange(-1000,1000))
print(apple1)
print('ket thuc bai 2')
apple2=list()
for i in range(n):
    apple2.append(random.triangular(-1000.0,1000.0))
print(apple2)
print('ket thuc bai 3')



