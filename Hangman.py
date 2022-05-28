# Prof. Kim
# 9/30/2019
# hangman v.1

def displayDude (chances):
    if (chances==6):
        print("--------")
        print("|      |")
        print("|      ")
        print("|     ")
        print("|     ")
        print("|")    
        print("--------")
    elif (chances==5):
        print("--------")
        print("|      |")
        print("|      O")
        print("|    ")
        print("|    ")
        print("|")    
        print("--------")
    elif (chances==4):
        print("--------")
        print("|      |")
        print("|      O")
        print("|      |")
        print("|      ")
        print("|")    
        print("--------")
    elif (chances==3):
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|")
        print("|     " )
        print("|")    
        print("--------")
    elif (chances==2):
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     ")
        print("|")    
        print("--------")
    elif (chances==1):
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     /")
        print("|")    
        print("--------")
    elif (chances==0):
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     / \\")
        print("|")    
        print("--------")







temp = [5,4,34,23]
answer = "FAGGOT" 
visible = ['_'] * len(answer)

life = 6  #number of chances you get

count = -1

while (True):
    print("**************************")
    print("You have", life, "chances left")
    displayDude(life)
    print(visible)
    
    guess = input("Guess a letter:")
    
    #check to see if guess is found in answer
    found = False
    for i in range(len(answer)):
        if (guess == answer[i]):
            visible[i] = guess
            count = count + 1
            found = True
    
    #check to see if the letter the user gussed
    # was found within the answer array
    if (found == False):
        life = life - 1
        if (life == 0):
            print("You lose")
            displayDude(life)
            break
    else:
        if (count == len(answer)):
            print("You win!")
            break
        
    
 