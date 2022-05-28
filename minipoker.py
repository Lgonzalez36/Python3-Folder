#Luis gpnzalez
#11/20/2019
# BlackJack game 

import random

#-------------------------Class Definition---------------------- 

class Card:
    def __init__ (self, s, v):
        # s is the suit type:
        # "spades" "hearts" "diamonds" "clubs"
        # v is the number:
        #  2-10 J=10 Q=10 K=10 A=10
        #
        # self.value is the numerical value        
        # self.faceValue is what you see on the screen (A,J,Q,K)
        self.suit = s
        self.value = v
        
        if (v==14):
            self.faceValue = 'A'
            self.value = 11
        elif (v==11):
            self.faceValue = 'J'
            self.value = 10
        elif (v==12):
            self.faceValue = 'Q'
            self.value = 10
        elif (v==13):
            self.faceValue = 'K'
            self.value = 10
        else:
            self.faceValue = v            
        
    def display (self):
        if (self.suit == "spades"):
            print ("[\u2660",self.faceValue,"]",sep='',end='')
        elif (self.suit == "hearts"):
            print ("[\u2661",self.faceValue,"]",sep='',end='')
        elif (self.suit == "diamonds"):
            print ("[\u2662",self.faceValue,"]",sep='',end='')
        elif (self.suit == "clubs"):
            print ("[\u2663",self.faceValue,"]",sep='',end='')

    def __gt__(self, other):
        return self.value > other.value

class Deck:
    def __init__ (self):
        #make a full deck
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

    def dealCard(self):
        index = self.topIdx
        self.topIdx = self.topIdx + 1
        return self.cards[ index ]
        

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
        
    def showDealer(self,):

        print(self.name, " $", self.wallet,sep='')
        if (self.nCards == 2 and newCard == "n"):        
            self.hand[0].display()
        else:
            for i in range(self.nCards):
                self.hand[i].display()
                
        print("")
        
    def getCard(self, aCard):     
        
        self.hand[ self.nCards ] = aCard
        self.nCards = self.nCards + 1
        
    def __gt__ (self, other):
        myScore = self.getScore()
        yourScore = other.getScore()        
        return myScore > yourScore
    
    def __lt__ (self, other):
        return self.getScore() < other.getScore()

        
    def getScore(self):
        # if we don't have 3 cards yet, return 0
        # triple = 1000 points
        # pair = 100 points
        # highcards = points == value of the highest card
        #  except ACE=1
        total = 0
        
        for i in range (self.nCards):
            total = total + self.hand[i].value
        
        for i in range (self.nCards):
            if (self.hand[i].value == 11 and total > 21):
                total = total - 10
               
        
        return total 


               
        
#-----------------------------------------------Main--------------------------------------------
d = Deck()
d.shuffle()
        #d.display()
newCard = True
print("--------------------------------------")
player1Name = str(input("Enter your name: "))
player1wallet = int(input("Enter the amount of money you want to play with: "))
DealerWallet = player1wallet * 2

p1 = Player(player1Name, player1wallet)
p2 = Player("Dealer", DealerWallet)
while(True):
    d.shuffle()
    #d.display()
    while(True):
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
                
                          
            
        d.shuffle()
        #d.display()
        
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        
        p2.getCard ( d.dealCard() )
        p2.showDealer()
        p2.getCard ( d.dealCard() ) #the hidden card from the player's view

        
        for i in range(2):
            p1.getCard ( d.dealCard() )
        p1.getScore()
        p2.getScore()
        p1.showPlayer()
        
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        
        
        if (p1.getScore() == 21):
            print(p1.name, "wins by Black Jack!")
            p1.wallet = p1.wallet + player1Bet * 2
            p2.wallet = p2.wallet - player1Bet
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p2.getScore() == 21 ):
            print(p2.name, "wins by Black Jack!")
            p2.wallet = p2.wallet + player1Bet 
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p2.getScore() == 21 and p1.getScore() == 21 ):
            print(p2.name, "wins by Black Jack!")
            p2.wallet = p2.wallet + player1Bet 
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p1.getScore() > 21):
            print(p1.name, "Busts !")
            p2.wallet = p2.wallet + player1Bet 
            player1wallet = p1.wallet
            DealerWallet = p2.wallet
            p1.showPlayer()
            p2.showDealer()
            break
        elif (p2.getScore() > 21 ):
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
        
        
        
        while(newCard):
            newCard = input("Would you like another Card?? y/n: ")
            print("---------------------------------------------------------")
            print("---------------------------------------------------------") 
            
            
            if (newCard == "y"):
                p1.getCard ( d.dealCard() )
                p1.getScore()
                p2.getScore()
                p1.showPlayer()
                p2.showDealer()
                
            
            elif (newCard == "n"):
                p1.showPlayer()
                p2.showDealer()
                print("---------------------------------------------------------") 

                print("Now its the Dealer's turn......")
                while(True):
                    input("Dealer is Drawing another card......")
                    p2.getCard ( d.dealCard() )
                    p1.getScore()
                    p2.getScore()
                    p1.showPlayer()
                    p2.showDealer()
                    print("---------------------------------------------------------")
                    print("---------------------------------------------------------") 
                  
                    
                    
                    if (p2.getScore() == 21):
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
                    elif (p2.getScore() > 21 ):
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
                    elif (p2.getScore() < 21  and p2.nCards == 5):
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
                    elif (p2.getScore() >= 17  and p2.getScore() < p1.getScore() ):
                        input("Dealer is Drawing another card......")
                       
            if (p1.getScore() == 21):
                print("______________________________")
                print("                              ")
                print("********",p1.name, "wins!", "********")
                print("______________________________")
                p1.wallet = p1.wallet + player1Bet * 2
                p2.wallet = p2.wallet - player1Bet
                player1wallet = p1.wallet
                DealerWallet = p2.wallet
                p1.showPlayer()
                p2.showDealer()
                newCard = False
                break
            elif (p1.getScore() > 21 ):
                print("______________________________")
                print("                              ")
                print("********", p2.name, "wins!", "********")
                print("______________________________")
                p2.wallet = p2.wallet + player1Bet 
                player1wallet = p1.wallet
                DealerWallet = p2.wallet
                p1.showPlayer()
                p2.showDealer()
                newCard = False
                break
            elif (p1.getScore() < 21  and p1.nCards == 5):
                print("______________________________")
                print("                              ")
                print("********",p1.name, "wins!", "********")
                print("______________________________")
                p1.wallet = p1.wallet + player1Bet * 2
                p2.wallet = p2.wallet - player1Bet
                player1wallet = p1.wallet
                DealerWallet = p2.wallet
                p1.showPlayer()
                p2.showDealer()
                newCard = False
                break
            
         
        if (player1wallet <= 0):
            print("""House wins! Looks like you can't afford to play again""" )
            print("Players wallet", "$", p1.wallet)
            break
                
    

        
        nextRound = input("Do you to play a new Round?? y/n?: ")
        
        
        if (nextRound == "y"):
            newCard = True
            print("---------------------------------------------------------")
            print("---------------------------------------------------------")

            
            print("starting a new Round....")
            
        elif (nextRound == "n"):
            break
    nextRound = input("Do you to play a new Round?? y/n?: ")   
    
    if (nextRound == "n"):
            break 

        


