# Tik tak toe GUI
#
# 6/8/2021
# @author Jack Hangen
# imcomplete
# making a GUI for tiktaktoe using tkinter

# import statments
import tkinter
import random
import time
from tkinter.constants import END

# var
board = [['-','-','-'],['-','-','-'],['-','-','-']]
places = [[1,2,3],[4,5,6],[7,8,9]]
places_set = [[1,2,3],[4,5,6],[7,8,9]]
places2 = [1,2,3,4,5,6,7,8,9]

# create instance
window = tkinter.Tk()
window.title("Tik Tak Toe")

def print_board(board):
  for i in board:
    print(i)

def print_pos(places):
  for i in places:
    print(i)

def print_pos_set(places_set):
  for i in places_set:
    print(i)

def player_move(pos):
  if (pos == 1 or pos == 2 or pos == 3):
    if(board[0][pos - 1] == '-' and places[0][pos - 1] != None):
      places[0][pos - 1] = None
      board[0][pos - 1] = 'O'
      return True
    else:
      print(f"{pos} is not an avaliable possition: ERROR 1")
      return False
  elif (pos == 4 or pos == 5 or pos == 6):
    if(board[1][pos - 4] == '-' and places[1][pos - 4] != None):
      places[1][pos - 4] = None
      board[1][pos - 4] = 'O'
      return True
    else:
      print(f"{pos} is not an avaliable possition: ERROR 1")
      return False
  elif (pos == 7 or pos == 8 or pos == 9):
    if(board[2][pos - 7] == '-' and places[2][pos - 7] != None):
      places[2][pos - 7] = None
      board[2][pos - 7] = 'O'
      return True
    else:
      print(f"{pos} is not an avaliable possition: ERROR 1")
      return False
  else:
    print(f"{pos} is not an avaliable possition: ERROR 2")
    return False

# computer turn
def computer_move():
    pick = random.randrange(1, 9, 1)
    if (pick == 1 or pick == 2 or pick == 3):
      if(places[0][pick - 1] != None):
        places[0][pick - 1] = None
        board[0][pick - 1] = 'X'
        return pick
      else:
        return computer_move()
    elif (pick == 4 or pick == 5 or pick == 6):
      if(places[1][pick - 4] != None):
        places[1][pick - 4] = None
        board[1][pick - 4] = 'X'
        return pick
      else:
        return computer_move()
    elif (pick == 7 or pick == 8 or pick == 9):
      if(places[2][pick - 7] != None):
        places[2][pick - 7] = None
        board[2][pick - 7] = 'X'
        return pick
      else:
        return computer_move()


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

def convert(num):
    if(num == "1"):
        return 1
    elif(num == "2"):
        return 2
    elif(num == "3"):
        return 3
    elif(num == "4"):
        return 4
    elif(num == "5"):
        return 5
    elif(num == "6"):
        return 6
    elif(num == "7"):
        return 7
    elif(num == "8"):
        return 8
    elif(num == "9"):
        return 9
    else:
        print("ERROR: 152")

count1 = 0
count = 0

# click
def click():
    output = num.get()
    num.delete(0, END)
    try:
        # I got lazy sorry :/
        global count
        global count1

        # person part
        game = game_over()
        if (game == False):
            output = convert(output)
            player_move(output)
            placeWigget(output, os[count])
            count = count + 1

        # computer part
        game = game_over()
        if (game == False):
            compMove = computer_move()
            print(compMove)
            placeWigget(compMove, xs[count1])
            count1 = count1 + 1
    except:
        print("ERROR: 168")
        time.sleep(5)
        window.destroy()
        exit()

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
    text="x", 
    font="none 60 bold"
)

x1 = tkinter.Label(
    text="x", 
    font="none 60 bold"
)

x2 = tkinter.Label(
    text="x", 
    font="none 60 bold"
)

x3 = tkinter.Label(
    text="x", 
    font="none 60 bold"
)

x4 = tkinter.Label(
    text="x", 
    font="none 60 bold"
)

o = tkinter.Label(
    text="o",
    font="none 60 bold"
)
o1 = tkinter.Label(
    text="o",
    font="none 60 bold"
)
o2 = tkinter.Label(
    text="o",
    font="none 60 bold"
)
o3 = tkinter.Label(
    text="o",
    font="none 60 bold"
)
o4 = tkinter.Label(
    text="o",
    font="none 60 bold"
)

xs = [x, x1, x2, x3, x4]
os = [o, o1, o2, o3, o4]

# submit button
button = tkinter.Button(
    text="SUBMIT",
    width=6,
    command=click
)

# lists the numbers
num = tkinter.Entry()

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

button.pack()
button.place(
    x = 850,
    y = 550
)

# creation of tiktaktoe funtions

# place X and O funtion
def placeWigget(nums, wigget):
    if(nums == 1):
        wigget.place(
            x = 800,
            y = 100
        )
    elif(nums == 2):
        wigget.place(
            x = 975,
            y = 100
        )
    elif(nums == 3):
        wigget.place(
            x = 1150,
            y = 100
        )
    elif(nums == 4):
        wigget.place(
            x = 775,
            y = 250
        )
    elif(nums == 5):
        wigget.place(
            x = 975,
            y = 250
        )
    elif(nums == 6):
        wigget.place(
            x = 1150,
            y = 250
        )
    elif(nums == 7):
        wigget.place(
            x = 800,
            y = 375
        )
    elif(nums == 8):
        wigget.place(
            x = 975,
            y = 375
        )
    elif(nums == 9):
        wigget.place(
            x = 1150,
            y = 375
        )
    else:
        print("fucking error 348")

window.mainloop()
