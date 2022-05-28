#Prof. Kim
#11/8/2019
# mini poker game setup v.8

import random

#-------------------------Class Definition----------------------

class Card:
    def __init__ (self, s, v):
        # s is the suit type:
        # "spades" "hearts" "diamonds" "clubs"
        # v is the number:
        #  2-10 J=11 Q=12 K=13 A=14
        #
        # self.value is the numerical value        
        # self.faceValue is what you see on the screen (A,J,Q,K)
        self.suit = s
        self.value = v
        
        if (v==14):
            self.faceValue = 'A'
        elif (v==11):s
            self.faceValue = 'J'
        elif (v==12):
            self.faceValue = 'Q'
        elif (v==13):
            self.faceValue = 'K'
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
        self.cards = [None] * 52        
        for i in range(0,13):
            self.cards[i] = Card("spades", i+2)
        
        for i in range(0,13):
            self.cards[ i + 13  ] = Card("hearts", i+2)
        
        for i in range(0,13):
            self.cards[ i + 26 ] = Card("diamonds", i+2)
        
        for i in range(0,13):
            self.cards[ i + 39 ] = Card("clubs", i+2)
        
        self.topIdx = 0
        
        
    
    def shuffle(self):
        #shuffle 
        for i in range(300):
            idx1 = random.randint(0,51)
            idx2 = random.randint(0,51)
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
        
        self.hand = [None] * 3
        self.handSize = 3  #max capacity of the hand
        self.nCards = 0    #nCards: how many cards do I actually have at the moment
        
    def show(self):
        score = self.getScore()
        print(self.name, " $", self.wallet, " (",score, ")",sep='')
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
        #  except ACE=14
        if (self.nCards != 3):
            return 0
    
        if (self.hand[0].value == self.hand[1].value and self.hand[0].value == self.hand[2].value):            
            #triple
            return 1000 + self.hand[0].value
        elif (self.hand[0].value == self.hand[1].value):            
            #pair
            return 100 + self.hand[0].value
        elif (self.hand[0].value == self.hand[2].value):
            #pair
            return 100 + self.hand[0].value
        elif (self.hand[1].value == self.hand[2].value):
            #pair
            return 100 + self.hand[1].value            
        else:
            #figure out highest value card
            highCard = self.hand[0]
            
            for i in range(len(self.hand)):
                if (self.hand[i] > highCard):
                    highCard = self.hand[i]
                       
            pts = highCard.value
            
            if (highCard.suit == "spades"):
                pts = pts + 0.4
            elif (highCard.suit == "hearts"):
                pts = pts + 0.3
            elif (highCard.suit == "diamonds"):
                pts = pts + 0.2
            elif (highCard.suit == "clubs"):
                pts = pts + 0.1
            
            return pts
            
            
    
        
        
#-------------------------Main----------------------
d = Deck()
p1 = Player("Colin", 20)
p2 = Player("John", 20)
while(True):
    d.shuffle()
    #d.display()
    
    print("")
    
    
    
    for i in range(3):
        p1.getCard ( d.dealCard() )
        
        p2.getCard ( d.dealCard() )
           
    
        
    p1.show()
    p2.show()
    
    if (p1 > p2):
        print(p1.name, "wins!")
    elif (p1 < p2):
        print(p2.name, "wins!")
    else:
        print("tie!")
    
    input("Do you wanna continue? Yes?")





