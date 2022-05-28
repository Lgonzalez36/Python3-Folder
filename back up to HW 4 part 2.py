# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:28:52 2019

@author: luisg
"""

import math

#need to import math library for computation 
###############################################################################################################
#----------------------------------------- definitions---------------------------------------------------------
###############################################################################################################
class Get_array:
    """this is supposed to make a difference"""
    def __init__(self, xVal, yVal):
        """Initailize a point obj's coordinate"""
        self.x = [None] * numberOfCoordinates
        self.y = [None] * numberOfCoordinates
        self.dist = [None] * numberOfCoordinates
        self.sorted = [None] * numberOfCoordinates
        
        
        for v in range (numberOfCoordinates):
            self.x[v] = xVal[v]
            self.y[v] = yVal[v]
            self.dist[v] = math.sqrt(xVal[v]**2 + yVal[v]**2) 
          
        
        for q in range (numberOfCoordinates):
            self.sorted[q] = self.dist[q]
        
        
        for l in range (numberOfCoordinates):
            for p in range (len(self.sorted) - 1):
                if (self.sorted[p] > self.sorted[p + 1]):
                    temp = self.sorted[p]
                    self.sorted[p] = self.sorted[p + 1]
                    self.sorted[p + 1] = temp
                    
                    
        
                    
    def display(self):         
        print("your new Coordinates from accending order are: ")
        print("(",self.x,",",self.y,"):",self.dist,sep='')
        print("--------------------------------------------------")
            
            
        
###############################################################################################################            
#----------------------------------------- Main Program---------------------------------------------------------
###############################################################################################################
            
print("--------------------------------------------------")

numberOfCoordinates = int(input("Enter the amount of numbers you want to comnpute: "))
My_list_X = [None] * numberOfCoordinates
My_list_Y = [None] * numberOfCoordinates
lenghts = [None] * numberOfCoordinates


for i in range (numberOfCoordinates):
    My_list_X[i] = int(input("Enter the X coordinate: "))
    My_list_Y[i] = int(input("Enter the y coordinate: "))
    
lenghts = Get_array(My_list_X, My_list_Y)

print("--------------------------------------------------")
print(lenghts.x, lenghts.y)
print("--------------------------------------------------")


print("--------------------------------------------------")
print("Unsorted ", lenghts.dist)
print("Sorted ", lenghts.sorted)
print("--------------------------------------------------")



print("------------------")
for i in range(numberOfCoordinates):
    lenghts[i].display()



for j in range (numberOfCoordinates):
    for k in range ((numberOfCoordinates) - 1):
        if (lenghts.sorted[j] == math.sqrt(lenghts.x[k]**2 + lenghts.y[k]**2)):
            
            Temp_X =  lenghts.x[k] 
            Temp_Y =  lenghts.y[k] 
                    
            lenghts.x[k] =  lenghts.x[k + 1]
            lenghts.y[k] =  lenghts.y[k + 1]
            
            lenghts.x[k + 1] = Temp_X
            lenghts.y[k + 1] = Temp_Y

            
print("------------------")
for i in range(numberOfCoordinates):
    lenghts[i].display()
