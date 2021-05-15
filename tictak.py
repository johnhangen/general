# Tik tak toe
#
# 5/14/2021
# @author Jack Hangen
# Incomplete
# hard coded implimentation of tik tak toe
import random

board = [['-','-','-'],['-','-','-'],['-','-','-']]
places = [[1,2,3],[4,5,6],[7,8,9]]
places_set = [[1,2,3],[4,5,6],[7,8,9]]

def print_board(board):
  for i in board:
    print(i)

def print_pos(places):
  for i in places:
    print(i)

def print_pos_set(places_set):
  for i in places_set:
    print(i)

def player_move():
  print_pos_set(places_set)
  pos = int(input('pick a position: '))
  if (pos == 1 or pos == 2 or pos == 3):
    if(board[0][pos - 1] == '-' and places[0][pos - 1] != None):
      places[0][pos - 1] = None
      board[0][pos - 1] = 'O'
    else:
      print(f"{pos} is not an avaliable possition")
      player_move()
  elif (pos == 4 or pos == 5 or pos == 6):
    if(board[1][pos - 4] == '-' and places[1][pos - 4] != None):
      places[1][pos - 4] = None
      board[1][pos - 4] = 'O'
    else:
      print(f"{pos} is not an avaliable possition")
      player_move()
  elif (pos == 7 or pos == 8 or pos == 9):
    if(board[2][pos - 7] == '-' and places[2][pos - 7] != None):
      places[2][pos - 7] = None
      board[2][pos - 7] = 'O'
    else:
      print(f"{pos} is not an avaliable possition")
      player_move()
  else:
    print(f"{pos} is not an avaliable possition")
    print("error 2")
    player_move()


# somthing is still wrong
def computer_move():
    pick = random.randrange(1, 9, 1)
    if (pick == 1 or pick == 2 or pick == 3):
      if(board[0][pick - 1] == '-' and places[0][pick - 1] != None):
        places[0][pick - 1] = None
        board[0][pick - 1] = 'X'
      else:
        computer_move()
    elif (pick == 4 or pick == 5 or pick == 6):
      if(board[1][pick - 4] == '-' and places[1][pick - 4] != None):
        places[1][pick - 4] = None
        board[1][pick - 4] = 'X'
      else:
        computer_move()
    elif (pick == 7 or pick == 8 or pick == 9):
      if(board[2][pick - 7] == '-' and places[2][pick - 7] != None):
        places[2][pick - 7] = None
        board[2][pick - 7] = 'X'
      else:
        computer_move()



def game_over():
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        print("computer won")
        return True
    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        print("you won!")
        return True
    elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        print("computer won")
        return True
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        print("you won!")
        return True
    elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        print("computer won")
        return True
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        print("you won!")
        return True
    elif (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        print("computer won")
        return True
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        print("you won!")
        return True
    elif (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        print("computer won")
        return True
    elif (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        print("you won!")
        return True
    elif (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        print("computer won")
        return True
    elif (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        print("you won!")
        return True
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        print("computer won")
        return True
    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        print("you won!")
        return True
    elif (places[0][0] == None and places[0][1] == None and places[0][2] == None and places[1][0] == None and places[1][1] == None and places[1][2] == None and places[2][0] == None and places[2][1] == None and places[2][2] == None):
        print("tie")
        return True
    else:
        return False

game_state = game_over()
while(game_state == False):
  player_move()
  if (game_state == True):
      break
  computer_move()
  print("")
  print_board(board)
  print("----------------------")
  game_state = game_over()

print("game over")