#Luis Gonzalez and Joey Klaips
#Prof Kim
#10/23/2019
#HW.4

import math
#need to import math library for computation 
#----------------------------------------- definitions---------------------------------------------------------
###############################################################################################################
def getArrays (X, Y): # there are two arrays needed to be stored
# this def will ask and store the coordinates in two seperate arrarys
    print("--------------------------------------------------")
    for i in range (number_of_coordinates):
        print("--------------------------------------------------")
    
        mylist_X[i] = int(input("Enter x coordinates: " ))
        mylist_Y[i] = int(input("Enter y coordinates: " ))
        
        print("--------------------------------------------------")
        
    print("--------------------------------------------------")
    print("your Coordinates are: ")    
    for i in range(number_of_coordinates):
        print("(", mylist_X[i], ",", mylist_Y[i],")")
    print("--------------------------------------------------")
    #prints arrays in a neat way to view

###############################################################################################################
def sortParallelLists (Sorted_lenghts, mylist_X, mylist_Y ):
# this def will sort an array based on the origins of the two coordinates
    for i in range (number_of_coordinates):
    
        Sorted_lenghts[i] =  math.sqrt((mylist_X[i] * mylist_X[i]) + (mylist_Y[i] + mylist_Y[i]))
     # a new array is created to store the lenghts of the coordinates 
    
    print("The Lenghts are: ", Sorted_lenghts)

    
    for i in range(number_of_coordinates):
        for j in range(len(Sorted_lenghts)-1):
            if (Sorted_lenghts[j] > Sorted_lenghts[j + 1]):
                temp = Sorted_lenghts[j]
                Sorted_lenghts[j] = Sorted_lenghts[j + 1]
                Sorted_lenghts[j + 1] = temp
                
                
                
  #sortedCoordinateList(Sorted_lenghts[i][j])
                
            
            
    print("The sorted lenghts: ", Sorted_lenghts)
   
    
    return Sorted_lenghts 

#----------------------------------------- definitions---------------------------------------------------------
###############################################################################################################
###############################################################################################################
#----------------------------------------- Main program---------------------------------------------------------


print("--------------------------------------------------")
number_of_coordinates = int(input("Enter the amount of coordinated you would like to compute: "))
mylist_X = [None] * number_of_coordinates
mylist_Y = [None] * number_of_coordinates
lenghts = [None] * number_of_coordinates
# These are the Golbal arrays needed to be intaited from the start


getArrays(mylist_X, mylist_Y)
#calls the function with the two arrays as the parameters
Global_Lenghts = sortParallelLists(lenghts, mylist_X, mylist_Y)
#the lenghts are stored in a new array that is now in a global scope


print(sortParallelLists)
            

for i in range(number_of_coordinates):
    for j in range((number_of_coordinates)-1):
        if (Global_Lenghts[i] ==  math.sqrt((mylist_X[j] * mylist_X[j]) + (mylist_Y[j] + mylist_Y[j]))):
            Temp_X =  mylist_X[j] 
            Temp_Y =  mylist_Y[j]
            
            mylist_X[j] =  mylist_X[j + 1]
            mylist_Y[j] =  mylist_Y[j + 1]
                
            mylist_X[j + 1] = Temp_X
            mylist_Y[j + 1] = Temp_Y

#sorts the coordinates based on if they match the sorted list of lenghts from prior calculations

print("--------------------------------------------------")
print("your new Coordinates from accending order are: ")
for i in range(number_of_coordinates):
    print("(", mylist_X[i], ",", mylist_Y[i],")")
print("--------------------------------------------------")

#prints out nicely the new sorted arrays from the X and Y coordinates
