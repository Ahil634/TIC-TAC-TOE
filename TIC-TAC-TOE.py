# Our board is a 3x3 array of dashes

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board) 

# take player input

def playerInput(board):
    inp = int(input("Enter a number 1-9 correlating to the board:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print("Oops spot is already taken")


# check for win or tie

# switch the player

# check for win or tie again
