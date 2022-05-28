base=input("enter a base: ")
base=float(base)
base=int(base)
    
exp=input("enter an Exponent:  ")
exp=float(exp)
exp=int(exp)

answer = 1



while(True):
    if(base== 0 and exp==0):
        answer="unkown"
        print("can not have a base and exponent both be 0")
    if(exp<0):
        answer=answer/base
        exp = exp + 1
    if(exp>0):
        answer=answer*base
        exp = exp -1  
    if(exp==0):
        break
print("answer:  ", answer)
