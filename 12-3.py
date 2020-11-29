# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:00:45 2020

@author: Admin
"""

import random
import string
list1=[]
n=random.randrange(50,101)
print('n= ' ,n)
for i in range(n):
    dic=dict()
    tup=[dic]
    m = random.randint(0, 6)
    a = random.choice(string.ascii_uppercase)
    for j in range(m):
        a = a + random.choice(string.ascii_lowercase)
    dic['name'] = a
    c = random.randrange(1, 140)
    dic['age'] = c
    print(i+1,' = ',tup)
    list1 += tup
print('list= ',list1)
