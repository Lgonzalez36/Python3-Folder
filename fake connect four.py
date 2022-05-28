# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:51:52 2019

@author: luisg
"""
import random
#................................. Function definitions ..................................
##########################################################################################
def displayBoard(gameBoard):
    # gameBoard is a 2d list (size: 3x3)
    for i in range(len(gameBoard)): # for each row
        print("---------------")
        print("|",end='')
        for j in range(len(gameBoard[0])): #each col, w/in a row
            print(gameBoard[i][j],end='|')
        print("")   
    print("---------------")
# this function allows the table to look pleasent 
##########################################################################################
##########################################################################################
def checkUserWin(gameBoard, Row, Col):
    # win condition check for four in a row (6x7)
    # returns True if there is a win
    # returns False otherwise
    
#check Col -------------------------------------------------------------------------------

    fourInaRow = False
    
    for i in range(0, 3, 1):
        for j in range(0, 7, 1):
            if (gameBoard[i][j] == 'O' and
                gameBoard[i + 1][j] == 'O' and 
                gameBoard[i + 2][j] == 'O' and
                gameBoard[i + 3][j] == 'O'):
                fourInaRow = True   

#check Row-------------------------------------------------------------------------------
    
    for i in range(0, 6, 1):
        for j in range(0, 4, 1):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i][j + 1] == 'O' and
                gameBoard[i][j + 2] == 'O' and
                gameBoard[i][j + 3] == 'O'):
                fourInaRow = True
 
#check for diagaonal in the positive slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(3, len(gameBoard)):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j - 1] == 'O' and
                gameBoard[i + 2][j - 2] == 'O' and
                gameBoard[i + 3][j - 3] == 'O'):
                fourInaRow = True                      

#check for diagaonal in the negative slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(len(gameBoard) - 3):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j + 1] == 'O' and
                gameBoard[i + 2][j + 2] == 'O' and
                gameBoard[i + 3][j + 3] == 'O'):
                fourInaRow = True
                
                
    return fourInaRow   
   
##########################################################################################
def checkBotWin(gameBoard, Row, Col):
    # the computer will make a counter move after the user input
#check Col -------------------------------------------------------------------------------

    fourInaRow = False
    
    for i in range(0, 3, 1):
        for j in range(0, 7, 1):
            if (gameBoard[i][j] == 'X' and
                gameBoard[i + 1][j] == 'X' and 
                gameBoard[i + 2][j] == 'X' and
                gameBoard[i + 3][j] == 'X'):
                fourInaRow = True   

#check Row-------------------------------------------------------------------------------
    
    for i in range(0, 6, 1):
        for j in range(0, 4, 1):
            if (gameBoard[i][j] == 'X' and 
                gameBoard[i][j + 1] == 'X' and
                gameBoard[i][j + 2] == 'X' and
                gameBoard[i][j + 3] == 'X'):
                fourInaRow = True
 
#check for diagaonal in the positive slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(3, len(gameBoard)):
            if (gameBoard[i][j] == 'X' and 
                gameBoard[i + 1][j - 1] == 'X' and
                gameBoard[i + 2][j - 2] == 'X' and
                gameBoard[i + 3][j - 3] == 'X'):
                fourInaRow = True                      

#check for diagaonal in the negative slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(len(gameBoard) - 3):
            if (gameBoard[i][j] == 'X' and 
                gameBoard[i + 1][j + 1] == 'X' and
                gameBoard[i + 2][j + 2] == 'X' and
                gameBoard[i + 3][j + 3] == 'X'):
                fourInaRow = True
                
                
    return fourInaRow   
##########################################################################################
def counterMove(gameBoard, Row, Col):
    
    # the computer will make a counter move after the user input
    BotMove = Col
    
#check Col -------------------------------------------------------------------------------

    for i in range(0, 3, 1):
        for j in range(0, 7, 1):
            if (gameBoard[i][j] == 'O' and
                gameBoard[i + 1][j] == 'O' and 
                gameBoard[i + 2][j] == 'O'):
                gameBoard[i + 3][j] = 'X'
                BotMove = gameBoard[i + 3][j]
                
            elif (gameBoard[i][j] == 'O' and
                gameBoard[i + 2][j] == 'O' and 
                gameBoard[i + 3][j] == 'O'):
                gameBoard[i + 1][j] = 'X'
                BotMove = gameBoard[i + 1][j]
                
            elif (gameBoard[i][j] == 'O' and
                gameBoard[i + 1][j] == 'O' and 
                gameBoard[i + 3][j] == 'O'):
                gameBoard[i + 2][j] = 'X'
                BotMove = gameBoard[i + 2][j]
                
            elif (gameBoard[i][j] == ' ' and
                gameBoard[i + 1][j] == 'O' and 
                gameBoard[i + 2][j] == 'O' and 
                gameBoard[i + 3][j] =='O'):
                gameBoard[i][j] = 'X'
                BotMove = gameBoard[i][j]
                  

#check Row-------------------------------------------------------------------------------
    
    for i in range(0, 6, 1):
        for j in range(0, 4, 1):
            if (gameBoard[i][j] == 'O' and
                gameBoard[i][j + 1] == 'O' and 
                gameBoard[i][j + 2] == 'O'):
                gameBoard[i][j + 3] = 'X'
                BotMove = gameBoard[i][j + 3]
                
            elif (gameBoard[i][j] == 'O' and
                gameBoard[i][j + 2] == 'O' and 
                gameBoard[i][j + 3] == 'O'):
                gameBoard[i][j + 1] = 'X'
                BotMove = gameBoard[i][j + 1]
                
            elif (gameBoard[i][j] == 'O' and
                gameBoard[i][j + 1] == 'O' and 
                gameBoard[i][j + 3] == 'O'):
                gameBoard[i][j + 2] = 'X'
                BotMove = gameBoard[i][j + 2]
                
            elif (gameBoard[i][j] == ' ' and
                gameBoard[i][j + 1] == 'O' and 
                gameBoard[i][j + 2] == 'O' and 
                gameBoard[i][j + 3] =='O'):
                gameBoard[i][j] = 'X'
                BotMove = gameBoard[i][j]
               
 
#check for diagaonal in the positive slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(3, len(gameBoard)):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j - 1] == 'O' and
                gameBoard[i + 2][j - 2] == 'O'):
                gameBoard[i + 3][j - 3] = 'X'
                BotMove = gameBoard[i + 3][j - 3]
                
            elif (gameBoard[i][j] == 'O' and 
                gameBoard[i + 2][j - 2] == 'O' and
                gameBoard[i + 3][j - 3] == 'O'):
                gameBoard[i + 1][j - 1] = 'X'
                BotMove = gameBoard[i + 1][j - 1]
                
            elif (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j - 1] == 'O' and
                gameBoard[i + 3][j - 3] == 'O'):
                gameBoard[i + 2][j - 2] = 'X'
                BotMove = gameBoard[i + 2][j - 2]
                
            elif (gameBoard[i][j] == ' ' and 
                gameBoard[i + 1][j - 1] == 'O' and
                gameBoard[i + 2][j - 2] == 'O' and
                gameBoard[i + 3][j - 3] == 'O'):
                gameBoard[i][j] = 'X'
                BotMove = gameBoard[i][j]
                                  

#check for diagaonal in the negative slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(len(gameBoard) - 3):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j + 1] == 'O' and
                gameBoard[i + 2][j + 2] == 'O'):
               
                gameBoard[i + 3][j] = BotMove
              
                
                
    return BotMove   
##########################################################################################   
#check vadlid col to drop piec ------------------------------------------------------------------
def valid_locationX(gameBoard, Col):
    
    for i in range(5, -1, -1):
        if (board[i][Col] == ' '):
            #empty slot is found
            board[i][Col] = 'X' #made it go to the bottem of the row
            break
            #make sure the chosen spot is empty   
def valid_locationO(gameBoard, Col):
    
    for i in range(5, -1, -1):
        if (board[i][Col] == ' '):
            #empty slot is found
            board[i][Col] = 'O' #made it go to the bottem of the row
            break
            #make sure the chosen spot is empty 

#................................. Main Program ..................................
    
board = [ [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
displayBoard (board)
# this is the table for the game board
# and aslo calls the function to display the board

cnt = 0
rowCount = 0
game_Over = True




while(game_Over):
    row=int(input("O: enter row#:"))
    col=int(input("O: enter col#:"))
        
    #make sure the chosen spot is empty
    while (board[row][col] != ' '): 
        row=int(input("O: enter row#:"))
        col=int(input("O: enter col#:"))  
                      
    
    valid_locationO(board, col)
        
    cnt = cnt + 1
    displayBoard (board)
    
    if (checkUserWin(board, row, col) == True):
        print ("O wins!")
        break
                
    
    if (cnt== 42): #check to see if there is a tie at the end
        print("Tie!")
        break
    
    Col = random.randint(0, 6)
    Row = random.randint(0, 5)
    
   
    
    counterMove(board, Row, Col)
    valid_locationX(board, Col)

    displayBoard (board)
    
    if (checkBotWin(board, row, Col) == True):
        print ("X wins!")
        break
    cnt = cnt + 1  
 
 





