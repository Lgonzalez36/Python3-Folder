#Prof. Kim
#10/4/2019
#exercise from 10/2


#----------------- function definitions ------------------

def findMin (someList):
    # searches someListfor the min value
    # returns the min value
    
    min = someList[0]
    
    for k in range(0,len(someList),1):
        if (someList[k] < min):
            min = someList[k]
    
    return min


def findMinLocation (someList):
    # searches someListfor the min value
    # returns the INDEX location of where min is
    
    min = someList[0]
    loc = 0
    
    for k in range(0,len(someList),1):
        if (someList[k] < min):
            min = someList[k]
            loc = k
    
    return loc
    
def getAvg(someList):
    # returns the average of all values in someList
    sum = 0
    
    for i in range(0,len(someList),1):
        sum = sum + someList[i]
    
    avg = sum / len(someList)
    
    return avg



def searchList(someList, someItem):
    # return True: if someItemis found insomeList
    # return False: if someItemis not found in someList

    found = False
    
    
    for i in range(0,len(someList), 1):        
        if (someList[i] == someItem):
            found = True
            break
    
    return found
    
def copyList(someList):
    # return a SEPARATE COPY of someList
    foo = [None] * len(someList)
    
    for i in range(0,len(someList),1):
        foo[i] = someList[i]
    
    return foo
    
    


#----------------- main program ------------------
    
x = [10,20,30,40,51]

y = findMin(x)
idx = findMinLocation(x)

print(y, idx)

result = getAvg(x)

print(result)

print ( searchList(x, 40) )
print ( searchList(x, 1) )

replica = copyList(x)

replica[0] = -1

print("x", x)
print("rep", replica)
