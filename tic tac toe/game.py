import random
board = {1: '1', 2: "2", 3: "3",
         4: "4", 5: "5", 6: "6",
         7: "7", 8: "8", 9: "9"}

def printBoard(board):
    print('\n')
    print(board[1] + '   |   ' +board[2] + '   |   ' + board[3])
    print('\n')    
    print(board[4] + '   |   ' + board[5] + '   |   ' + board[6])
    print('\n')    
    print(board[7] + '   |   ' + board[8] + '   |   ' + board[9])
    print('\n')
    



def setplayer():
  symboles = ['X' ,'O']

  player1 = random.choice(symboles)
  player2 = random.choice(symboles)
    
  if player1 == player2 == 'X' :
      player2 = 'O'
  elif player1 == player2 == 'O':    
      player2 ='X'
  print(f'player1 : {player1} \nplayer2 : {player2} ')
  return player1 , player2
  

  


def playerInput(board , player):
    inp = int(input("Please Enter a number between 1,9 represents an empty position "))
    if board[inp] == str(inp):      
      board[inp] = player
    else:
        print("Oops player is already at that spot.")

def check_full_board(board) :
      for key in board.keys():
        if board[key] == '1' or '2' or '3' or '4' or '5' or '6'or'7'or'8'or'9':
            return False 
      return True 


def checkWin(board , player):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == player ):
        return True
    elif (board[4] == board[5] and board[4] == board[6]  and board[4] == player  ):
        return True
    elif (board[7] == board[8] and board[7] == board[9]  and board[7] == player ):
        return True
    elif (board[1] == board[4] and board[1] == board[7]  and board[1] == player ):
        return True
    elif (board[2] == board[5] and board[2] == board[8]  and board[2] == player ):
        return True
    elif (board[3] == board[6] and board[3] == board[9]  and board[3] == player ):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == player ):
        return True
    elif (board[7] == board[5] and board[7] == board[3]  and board[7] == player ):
        return True
    else:
        return False

def play () :
  
  player1 , player2 = setplayer()
  while check_full_board(board) != True :  
    print('playerOne turn') 
    printBoard(board)   
    playerInput(board , player1)
    if checkWin(board,player1) == True :
      print('player one win')
      break
    printBoard(board)
    print('playerTwo turn')
    playerInput(board , player2)
    if checkWin(board,player2) == True :
      print('player Two win')
      break
  print("Game Finished. Draw!")
    
    



play()