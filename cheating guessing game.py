#prof. Kim
#9/11/2019
# guessing game

import random

#wallet = 100
values = [None] * 10



while (True):
    answer = random.randint(1,10)
    
    for i in range(0,10,1):
        answer[i] = random.randint(1,10)
    print("------------------------------")    
    #print("You have:$", wallet)
    #bet = float( input("Place a bet:"))
    
    #while (bet > wallet or bet <= 0):  # invalid wager
        #print("Invalid bet amount.")
        #bet = float( input("Place a bet:"))
        
    print(answer)
       
    guess = int( input("Guess between 1 and 10:") )
    
    
    if (guess == answer):
        print ("correct")
        #wallet = wallet + bet
    else:
        print ("wrong, the aswer was", answer)
        #wallet = wallet - bet
        #if (wallet == 0):
           # print ("You are out of money")
            #break

print ("Thanks for playing, and thanks for your money")
        