#Luis gonzalez
#11/20/2019
# BlackJack game 

import random
################################################################################################
#--------------------------------------------Class Definition-------------------------------------------- 
################################################################################################
class Card:
    def __init__ (self, s, v):
        # s is the suit type:
        # "spades" "hearts" "diamonds" "clubs"
        # v is the number:
        #  2-10 J=10 Q=10 K=10 A=14
        #
        # self.value is the numerical value        
        # self.faceValue is what you see on the screen (A,J,Q,K)
        self.suit = s
        self.value = v
        if (v==14):
            self.faceValue = 'A'
            self.value = 11 # will turn the ace value of 14 to 11
        elif (v==11):
            self.faceValue = 'J'
            self.value = 10 # will turn the high cards to have a value of 10
        elif (v==12):
            self.faceValue = 'Q'
            self.value = 10 # will turn the high cards to have a value of 10
        elif (v==13):
            self.faceValue = 'K'
            self.value = 10 # will turn the high cards to have a value of 10
        else:
            self.faceValue = v # anyother value will be from 2-10     
    def display (self):
        if (self.suit == "spades"):
            print ("[\u2660",self.faceValue,"]",sep='',end='') #this makes the card into a spades
        elif (self.suit == "hearts"):
            print ("[\u2661",self.faceValue,"]",sep='',end='') #this makes the card into hearts
        elif (self.suit == "diamonds"):
            print ("[\u2662",self.faceValue,"]",sep='',end='') #this makes the card into diamonds
        elif (self.suit == "clubs"):
            print ("[\u2663",self.faceValue,"]",sep='',end='') #this makes the card into clubs
################################################################################################
################################################################################################
class Deck:
    def __init__ (self):
        #make a full deck of 104 cards
        self.cards = [None] * 104        
        for i in range(0,13):
            self.cards[i] = Card("spades", i+2)
        for i in range(0,13):
            self.cards[ i + 13  ] = Card("hearts", i+2)
        for i in range(0,13):
            self.cards[ i + 26 ] = Card("diamonds", i+2)
        for i in range(0,13):
            self.cards[ i + 39 ] = Card("clubs", i+2)
        for i in range(0,13):
            self.cards[ i + 52 ] = Card("spades", i+2)
        for i in range(0,13):
            self.cards[ i + 65  ] = Card("hearts", i+2)
        for i in range(0,13):
            self.cards[ i + 78 ] = Card("diamonds", i+2)
        for i in range(0,13):
            self.cards[ i + 91 ] = Card("clubs", i+2)
        self.topIdx = 0
    def shuffle(self):
        #shuffle 
        for i in range(600):
            idx1 = random.randint(0,103)
            idx2 = random.randint(0,103)
            temp = self.cards[idx1]
            self.cards[idx1] = self.cards[idx2]
            self.cards[idx2] = temp               
    def display(self):
        for i in range(len(self.cards)):
            self.cards[i].display()
        # display function per card in the hand
    def dealCard(self):
        index = self.topIdx
        self.topIdx = self.topIdx + 1
        return self.cards[ index ]
    # deals cards
################################################################################################        
################################################################################################
class Player:
    def __init__(self, n, m):
        # n = name of the player (string)
        # m = amount of  money the player starts with
        self.name = n
        self.wallet = m
        self.hand = [None] * 5
        self.handSize = 5  #max capacity of the hand
        self.nCards = 0    #nCards: how many cards do I actually have at the moment
        self.nCardsDealer = 0    #nCards: how many cards do I actually have at the moment
        
        
    def showPlayer(self,):
        print(self.name, " $", self.wallet,sep='')
        for i in range(self.nCards):
            self.hand[i].display()
        print("")
        # will print out the player's cards and wallet
    def showDealer(self,):
        print(self.name, " $", self.wallet,sep='')
        if (self.nCards == 2 ):        
            self.hand[0].display()
        else:
            for i in range(self.nCards):
                self.hand[i].display()
        print("")
        # will print out the computer's cards and wallet bc it was easier to display one with out the other
        
    def getCard(self, aCard):     
        self.hand[ self.nCards ] = aCard
        self.nCards = self.nCards + 1
        # keeps track of the hand and how many cards the player/computer has
    def getScore(self):
        total = 0        
        for i in range (self.nCards):
            total = total + self.hand[i].value
            # add the sum of the values of the cards of both players
        for i in range (self.nCards):
            if (self.hand[i].value == 11 and total > 21):
                total = total - 10
            # if the sum is > 21 and an ace is found, it will turn it back to a value of 1        
        return total 
        #returns the total of the players/Dealer's hand
