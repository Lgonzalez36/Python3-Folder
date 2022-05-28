# Prof. Kim
# TicTacToe
# 10/7/2019

# ---------- function definition ---------------------

def displayBoard(gameBoard):
    # gameBoard is a 2d list (size: 3x3)
    for i in range(len(gameBoard)): # for each row
        print("-------")
        print("|",end='')
        for j in range(len(gameBoard[0])): #each col, w/in a row
            print(gameBoard[i][j],end='|')
        print("")   
    print("-------")


def checkBoard(gameBoard):
    # win condition check for tic tac toe (3x3)
    # returns True if there is a win
    # returns False otherwise
    
    #check rows
    if (gameBoard[0][0]==gameBoard[0][1] and 
        gameBoard[0][0]==gameBoard[0][2] and 
        gameBoard[0][0]!=' '):
        return True
    elif (gameBoard[1][0]==gameBoard[1][1] and 
          gameBoard[1][0]==gameBoard[1][2] and 
          gameBoard[1][0]!=' '):
        return True
    elif (gameBoard[2][0]==gameBoard[2][1] and 
          gameBoard[2][0]==gameBoard[2][2] and 
          gameBoard[2][0]!=' '):
        return True

    #check cols
    for i in range(3):
        if (gameBoard[0][i]==gameBoard[1][i] and 
            gameBoard[0][i]==gameBoard[2][i] and 
            gameBoard[0][i]!=' '):
            return True
        
    #check colums
    if (gameBoard[0][0]==gameBoard[1][1] and 
        gameBoard[0][0]==gameBoard[2][2] and 
        gameBoard[0][0]!=' '):
        return True    
    elif (gameBoard[0][2]==gameBoard[1][1] and 
          gameBoard[0][2]==gameBoard[2][0] and 
          gameBoard[0][2]!=' '):
        return True

    return False    
    


# main program

board = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
displayBoard (board)
cnt = 0

while(True):
    row=int(input("O: enter row#:"))
    col=int(input("O: enter col#:"))
        
    #make sure the chosen spot is empty
    while (board[row][col] != ' '): 
        row=int(input("O: enter row#:"))
        col=int(input("O: enter col#:"))                 
    
    board[row][col] = 'O'    
    displayBoard (board)
    if (checkBoard(board)==True):
        print ("O wins!")
        break
    cnt = cnt + 1    

    if (cnt==9): #check to see if there is a tie at the end
        print("Tie!")
        break
    
    row=int(input("X: enter row#:"))
    col=int(input("X: enter col#:"))
    #make sure the chosen spot is empty
    while (board[row][col] != ' '): 
        row=int(input("X: enter row#:"))
        col=int(input("X: enter col#:"))

    board[row][col] = 'X'
    displayBoard (board)
    if (checkBoard(board)):
        print ("X wins!")
        break
    cnt = cnt + 1    



