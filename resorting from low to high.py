# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:58:49 2019

@author: luisg
"""




Array_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


    
    
    
for i in range(10):
    for j in range(len(Array_2)-1):
        if (Array_2[j] > Array_2[j + 1]):
            temp = Array_2[j]
            Array_2[j] = Array_2[j + 1]
            Array_2[j + 1] = temp
            
            
print(Array_2)
            
