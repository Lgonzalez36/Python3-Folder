
def power (b, e):
    
    total = 1 
    
    while





while(True):
    print("...................................")
    print("Modes")
    print("(1) Power")
    print("(2) Factorial")
    print("(3) Quit")
    
    option=int(input("Enter a Mode:  "))
        
    
    if (option == 1):
    
        
        base=input("enter a base: ")
        base=float(base)
        base=int(base)
            
        exp=input("enter an Exponent:  ")
        exp=float(exp)
        exp=int(exp)
        
        
        if(base== 0 and exp==0):
            answer="unkown"
            print("can not have a base and exponent both be 0")
        
        else:
            def power_functions_positve(base,exp):
                result = base ** exp
                return result
            
            
            answer= power_functions_positve(base,exp)
            print("answer:  ", answer)  
            
    elif (option == 2):
        
        Factorial=1
        N=int(input("Enter the number you'll like to do a factorial:  "))
            
        for i in range(N):
            Factorial = Factorial * (i+1)
            
        print("Factorial", N, "! = ", Factorial)  
        
        
        
    elif(option == 3):
        print("Goodbye")
        break
    
    else:
        print("select one of the three options")
        
        
    