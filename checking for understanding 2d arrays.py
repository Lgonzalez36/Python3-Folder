# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:39:47 2019

@author: luisg
"""

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)