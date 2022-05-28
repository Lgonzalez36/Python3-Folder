#Prof. Kim
#10/7/2019
#ex. from 10/4


#---------- function definitions -----------------------

def findMin(someTable):
    # return the min value in a 2D array called someTable
    
    min = someTable[0][0]
    
    for i in range(0,len(someTable), 1): #walk rows
        for j in range(0,len(someTable[i]),1): #walk cols
            if (someTable[i][j] < min):
                min = someTable[i][j]
    
    return min    


def getAvg(someTable):
    sum = 0
    for i in range(0,len(someTable), 1): #walk rows
        for j in range(0,len(someTable[i]),1): #walk cols
            sum = sum + someTable[i][j]
    
    avg = sum / ( len(someTable) * len(someTable[0]) )
    return avg


def searchTable(someTable, item):
    #return True if item is found in someTable (2D list)
    #return False otherwise
    found = False
    
    for i in range(0,len(someTable), 1): #walk rows
        for j in range(0,len(someTable[i]),1): #walk cols
            if (item == someTable[i][j]):
                found = True
                break
        if (found == True):
            break
                
    return found
    
    
    
#---------- main program --------------------------------

myMat = [[100,200,300,400], 
         [5,6,7,8], 
         [9,10,11,12]]
print (myMat)
result = findMin(myMat)
print ("min=",result,sep='')

result = getAvg(myMat)
print ("avg=",result,sep='')

if (searchTable(myMat, 9)):
    print ("Found9!")
else:
    print ("Not Found!")



