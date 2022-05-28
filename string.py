# CSCE 160
# Prof. Kim
# Sudoku w/ file use

import random
import sys, os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Sudoku:
    def __init__(self, fileName=None):
        self.origBoard = [None] * 9  # Used to mark original puzzle state
        self.board = [None] * 9      # Used to mark user-entered numbers
        for i in range(9):
            self.board[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
            self.origBoard[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
        
        if (fileName==None):  # default puzzle
            self.default()
        else:                 # create puzzle
            self.readFile(fileName)
#------------------------------------------------------------------------------        
   
    def readFile(self, fn):
        
        #fileformat
        #9 lines of original puzzle state
        #9 lines of user entered values
        #Use 0 for empty space
        #Example (refer to the puzzle in the default function):
        # [2,4,3,7,0,1,8,6,9]
        # [5,0,7,9,0,0,0,3,0]
        # [0,1,0,0,4,0,0,0,5]
        # [0,2,0,0,7,0,5,0,0]
        # [3,0,5,0,0,0,2,0,7]
        # [0,0,1,0,3,0,0,4,0]
        # [1,0,0,0,9,0,0,7,0]
        # [0,6,0,0,0,7,4,0,8]
        # [7,3,4,5,0,8,6,9,1]
        
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        # [0,0,0,0,0,0,0,0,0]
        
        #setup file to open
        self.file = open(os.path.join(__location__,fn), 'r')
        
        #read data as an array of strings
        self.data = self.file.readlines()
        print(self.data)
        print("$$$$$$$$$$$$$$$$$$")
        
        #treat the array of strings as a matrix of characters
        #First, process the portion that belongs to the original board
        for i in range(9):
            for j in range(9):
                if (self.data[i][j] != '0'):
                    self.origBoard[i][j] = self.data[i][j] #from the sudoku1.txt file

        #Then, process the user entered values
        for i in range(9,18): #row index 9~17
            for j in range(9):
                if (self.data[i][j] != '0'):
                    self.board[i-9][j] = self.data[i][j]
        #close the file
        self.file.close()
#------------------------------------------------------------------------------        
       
    def default(self):
        #user did not provide a puzzle so we will provide one
        self.origBoard[0]=' 19374652'
        self.origBoard[1]='576182943'
        self.origBoard[2]='342596718'
        self.origBoard[3]='921753864'
        self.origBoard[4]='638419527'
        self.origBoard[5]='457628139'
        self.origBoard[6]='185237496'
        self.origBoard[7]='763941285'
        self.origBoard[8]='29486537 '

#------------------------------------------------------------------------------        
                   
    def display(self):
        #combine original board and current board
        db = [None] * 9
        for i in range(9):
            db[i] = [None] * 9
            for j in range(9):
                if (self.origBoard[i][j] == ' '):
                    db[i][j] = ' ' + self.board[i][j]
                else:
                    db[i][j] = '*' + self.origBoard[i][j]
        #format and print
        print("   0  1  2  3  4  5  6  7  8")
        print(" \u2554\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2566\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2566\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2557")
        i=0
        for m in range(0,3):
            for k in range(0,2):
                print(i,"\u2551",sep='',end='')
                for j in range(0,9,3):
                    print(db[i][j], db[i][j+1], db[i][j+2], sep='\u2502', end='\u2551')
                print("")
                print(" \u255F\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u256B\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u256B\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u2562")
                i+=1
            print(i,"\u2551",sep='',end='')
            for j in range(0,9,3):
                print(db[i][j], db[i][j+1], db[i][j+2], sep='\u2502', end='\u2551')
            print("")
            if (m<2):
                print(" \u255F\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u256C\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u256C\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u2562")
            else:
                print(" \u255A\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u2569\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u2569\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u255D")
            i+=1
#------------------------------------------------------------------------------        
           
    def updateGame (self, r, c, v):
        self.Row = r 
        self.Col = c
        self.value = v
        
        self.file =  open ('sudoku1_copy.txt', 'r')
        
        #read data as an array of strings
        self.data = self.file.readlines()
        
        
        #close the file
        self.board[self.Row][self.Col] = self.value
        print(self.origBoard)
        print(self.board)
        
        #close the file
        self.file.close()
        
       #MERGE =  + self.board
        
        self.matrix(self.origBoard, self.board)
    
#------------------------------------------------------------------------------ 
    def matrix(self, ori, board ):
        self.original = ori
        self.tracker = board
        self.fuse = [None] * 9
        self.full = False
        for i in range(9):
            self.fuse[i] = [None] * 9
            for j in range(9):
                if (self.original[i][j] == ' '):
                    self.fuse[i][j] = ' ' + self.tracker[i][j]
                    self.fuse[i][j] = '0'
                else:
                    self.fuse[i][j] =  self.original[i][j]
                if (self.fuse[i][j] != '0'):
                    self.full = True
                    print(self.full)
                    return self.full
        print("**********************************")
        print(self.fuse)
        print("**********************************")
        
            
                
                
#------------------------------------------------------------------------------        
    def rowUnique(self, m, rowNum):
        Fuse = m
        unique = True
        for i in range (9):
            for j in range (9):
                Fuse[i][j] = [ int(x) for x in Fuse[i][j]]
            
        print(Fuse)
        print("BOBOBOBOBOBOBOBOBBO")
        
        for num in range (1,10): #for EACH values 1-9
            count = 0
            for j in range(9):
                if (self.fuse[0][j] == num):
                    count = count + 1
                    print(count, "@@@@@@")
            if (count!=1): #MUST have a count of 
                print(count, "*******")
                unique = False
                print("you lose")
            else:
                print(count, "&&&&&&&")
                print("you good for now")
                return unique
#------------------------------------------------------------------------------        
    def saveGame(self, fileName=None):
        if (fileName==None):
            print("You must provide a file name so we can save the game!")
        else:
            print("Saving to:", fileName)
            #open file (for writing)
            
            with open('sudoku1_copy.txt', 'w') as new_copy:
                for i in range (9):
                    for j in range(9):
                        new_copy.write(self.origBoard[i][j])
                    new_copy.write("\n")
                    
                for k in range (9,18):
                    for l in range (9):
                        if (self.board[k - 9][l] != "0"):
                            new_copy.write(self.board[k - 9][l])
                    new_copy.write("\n")
           
            #process origBoard and board and write it to the file
            #close file
            
try:    
    game = Sudoku("sudoku1_copy.txt")    
except:
    game = Sudoku()
full = False

while (True):
    
    game.display()
    
    print("pick an allowed location by column and row: ")
    
    Row = int(input("Enter a Row: "))
    Col = int(input("Enter a Column: "))
    user_number = str(input("Now Enter a number from 1-9 you want to insert: "))
    
    while( user_number == game.origBoard[Row][Col] ):
        Row = int(input("Enter a Row: "))
        Col = int(input("Enter a Column: "))
        user_number = str(input("Now Enter a number from 1-9 you want to insert: "))
        
    
    game.updateGame(Row, Col, user_number)
    choice = input("would you like to save? y/n: ")
    if (choice == "y"):
        game.saveGame("sudoku1_copy.txt")
    else:
        print("if you say so...")
        
        
#The flag unique can now be used 
    
    if (game.full == True):
        print(game.full)
        for i in range (9):
            if (game.rowUnique(game.fuse, i) == False):
                solved = False
                
            else:
                print("continue")

            
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    
    
    
    



    