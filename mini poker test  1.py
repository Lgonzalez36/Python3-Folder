#Prof. Kim
#11/6/2019
# mini poker game setup

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
        elif (v==10):
            self.faceValue = 'J'
        elif (v==10):
            self.faceValue = 'Q'
        elif (v==10):
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
        for i in range(0,10):
            self.cards[i] = Card("spades", i+2)
            
        
        
        
        for i in range(0,10):
            self.cards[ i + 13  ] = Card("hearts", i+2)
        
        for i in range(0,10):
            self.cards[ i + 26 ] = Card("diamonds", i+2)
        
        for i in range(0,10):
            self.cards[ i + 39 ] = Card("clubs", i+2)
        
        
        self.topIdx = 0
        
        
    
    def shuffle(self):
        #shuffle 
        for i in range(600):
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
        self.total = 0
        if (self.nCards < self.handSize):
            return self.total
        else:
            for i in range (self.nCards):
                self.total = self.total + self.hand[i].value
                
            return self.total
            
        
            
            
        
        
#-------------------------Main----------------------
d = Deck()


d.display()
  