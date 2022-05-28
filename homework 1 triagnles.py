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
            b = input("Enter second lenght size: ")
            b = float(b)
            b = int(b)
            c = input("Enter third lenght size: ")
            c = float(c)
            c = int(c)
            #all the vaiables are listed and converted into useable integers
            if (a+b <= c or c <= 0):
                print("Your lentghts are not invalid")
                break
            elif (a+c <= b or b <= 0):
                print("Your lentghts are not invalid")
                break
            elif(b+c <= a or a <= 0):
                print("Your lentghts are not invalid")
                break
            elif(a==b and a==c and b==c and b==a and a==c and c==b):
                print (" Your triangle is an Equilateral!!")
                break
            elif(a==b or a==c or b==c ):
                print("Your triangle is an Isosceles!!")
                break
            else:
                print("Its a Scalene Triangle!!!")
                break
    elif(option == 2):
        #this is the option to work witb the angles mode
        print("You decided to work with Angles(:")
        while(True):
            a=input("Enter the first angle: ")
            a=float(a)
            a=int(a)
            b=input("Enter the second angle: ")
            b=float(b)
            b=int(b)
            c=input("Enter the Third angle: ")
            c=float(c)
            c=int(c)
            if (a <= 0):
                print("Enter angles greater than 0")
                break
            elif (b <=0 ):
                print("Enter angles greater than 0")
                break
            elif (c <= 0):
                print("Enter angles greater than 0")
                break
            elif (a+b+c < 180 or a+b+c >180):
                print("The Sum of the angles do not eqaul to 180")
                break
            elif (a==90 or b==90 or c==90):
                print("You have a right triangle")
                break
            elif (a>90 or b>90 or c>90):
                print("You have an Obtuse angle")
                break
            elif (a<90 or b<90 or c<90):
                print("You have an acute angel")
                break
    elif(option == 3):
        #the last mode which exits the loop
        print("Goodbye")
        break
    else:
        # If user does not choose the right mode, it will ask again
        print("Enter another option")
            
            
        
            
        
                
        
            
       
            
            
            
    