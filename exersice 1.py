#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:52:53 2019

@author: lagonzalez
"""


def findMin (someList):
    
    
    min = someList[0]
    for i in range (0,10,1):
       if (someList[i] < min):
           min = someList[i]
    return min





    #searches somelist of the min value wasa 
    #returns the min value



def findMinLocation(someList):
    min = someList[0]
    loc = 0
    for i in range (0,10,1):
       if (someList[i] < min):
           min = someList[i]
           loc = i
    return loc

    
    #returns the INDEX of where the min calue was
    #found insaide somelist
def getAvg(someList):
    avg = 0
    sum = 0
    for i in range (len(someList)):
        sum = sum + someList[i]
        
    avg = sum / len(someList)
         
    return avg
    
    
    # return avg of all numbers in someList
def copyList(someList):
    copy_List = [None] * len(someList)
    for i in range (len(someList)):
        copy_List[i] = someList[i]

    
    return copy_List
    
    
    
    # return a SEPARATE COPY of someList
def searchList (someList, someItem):
    found = False
    
    for i in range(len(someList)):        
        if (someList[i] == someItem):
            found = True
            break
    
    return found
    
    

    # return True: if someItemis found insomeList
    # return False: if someItemis not found in someList
numbers = [55, 2, 1, 4, 5, 6, 7, 8, 9, 10]    
x = findMin(numbers)
location = findMinLocation(numbers)  
x = findMin(numbers) 
average = getAvg(numbers)
copy = copyList(numbers)
copy[1] = - 20

print ( searchList(x, 40) )
print ( searchList(x, 1) )

print("location", location)
print("min", x)
print("average", average)
print("copy List", copy)
print("original", numbers)