import random

class Card:
    def __init__ (self, s, v):
        # s is the suit type:
        # "spades" "hearts" "diamonds" "clubs"
        # v is the number:
        # 1=A 2-10 J=11 Q=12 K=13
        #
        # self.value is the numerical value        
        # self.faceValue is what you see on the screen (A,J,Q,K)
        self.suit = s
        self.value = v
        if (v==1):
            self.faceValue = 'A'
        elif (v==11):
            self.faceValue = 'J'
        elif (v==12):
            self.faceValue = 'Q'
        elif (v==13):
            self.faceValue = 'K'
        else:
            self.faceValue = v            
        
    def display (self):
        if (self.suit == "spades"):
            print ("[\u2660",self.faceValue,"]",sep='')
        elif (self.suit == "hearts"):
            print ("[\u2661",self.faceValue,"]",sep='')
        elif (self.suit == "diamonds"):
            print ("[\u2662",self.faceValue,"]",sep='')
        elif (self.suit == "clubs"):
            print ("[\u2663",self.faceValue,"]",sep='')
            
            
    def __gt__(self, other):
           
        
        if (self.value == 1): #Ace
            myValue = 14
        else:
            myValue = self.value
            
        if (myValue == other.value):
            if (self.suit == "spades"):
                self.suit = 4
                myValue = myValue + self.suit
            elif (self.suit == "hearts"):
                self.suit = 3
                myValue = myValue + self.suit
            elif (self.suit == "diamonds"):
                self.suit = 2
                myValue = myValue + self.suit
            elif (self.suit == "clubs"):
                self.suit = 1
                myValue = myValue + self.suit
                
                
            
        if (other.value == 1): #Ace
            yourValue = 14
        else:
            yourValue = other.value
         
        if (myValue == other.value):
            
            if (other.suit == "spades"):
                other.suit = 4
                yourValue = other.suit + yourValue
            elif (other.suit == "hearts"):
                other.suit = 3
                yourValue = other.suit + yourValue
            elif (other.suit == "diamonds"):
                other.suit = 2
                yourValue = other.suit + yourValue
            elif (other.suit == "clubs"):
                other.suit = 1
                yourValue = other.suit + yourValue
            
        print ("c1 value ", myValue)
        print ("c2 value ", yourValue)
            
        return myValue > yourValue 
       
        

c1 = Card("spades", 1)   #Ace of spades
c2 = Card("diamonds", 1)  #King of  spades

if (c1 > c2):
    print("c1 is better")
else:
    print("c2 is better")
    
    








