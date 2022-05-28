# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:51:52 2019

@author: luisg
"""

#................................. Function definitions ..................................

def diesPlayBoard(gameBoard):
    
    for i in range(len(gameBoard)):
        print(".............................................")
        print("|", end= "")
        for j in range(len(gameBoard[i])):
            
            print(gameBoard[i][j], end=" ")
            
        print("")
    print(".............................................")
        






















#................................. Main Program ..................................
broad = [["", "", "",], ["", "", "",], ["", "", "",]]

diesPlayBoard(broad)



