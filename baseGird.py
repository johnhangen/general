# Grid GUI
#
# 6/18/2021
# @author Jack Hangen
# Complete
# Create a dynamic way to make a gird

# Imports
from tkinter import *


x = int(input("Size x: "))
y = int(input("Size y: "))
 
class Table:
    def __init__(self,root, total_rows, total_columns):
 
        # code for creating table
        for i in range(1, total_rows, 1):
            for j in range(0, total_columns, 1):
                name = (f"{i} {j}")
                self.e = Button(root, text=name, padx=10, pady = 5)
 
                self.e.grid(row=i, column=j)
 
# take the data
grid = []

temp = ['x' for i in range(y)]

for i in range(x):
    grid.append(temp)
 
# find total number of rows and
# columns in list
total_rows = len(grid)
total_columns = len(grid[0])
 
# create root window S
root = Tk()
root.title("Grid test")
root.iconbitmap(r"C:\Users\12034\Desktop\Summer_2021\other\favicon.ico")
title = Label(root, text="placeholder")
title.grid(row=0, column=0)

##root.attributes("-fullscreen",True)
 
t = Table(root, total_rows, total_columns)
root.mainloop()