# Tik tak toe GUI
#
# 6/8/2021
# @author Jack Hangen
# imcomplete
# making a GUI for tiktaktoe using tkinter

# import statments
from tkinter import *
from tkinter import filedialog

def openFile(num):
    if(num == 1):
        global firstFile
        root.filename = filedialog.askopenfilename( initialdir = "/", title = "Select a dataset", filetypes=(("ALL files","*.*"),("HTML files","*.html"),("XLS files","*.xls"),("JSON files","*.json"),("CSV files","*.csv")))
        firstFile = root.filename
        table1Entry.insert(0, firstFile)
        print(firstFile)
    elif(num == 2):
        global secondFile
        root.filename = filedialog.askopenfilename( initialdir = "/", title = "Select a dataset", filetypes=(("ALL files","*.*"),("HTML files","*.html"),("XLS files","*.xls"),("JSON files","*.json"),("CSV files","*.csv")))
        secondFile = root.filename
        table2Entry.insert(0, secondFile)
        print(secondFile)
    else:
        errorMessage1 = Label(root, text="ERROR: 17")
        errorMessage1.grid(column=2, row=2)

root = Tk()
root.title("Data Set tool")

title = Label(root, text="Enter in the box the path of the file or open the file explorer")
title.grid(column=2, row=1)

table1Label = Label(root, text="Table 1")
table1Label.grid(column=2, row=3)

table1FileExplore = Button(root, text="Open file explorer", padx=20, pady = 10, command= lambda: openFile(1))
table1FileExplore.grid(column=2, row=4)

table1Entry = Entry(root, borderwidth= 5)
table1Entry.grid(column=3, row=3)

space = Label(root, text="                     ")
space.grid(column=1, row=5)

table2Label = Label(root, text="Table 2")
table2Label.grid(column=2, row=6)

table2FileExplore = Button(root, text="Open file explorer", padx=20, pady = 10, command= lambda: openFile(2))
table2FileExplore.grid(column=2, row=7)

table2Entry = Entry(root, borderwidth= 5)
table2Entry.grid(column=3, row=6)

root.mainloop()