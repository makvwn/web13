board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
def printBoard():
   print(board[0] + '|'+ board[1]+'|'+ board[2])
   print('-----')
   print(board[3] + '|'+board[4]+'|' + board[5])
   print('-----')
   print(board[6] + '|'+board[7]+'|' + board[8])
   return

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def stepBoard(step,symbol):
    board[step - 1] = symbol
 
def getResult():
    win = ""
    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"   
    return win
 
game_over = False
player1 = True
 
while game_over == False:
 
    printBoard()
 
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
 
    stepBoard(step,symbol) 
    win = getResult() 
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
         
printBoard()
print("Победил", win)