################################################################################################
#-----------------------------------------------Main--------------------------------------------
################################################################################################
d = Deck() # makes a deck of cards
d.shuffle() # shuffles the deck of cards
newCard = True # is a way to exit the last while loop
print("---------------------------------------------------------")
player1Name = str(input("Enter your name: ")) 
player1wallet = int(input("Enter the amount of money you want to play with: "))
DealerWallet = player1wallet * 2 # The dealer will have double the amount of the Player
# The player enter information about their name and how much they have to spend
p1 = Player(player1Name, player1wallet)
p2 = Player("Dealer", DealerWallet)
while(True):
    d.shuffle()
    # after each new game (not Round) the game will have a new shuffled deck
    while(True): # the first loop which will be for each round if the player wants to continue
        print("Players wallet", "$", p1.wallet)
        player1Bet = int(input("Place your bet: "))
        if(player1Bet <= 0):
            print("Invalid Bet")  
            break
        elif (player1Bet > player1wallet):
            print("You can't bet more than what you have in your wallet")
            print(p1.wallet, "Players wallet")
            break
        else:
            player1wallet = player1wallet - player1Bet
            p1 = Player(player1Name, player1wallet)
            p2 = Player("Dealer", DealerWallet)
        # The second inner while loop is to make sure the bet amount is > 0 and < wallet amount
        # The bet will be taken away from the wallet as if they put the bet money on the "Table"
        # The player and the computer will now have assigned their name and wallet per round
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        # An aesthetic break 
        p2.getCard ( d.dealCard() ) # The dealer will first have delt omw card to itself
        p2.showDealer() # will display one card 
        p2.getCard ( d.dealCard() ) #the hidden card from the player's view
        for i in range(2):
            p1.getCard ( d.dealCard() ) # the for loop will deal two cards to the player
        p1.getScore() # will call score function to compute the total score of the the player
        p2.getScore() # will call score function to compute the total score of the the computer
        p1.showPlayer() # will display the player's two cards
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        # An aesthetic break 
        if (p1.getScore() == 21): # Will call the score function to see if the conditions are met for a win or loss
            print(p1.name, "wins by Black Jack!")
            p1.wallet = p1.wallet + player1Bet * 2
            p2.wallet = p2.wallet - player1Bet
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p2.getScore() == 21 ): # Will call the score function to see if the conditions are met for a win or loss
            print(p2.name, "wins by Black Jack!")
            p2.wallet = p2.wallet + player1Bet 
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p2.getScore() == 21 and p1.getScore() == 21 ): # Will call the score function to see if the conditions are met for a win or loss
            print(p2.name, "wins by Black Jack!")
            p2.wallet = p2.wallet + player1Bet 
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p1.getScore() > 21): # Will call the score function to see if the conditions are met for a win or loss
            print(p1.name, "Busts !")
            p2.wallet = p2.wallet + player1Bet 
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p2.getScore() > 21 ): # Will call the score function to see if the conditions are met for a win or loss
            print(p2.name, "Busts !")
            p1.wallet = p1.wallet + player1Bet * 2
            p2.wallet = p2.wallet - player1Bet
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
# the dealer has delt cards to it self and the player
# the dealer has one card facing up
# the player can fully see their two cards          
        while(newCard): # This loop is only for the player turn to be over when it wants to or bc the conditions were made to turn it flase
            newCard = input("Would you like another Card?? y/n: ")
            print("---------------------------------------------------------")
            print("---------------------------------------------------------") # An aesthetic break 

            if (newCard == "y"):
                p1.getCard ( d.dealCard() )
                p1.getScore()                       # if input == y the player will get another card til it wants to stop or wins/loses
                p2.getScore()
                p1.showPlayer()
                p2.showDealer()
            elif (newCard == "n"):          # if the player wants to stop getting cards it will show what it has and go to the next loop
                p1.showPlayer()
                p2.showDealer()
                print("---------------------------------------------------------") # An aesthetic break 
                print("Now its the Dealer's turn......")
                while(True): # This loop is for the dealer to get more cards till the conditions are met
                    input("Dealer is Drawing another card......") # Allows the game to lag slightly for the computer to get a card by card
                    p2.getCard ( d.dealCard() ) # it will first get a card
                    p1.getScore()
                    p2.getScore()
                    p1.showPlayer()
                    p2.showDealer()
                    print("---------------------------------------------------------")
                    print("---------------------------------------------------------") # An aesthetic break 
                    if (p2.getScore() == 21): # Will call the score function to see if the conditions are met for a win or loss
                        print("______________________________")
                        print("                              ")
                        print("********",p2.name, "wins!", "********")
                        print("______________________________")
                        p2.wallet = p2.wallet + player1Bet 
                        player1wallet = p1.wallet
                        DealerWallet = p2.wallet
                        p1.showPlayer()
                        p2.showDealer()
                        newCard = False
                        break
                    elif (p2.getScore() > 21 ): # Will call the score function to see if the conditions are met for a win or loss
                        print("______________________________")
                        print("                              ")
                        print("********", p1.name, "wins!", "********")
                        print("______________________________")
                        p1.wallet = p1.wallet + player1Bet * 2
                        p2.wallet = p2.wallet - player1Bet
                        player1wallet = p1.wallet
                        DealerWallet = p2.wallet
                        p1.showPlayer()
                        p2.showDealer()
                        newCard = False
                        break
                    elif (p2.getScore() < 21  and p2.nCards == 5): # Will call the score function to see if the conditions are met for a win or loss
                        print("______________________________")
                        print("                              ")
                        print("********",p2.name, "wins!", "********")
                        print("______________________________")
                        p2.wallet = p2.wallet + player1Bet 
                        player1wallet = p1.wallet
                        DealerWallet = p2.wallet
                        p1.showPlayer()
                        p2.showDealer()
                        newCard = False
                        break
                    elif (p2.getScore() >= 17  and p2.getScore() < p1.getScore() ): # id the conditions are not met the Dealer will draw more cards
                        input("Dealer is Drawing another card......")
            if (p1.getScore() == 21): # Will call the score function to see if the conditions are met for a win or loss
                print("______________________________")
                print("                              ")
                print("********",p1.name, "wins!", "********")
                print("______________________________")
                p1.wallet = p1.wallet + player1Bet * 2  # updates the wallet if the player wins/loses      
                p2.wallet = p2.wallet - player1Bet
                player1wallet = p1.wallet
                DealerWallet = p2.wallet
                p1.showPlayer()
                p2.showDealer()
                newCard = False
                break
            elif (p1.getScore() > 21 ): # Will call the score function to see if the conditions are met for a win or loss
                print("______________________________")
                print("                              ")
                print("********", p2.name, "wins!", "********")
                print("______________________________")
                p2.wallet = p2.wallet + player1Bet  # updates the wallet if the player wins/loses
                player1wallet = p1.wallet
                DealerWallet = p2.wallet
                p1.showPlayer()
                p2.showDealer()
                newCard = False
                break
            elif (p1.getScore() < 21  and p1.nCards == 5): # Will call the score function to see if the conditions are met for a win or loss
                print("______________________________")
                print("                              ")
                print("********",p1.name, "wins!", "********")
                print("______________________________")
                p1.wallet = p1.wallet + player1Bet * 2 # updates the wallet if the player wins/loses
                p2.wallet = p2.wallet - player1Bet
                player1wallet = p1.wallet
                DealerWallet = p2.wallet
                p1.showPlayer()
                p2.showDealer()
                newCard = False
                break
        if (player1wallet <= 0): # will check if the players is broke to end the game automatically
            print("""House wins! Looks like you can't afford to play again""" )
            print("Players wallet", "$", p1.wallet)
            break
        nextRound = input("Do you to play a new Round?? y/n?: ") # will ask if the player wants to play another round and then will go back to the second inner loop
        if (nextRound == "y"):
            newCard = True
            print("---------------------------------------------------------")
            print("---------------------------------------------------------") # An aesthetic break
            print("starting a new Round....")
        elif (nextRound == "n"):
            break
    nextRound = input("Are you sure you don't want to play a new Round?? y/n?: ")   # will ask the player again to end game. 
    if (nextRound == "y"):
            break 

        


