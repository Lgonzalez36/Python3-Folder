#Prof. Kim
#Practice exam

def countOdds(list):
    cnt = 0
    for i in range(len(list)):
        if (list[i] % 2 == 1):
            cnt += 1
    
    return cnt

def squareEvens (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] % 2 == 0):
                matrix[i][j] = matrix[i][j] * matrix[i][j]


def secondMax (mat):
    #1st find THE MAX
    max = mat[0][0]
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (mat[i][j] > max):
                max = mat[i][j]
    
    found = False
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (mat[i][j] != max):  ############
                max2 = mat[i][j]
                found = True
                break
        if (found==True):
            break

    if (found == False):
        return max
    else:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (mat[i][j] > max2 and mat[i][j] < max):
                    max2 = mat[i][j]
        
        return max2
    
    
    
    
    

x = [3,4,4,5,6,766,54,4,43]

count = countOdds(x)
print(count)

y = [[1,3,5,2], [6,6,8,7], [9,6,4,9]]
squareEvens(y)
print(y)

z = [[5,5,5,5],[5,5,5,5]]
result = secondMax(z)
print(result)


def removeMatches (myData, prefix):
    stringPrefix = str(prefix)
    
    #copy myData
    copy = [None] * len(myData)
    for i in range(len(myData)):              
        copy[i] = myData[i]
   
    for i in range(len(copy)):              
        if (copy[i].startswith( stringPrefix )):            
            myData.remove(copy[i])
        



dat=["11130900", "11120809", "11148878", "11120911"]
p = 1112


removeMatches(dat, p)
print(dat)










