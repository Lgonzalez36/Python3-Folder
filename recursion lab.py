def sigma (x):
    if (x == 1):
        return 1
    
    reslut = x * sigma(x - 1)
    return reslut





Nfactor = int(input("Enter a number you want be factorial: "))
sum = sigma (Nfactor)

print(sum)
    
