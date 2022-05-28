
countYes = 0
    
for x in range(1,11,1):
    
    found = False
    
    for i in range(0,10,1):    
        if (guesses[i] == x):
            found = True
            break
    
    if (found == False): #means: user missed a number
        print("You lose, the answer is", x)
        break
    else:
        countYes = countYes + 1

# did the user win?
if (countYes == 10):
    print ("You win!")
else:
    print ("You lose...")