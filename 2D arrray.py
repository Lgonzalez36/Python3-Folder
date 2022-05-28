#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:52:08 2019

@author: lagonzalez
"""

#........................definiations........................

def findMin (someTable):
#searches someTable for the min value
#returns the min value
   
    min = someTable[0][0]
    
    
    for i in range(len(someTable)):
        for j in range(len(someTable[i])):
            if ( min > someTable[i][j]):
                min = someTable[i][j]
        
    return min


def getAvg (someTable):
#reaturn avg of all numbers in someTable

  sum = 0
  for i in range(len(someTable)):
      for j in range(len(someTable[i])):
          sum = sum + someTable[i][j]
          
          avg = sum / (len(someTable[0]) + len(someTable[1]))
  return avg


def searchList (someTable, someItem):
    
    for i in range(len(someTable)):
        for j in range(len(someTable[i])):
            if (someTable[i][j] == someItem):
                return True
            
    return False
    
    
#return True: if someItem is found in someTable
#return False: if someItem is not found in someTable


#.............................Main Program.........................
    
Table = [[200, 4, 6, 8], 
         [10, 20, 2, 40]
]  


average = getAvg(Table)
x = findMin(Table)



print("Min =", x)
print("average =", average)


print (searchList(Table, 11))
print ( searchList(Table, 2))



#average = getAvg(x)
#print("average", average)

