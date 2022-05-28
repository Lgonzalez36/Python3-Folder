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
		   
	
def checkBoard(board):    # win condition check for four in a row (6x7)
    # returns True if there is a win
    # returns False otherwise 
    
	for row in range(6):    # check rows 
		for col in range(4):
			if (board[row][col]== 'X') and (board[row][col+1]== 'X') and (board[row][col+2]== 'X') and (board[row][col+3]== 'X'):
				return 'X'
			elif (board[row][col]== 'O') and (board[row][col+1]== 'O') and (board[row][col+2]== 'O') and (board[row][col+3]== 'O'):
				return 'O'
# check col for each one  	
	for col in range(7):
		for row in range(3):	
			if (board[row][col]== 'X') and (board[row+1][col]== 'X') and (board[row+2][col]== 'X') and (board[row+3][col]== 'X'):
				return 'X'
			elif (board[row][col]== 'O') and (board[row+1][col]== 'O') and (board[row+2][col]== 'O') and (board[row+3][col]== 'O'):
				return 'O'
				
	for col in range(4):
		for row in range(3, 6):	
			if (board[row][col]== 'X') and (board[row-1][col+1]== 'X') and (board[row-2][col+2]== 'X') and (board[row-3][col+3]== 'X'):
				return 'X'
			elif (board[row][col]== 'O') and (board[row-1][col+1]== 'O') and (board[row-2][col+2]== 'O') and (board[row-3][col+3]== 'O'):
				return 'O'
				
	for col in range(4):
		for row in range(3):	
			if (board[row][col]== 'X') and (board[row+1][col+1]== 'X') and (board[row+2][col+2]== 'X') and (board[row+3][col+3]== 'X'):
				return 'X'
			elif (board[row][col]== 'O') and (board[row+1][col+1]== 'O') and (board[row+2][col+2]== 'O') and (board[row+3][col+3]== 'O'):
				return 'O'				

def pcSmart(board):
	for j in range(7):   #check col 
		for i in range(5, -1, -1):
			if (board[i][j]== ' ') and (board[i-1][j]== 'X') and (board[i-2][j]== 'X') and (board[i-3][j]== 'X'):
				return j
            
               #check for diagonal in the positive slope
	for i in range(5, -1, -1):
		for j in range(3):
			if (board[i][j]== ' ') and (board[i][j+1]== 'X') and (board[i][j+2]== 'X') and (board[i][j+3]== 'X'):
				return j
			elif (board[i][j]== 'X') and (board[i][j+1]== ' ') and (board[i][j+2]== 'X') and (board[i][j+3]== 'X'):
				return j+1
			elif (board[i][j]== 'X') and (board[i][j+1]== 'X') and (board[i][j+2]== ' ') and (board[i][j+3]== 'X'):
				return j+2
			elif (board[i][j]== 'X') and (board[i][j+1]== 'X') and (board[i][j+2]== 'X') and (board[i][j+3]== ' '):
				return j+3
            
             #check for diagonal in the nagtive slope
	for j in range(4):
		for i in range(3, 6):
			if (board[i][j]== ' ') and (board[i-1][j+1]== 'X') and (board[i-2][j+2]== 'X') and (board[i-3][j+3]== 'X'):
				return j
			if (board[i][j]== 'X') and (board[i-1][j+1]== ' ') and (board[i-2][j+2]== 'X') and (board[i-3][j+3]== 'X'):
				return j+1
			if (board[i][j]== 'X') and (board[i-1][j+1]== 'X') and (board[i-2][j+2]== ' ') and (board[i-3][j+3]== 'X'):
				return j+2
			if (board[i][j]== 'X') and (board[i-1][j+1]== 'X') and (board[i-2][j+2]== 'X') and (board[i-3][j+3]== ' '):
				return j+3
            
              #check for diagonal in the positive slope
	for j in range(4):
		for i in range(3):
			if (board[i][j]== ' ') and (board[i+1][j+1]== 'X') and (board[i+2][j+2]== 'X') and (board[i+3][j+3]== 'X'):
				return j
			if (board[i][j]== 'X') and (board[i+1][j+1]== ' ') and (board[i+2][j+2]== 'X') and (board[i+3][j+3]== 'X'):
				return j+1
			if (board[i][j]== 'X') and (board[i+1][j+1]== 'X') and (board[i+2][j+2]== ' ') and (board[i+3][j+3]== 'X'):
				return j+2
			if (board[i][j]== 'X') and (board[i+1][j+1]== 'X') and (board[i+2][j+2]== 'X') and (board[i+3][j+3]== ' '):
				return j+3
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
		value = pcSmart(board)
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
        winner = checkBoard(board)
        if winner == 'X': # let X make the move and see if they won 
            print("You won!")
            break
        elif winner == 'O': # let O make the move and see if they won 
            print("Computer won!")
            break	
        pc_col = pcTurn()
        displayBoard(board)
        undo_func(board, pc_col, user_col)
        winner = checkBoard(board)
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

    
