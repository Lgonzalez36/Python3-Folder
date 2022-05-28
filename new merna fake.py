# Merna Saad and Luis Gonzalez 
# Professor Kim 
# group project: ConnectFour 
# Octber 18, 2019 

#-------------------------------Original Definition----------------------------
import random


def displayBoard(gameBoard):
	# gameBoard is a 2d list (size: 6x7)
	for i in range(len(gameBoard)):
		print("---------------")
		print("|",end='')
		for j in range(len(gameBoard[0])): # each colum within a row  
			print(gameBoard[i][j], end='|')
		print("\n")
	print("---------------")
	print("\n__________________________________\n")
		   
	
def checkUserWin(gameBoard, Row, Col):
    # win condition check for four in a row (6x7)
    # returns True if there is a win
    # returns False otherwise
    
#check Col -------------------------------------------------------------------------------

    
    
    for i in range(0, 3, 1):
        for j in range(0, 7, 1):
            if (gameBoard[i][j] == 'O' and
                gameBoard[i + 1][j] == 'O' and 
                gameBoard[i + 2][j] == 'O' and
                gameBoard[i + 3][j] == 'O'):
                return 'O'

#check Row-------------------------------------------------------------------------------
    
    for i in range(0, 6, 1):
        for j in range(0, 4, 1):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i][j + 1] == 'O' and
                gameBoard[i][j + 2] == 'O' and
                gameBoard[i][j + 3] == 'O'):
                return 'O'
 
#check for diagaonal in the positive slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(3, len(gameBoard)):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j - 1] == 'O' and
                gameBoard[i + 2][j - 2] == 'O' and
                gameBoard[i + 3][j - 3] == 'O'):
                return 'O'                      

#check for diagaonal in the negative slop ------------------------------------------------------------------
    for i in range(len(gameBoard) - 3):
        for j in range(len(gameBoard) - 3):
            if (gameBoard[i][j] == 'O' and 
                gameBoard[i + 1][j + 1] == 'O' and
                gameBoard[i + 2][j + 2] == 'O' and
                gameBoard[i + 3][j + 3] == 'O'):
                return 'O'
                
                
    return 'O'
   
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
	return -1

def isColValid(gameBoard, colNum):
	for i in range(5, -1, -1):
		if(board[i][colNum] == ' '):
			return i
	return -1
	#return an empty space
    
def userTurn(): # let the user play first  
	while(True):
		col = int(input("Enter col:"))
		row = isColValid(board, col)
		if row == -1:
			print("that column is already full!") # use different col b/c this one is already full 
    
		else:
			board[row][col] = 'X'
			return col
        
	# let the pcTurn make a move 		
def pcTurn():
	while(True):
		value = checkBotWin(board)
		if value == -1:
			col = random.randint(0, 6)
			row = isColValid(board, col)
			if row != -1:  # start at the bottom of the col and go up 
				board[row][col] = 'O'
				return col
		else:
			row = isColValid(board, value)
			board[row][value] = 'O'
			return value
		
def undo_func(board, pc_col, user_col): # use the undo_func to undo a move that you made  
  # compture move will also be removed 
  
	while(True):
		ans = str(input("undo? y/n: "))
		if ans == 'y':
			pc_row = isColValid(board, pc_col)+1
			board[pc_row][pc_col] = ' '    # empty space is found 
			user_row = isColValid(board, user_col)+1
			board[user_row][user_col] = ' '  # empty space is found 
			break
		elif ans == 'n':
			break
		else:
			print("invalid answer")
            
    #ask the user if they want to play again          
def play_again():
    again = str(input("Wanna play again? y/n: "))
    if again == 'y':
        print("_____________________")
        print("|Starting a new game|")
        print("---------------------")
    elif again == 'n':
        exit()	
        # if dont wanna play again then quit the game 
    return again
#-------------------------------original program-------------------------------        
        
while(True):
       # this is the table for the game board
    #which is also known as displayboard
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    winner = ' '

    while(True):
        displayBoard(board)
        user_col = userTurn()
        displayBoard(board)
        winner = checkUserWin(board)
        if winner == 'X': # let X make the move and see if they won 
            print("You won!")
            break
        elif winner == 'O': # let O make the move and see if they won 
            print("Computer won!")
            break	
        pc_col = pcTurn()
        displayBoard(board)
        undo_func(board, pc_col, user_col)
        winner = checkUserWin(board)
        if winner == 'X':
            print("You won!")
            break
        elif winner == 'O': # let O make the move and see if they won 
            print("Computer won!")
            break
    #play_again():
    again = str(input("Wanna play again? y/n: "))
    if again == 'y':
        print("_____________________")
        print("|Starting a new game|")
        print("---------------------")
    elif again == 'n':
        break	
        # if dont wanna play again then quit the game 

    
