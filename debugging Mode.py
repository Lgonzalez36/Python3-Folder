#Prof. Kim
#debugging exercises

import math
import random

def testFunc3():
    # here we have a more elusive logical problem that does NOT
    # result in a runtime error. Rather, the result is just wrong.


    a=float(input("Enter side length a:"))
    b=float(input("Enter side length b:"))
    c=float(input("Enter side length c:"))
    
    print (a, b, c)
    #get angles
    x = math.acos(((b*b)+(c*c)-(a*a))/(2*c*c))
    y = math.acos(((a*a)+(c*c)-(b*b))/(2*a*a))
    z = math.acos(((a*a)+(b*b)-(c*c))/(2*b*b))
    
    print(x, y, z)
    
    #get area
    area = a*b*math.sin(z)/2
    
    #convert radians to angles
    x = x*(180/math.pi)
    y = y*(180/math.pi)
    z = z*(180/math.pi)

    print("x (opposite side a):", x)
    print("y (opposite side b):", y)
    print("z (opposite side c):", z)
    print("Area", area)
    



def testFunc2():
    # here we introduce a few array out of bounds problem
    list = [None] * 10
    
    #fill array with random integers
    for i in range (1,11):
    	list[i] = i + 1 # numbers between 1 and 10			
    
    for i in range (1,11):
    	print("original:", list[i])
				
    #swap the items around 	
    for i in range (0,50):
        idx1 = random.randint(0,11) # random index up to 10
        idx2 = random.randint(0,11) # random index up to 10
        temp = list[idx1]
        list[idx1]=list[idx2]
        list[idx2]=temp

    for i in range (1,11):
        print("shuffled:", list[i])


def testFunc1():
    #here we introduce an infinite loop
    # so that you can practice variable value inspection
    # using the debugging tool
    
    	
    sum=0.0
    while (sum!=10.0):
        sum = sum + random.randint(0,3)
    
    print("I generated some random numbers and their sum is:", sum)
		
	
def main():
    a= 1
    testFunc2()
    print(a)

main()