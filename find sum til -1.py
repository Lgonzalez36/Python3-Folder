while(True):
    sum=0
    x=0
    Avg=0
    
    while(True):
        x=input("Enter a number:  ")
        x=int(float(x))
        
        
        sum = sum + x
        Avg= Avg + 1
        
        print(sum)
        
        if(x==-1):
            x= x*(-1)
            x= x + 1
            Avg= Avg + 1
            
            print("Average = ", sum/Avg, "total =  ", sum)
            break