# CSCE 160
# Luis Gonzalez Jeff Gonzalez
# Sudoku w/ file use
##################################################################################
#--------------------------class and functions-------------------------------------------            
##################################################################################
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
#------------------------------------------------------------------------------        
    def updateGame (self, r, c, v):
        self.Row = r #user row input
        self.Col = c #user col input
        self.value = v #user value input
        self.file =  open ('sudoku1_copy.txt', 'r') #import file to game
        #read data as an array of strings
        self.data = self.file.readlines() # sets the data into an array of strings
        self.board[self.Row][self.Col] = self.value #updated board
        #print(self.origBoard)
        #print(self.board)
        #close the file
        self.file.close()        
        self.matrix(self.origBoard, self.board) #calls for function to merge
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------ 
    def matrix(self, ori, board ):
        self.original = ori #save to new object
        self.tracker = board #save to new obect
        self.fuse = [None] * 9 #creates a list to merge both boards
        self.full = False #asuming its not full
        for i in range(9):
            self.fuse[i] = [None] * 9 #makes the list for the merge
            for j in range(9):
                if (self.original[i][j] == ' '):
                    self.fuse[i][j] = '' + self.tracker[i][j]
                    if (self.tracker[i][j] == ' '):
                        self.fuse[i][j] = '0'
                else:
                    self.fuse[i][j] =  self.original[i][j]
        #this is going to merge the two boards together
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
    def BlockUnique(self, b, r, c):
        Fuse = b 
        Blockunique = True
        for i in range (9):             
            for j in range (9):
                Fuse[i][j] = int(Fuse[i][j])
        for num in range (1,10): #for EACH values 1-9
            count = 0
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if (Fuse[i][j] == num):
                        count += 1
            if (count!=1): #MUST have a count of 1
                Blockunique = False
        return Blockunique #its going to check 3x3 at a time and return True or False
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------        
    def rowUnique(self, m, rowNum):
        Fuse = m
        unique = True
        for i in range (9):
            for j in range (9):
                Fuse[i][j] = int(Fuse[i][j])
        for num in range (1,10): #for EACH values 1-9
            count = 0
            for j in range(9):
                if (Fuse[0][j] == num):
                    count += 1
            if (count!=1): #MUST have a count of 1
                unique = False
        return unique #its going to check for row uniqueness and return true or false
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
    def colCheck (self, f, colNum):
        Fuse = f
        Colunique = True
        for i in range (9):
            for j in range (9):
                Fuse[i][j] = int(Fuse[i][j])
        for num in range (1,10): #for EACH values 1-9
            count = 0
            for j in range(9):
                if (Fuse[j][0] == num):
                    count += 1
            if (count!=1): #MUST have a count of 1
                Colunique = False
        return Colunique  #its going to check for col uniqueness and return true or false
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------        
    def saveGame(self, fileName=None):
        if (fileName==None):
            print("You must provide a file name so we can save the game!")
        else:
            print("Saving to:", fileName)
            with open('sudoku1_copy.txt', 'w') as new_copy: #open the file
                #first going to write the origBoard 
                for i in range (9):
                    for j in range(9):
                        new_copy.write(self.origBoard[i][j])
                    new_copy.write("\n")
                #going to write the user board right after to the fil
                for k in range (9,18):
                    for l in range (9):
                        if (self.board[k - 9][l] != "0"):
                            new_copy.write(self.board[k - 9][l])
                    new_copy.write("\n")
            #process origBoard and board and write it to the file
            #close file
##################################################################################
#--------------------------Main program-------------------------------------------            
##################################################################################            
try:    
    game = Sudoku("sudoku1_copy.txt")    
except:
    game = Sudoku()
full = False 
Rowsolved = False
Colsolved = False
Blocksolved = False
user_number = '' #inituates user_number
#sets up to assume the puzzle is not solved
while (True):
    game.display()
    print("pick an allowed location by column and row: ")
    Row = int(input("Enter a Row: "))
    Col = int(input("Enter a Column: "))
    user_number = str(input("Now Enter a number from 1-9 you want to insert: "))
    #loads all info to usable variables
    while( user_number == game.origBoard[Row][Col] or user_number == '0' ): 
        Row = int(input("Enter a Row: "))
        Col = int(input("Enter a Column: ")) #if not valid it would ask you to try again
        user_number = str(input("Now Enter a number from 1-9 you want to insert: "))
        
    game.updateGame(Row, Col, user_number) #calls function to update the board
    save = input("Would you like to save the game? y/n: ")
    if(save == "y"):
        game.saveGame("sudoku1_copy.txt") #calls the function to  save into the file
    else:
        print("if you say so...")
    
    for i in range (9):
        if (game.rowUnique(game.fuse, i) == False):
            Rowsolved = False
        else:
            Rowsolved = True
    for k in range (9):
        if (game.colCheck(game.fuse, k) == False):
            Colsolved = False
        else:
            Colsolved = True
    #for r in range (0,7,3): #will check all the 3x3 to see if it is true or false
        #for c in range(0,7,3):
    if (game.BlockUnique(game.fuse, 0, 0) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 0, 3) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 0, 6) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 3, 0) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 3, 3) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 3, 6) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 6, 0) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 6, 3) == False):
        Blocksolved = False
    if (game.BlockUnique(game.fuse, 6, 6) == False):
        Blocksolved = False
 
    if (Colsolved == True and Rowsolved == True and Blocksolved == True):
        print("you won the game!!!")
    else:
        print("continue its still not solved!")

    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    
    
    
    
    
    