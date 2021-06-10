# Tik tak toe GUI
#
# 6/8/2021
# @author Jack Hangen
# imcomplete
# making a GUI for tiktaktoe using tkinter

# import statments
import tkinter
import random

# var
board = [['-','-','-'],['-','-','-'],['-','-','-']]
places = [[1,2,3],[4,5,6],[7,8,9]]
places_set = [[1,2,3],[4,5,6],[7,8,9]]
places2 = [1,2,3,4,5,6,7,8,9]

# creation of tiktaktoe funtions
def player_move(pos):
  if (pos == 1 or pos == 2 or pos == 3):
    if(board[0][pos - 1] == '-' and places[0][pos - 1] != None):
      places[0][pos - 1] = None
      board[0][pos - 1] = 'O'
      return True
    else:
      print(f"{pos} is not an avaliable possition")
      return False
  elif (pos == 4 or pos == 5 or pos == 6):
    if(board[1][pos - 4] == '-' and places[1][pos - 4] != None):
      places[1][pos - 4] = None
      board[1][pos - 4] = 'O'
      return True
    else:
      print(f"{pos} is not an avaliable possition")
      return False
  elif (pos == 7 or pos == 8 or pos == 9):
    if(board[2][pos - 7] == '-' and places[2][pos - 7] != None):
      places[2][pos - 7] = None
      board[2][pos - 7] = 'O'
      return True
    else:
      print(f"{pos} is not an avaliable possition")
      return False
  else:
    print(f"{pos} is not an avaliable possition")
    return False

# computer turn
def computer_move():
    pick = random.randrange(1, 9, 1)
    if (pick == 1 or pick == 2 or pick == 3):
      if(board[0][pick - 1] == '-' and places[0][pick - 1] != None):
        places[0][pick - 1] = None
        board[0][pick - 1] = 'X'
        return pick
      else:
        computer_move()
    elif (pick == 4 or pick == 5 or pick == 6):
      if(board[1][pick - 4] == '-' and places[1][pick - 4] != None):
        places[1][pick - 4] = None
        board[1][pick - 4] = 'X'
        return pick
      else:
        computer_move()
    elif (pick == 7 or pick == 8 or pick == 9):
      if(board[2][pick - 7] == '-' and places[2][pick - 7] != None):
        places[2][pick - 7] = None
        board[2][pick - 7] = 'X'
        return pick
      else:
        computer_move()


# game over funtion: tells if the game is over
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

# create instance
window = tkinter.Tk()

# create wiggets

# makes the four lines
line_one = tkinter.Label(
    bg="black",
    fg="black",
    width=1,
    height=30
)

line_two = tkinter.Label(
    bg="black",
    fg="black",
    width=1,
    height=30
)

line_three = tkinter.Label(
    bg="black",
    fg="black",
    width=70,
    height=1
)

line_four = tkinter.Label(
    bg="black",
    fg="black",
    width=70,
    height=1
)

title = tkinter.Label(
    text="enter a number 1-9"
)

# for x and o
x = tkinter.Label(
    text="x"
)

o = tkinter.Label(
    text="o"
)

num = tkinter.Listbox()
num.insert(1, "1")
num.insert(2, "2")
num.insert(3, "3")
num.insert(4, "4")
num.insert(5, "5")
num.insert(6, "6")
num.insert(7, "7")
num.insert(8, "8")
num.insert(9, "9")

# place x funtion
def placeX(nums):
    if(nums == 1):
        x.place(
            x = 800,
            y = 100
        )
    elif(nums == 2):
        x.place(
            x = 1000,
            y = 100
        )
    elif(nums == 3):
        x.place(
            x = 1200,
            y = 100
        )
    elif(nums == 4):
        x.place(
            x = 800,
            y = 275
        )
    elif(nums == 5):
        x.place(
            x = 1000,
            y = 275
        )
    elif(nums == 6):
        x.place(
            x = 1200,
            y = 275
        )
    elif(nums == 7):
        x.place(
            x = 800,
            y = 450
        )
    elif(nums == 8):
        x.place(
            x = 1000,
            y = 450
        )
    elif(nums == 9):
        x.place(
            x = 1200,
            y = 450
        )
    else:
        print("fucking error")

# place 0 funtion
def placeO(nums):
    if(nums == 1):
        o.place(
            x = 800,
            y = 100
        )
    elif(nums == 2):
        o.place(
            x = 1000,
            y = 100
        )
    elif(nums == 3):
        o.place(
            x = 1200,
            y = 100
        )
    elif(nums == 4):
        o.place(
            x = 800,
            y = 275
        )
    elif(nums == 5):
        o.place(
            x = 1000,
            y = 275
        )
    elif(nums == 6):
        o.place(
            x = 1200,
            y = 275
        )
    elif(nums == 7):
        o.place(
            x = 800,
            y = 450
        )
    elif(nums == 8):
        o.place(
            x = 1000,
            y = 450
        )
    elif(nums == 9):
        o.place(
            x = 1200,
            y = 450
        )
    else:
        print("fucking error")

# place afformentioned wiggets
line_one.pack()
line_one.place(
    x = 1100,
    y = 50
)

line_two.pack()
line_two.place(
    x = 900,
    y = 50
)

line_three.pack()
line_three.place(
    x = 750,
    y = 200
)

line_four.pack()
line_four.place(
    x = 750,
    y = 350
)

num.pack()
num.place(
    x = 1000,
    y = 500
)

title.pack()
title.place(
    x = 850,
    y = 500
)


game_state = game_over()
keep = False
# main loops
while(game_state == False):
    while(keep == False):
        print("got here")
        nums = num.get(first= 0)
        print(nums)
        if(nums in places2):
            keep = True
    keep = False
    nums = player_move(nums)
    placeX(nums)
    if (game_state == True):
        break
    nums = computer_move()
    placeO(nums)
    game_state = game_over()

window.mainloop()
