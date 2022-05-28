#Luis Gonzalez
#Prof. Kim
#cse 160
#8/31/2019

while (True): # start of infinite loop
    #print the menu
    print("I'll guess the triangle")
    print("Program Mode")
    print("(1) Side Lenghts")
    print("(2) Angles")
    print("(3) Quit")
    #get user input
    option=input("Enter option: ")
    option=float(option)
    optin=int(option)
    #these are the strings that are converted to integers
    if (option == 1):
        print("You decided to work with lenght sizes")
        while (True):
            a = input("Enter First lenght size: ")
            a = float(a)
            a = int(a)
            if (a <= 0):
                print("Your first lenght is invalid")
            else:
                break
   ## this ends the loop for the first condition for a valid variable thats greater than 0
        while (True):
            b = input("Enter second lenght size: ")
            b = float(b)
            b = int(b)
            if (b <= 0):
                print("Your lenght is invalid")
            else:
                break
    ## this ends the loop for the second condition for a valid variable thats greater than 0
        
        while (True):
            c = input("Enter third lenght size: ")
            c = float(c)
            c = int(c)
            if(c <= 0):
                print("Your lenght is invalid")
            else:
                break
    ## this ends the loop for the third condition for a valid variable thats greater than 0

        if ((a+b <= c) or
            (a+c <= b) or
            (b+c <= a)):
            print("Your lenght are not invalid")
    ## The conditions of a triangle that would make it invaild
     
        elif(a==b and  b==c):
            print(" Your triangle is an Equilateral!!")
        elif(a==b or a==c or b==c ):
            print("Your triangle is an Isosceles!!")
        else:
            print("Its a Scalene Triangle!!!")
    ## set of conditions that will help the computer decide what type of triangle it is
            
    elif(option == 2):
        #this is the option to work witb the angles mode
        print("You decided to work with Angles(:")
        while (True):
            a = input("Enter First angle:  ")
            a = float(a)
            a = int(a)
            if (a <= 0 or a > 180):
                print("Your first angle invalid")
            else:
                break
     ## this ends the loop for the first condition for a valid variable thats greater than 0
  
        while (True):
            b = input("Enter Second Angle:  ")
            b = float(b)
            b = int(b)
            if (b <= 0 or b > 180):
                print("Your second angle is invalid")
            else:
                break
     ## this ends the loop for the second condition for a valid variable thats greater than 0
     
        while (True):
            c = input("Enter third angle:  ")
            c = float(c)
            c = int(c)
            if(c <= 0 or c > 180):
                print("Your third angle is invalid")
            else:
                break
     ## this ends the loop for the third condition for a valid variable thats greater than 0

        if (a+b+c < 180 or a+b+c >180):
            print("The Sum of the angles do not eqaul to 180")
     ## The only two conditions that need to be true to be a triangle  
        elif (a==90 or b==90 or c==90):
            print("You have a right triangle")
            
        elif (a>90 or b>90 or c>90):
            print("You have an Obtuse angle")
        
        elif (a<90 or b<90 or c<90):
            print("You have an acute angel")
    ## set of conditions that will help the computer decide what type of triangle it is
    
    elif(option == 3):
        #the last mode which exits the loop
        print("Goodbye")
        break
    else:
        # If user does not choose the right mode, it will ask again
        print("Enter another option")
            
        