# merge GUI tool
#
# 6/15/2021
# @author Jack Hangen
# Compete
# Making a GUI to merge two data sets

# import statments
from tkinter import *
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox

firstFile = ""
secondFile = ""

def popup(errorTitle, errorMessage):
    messagebox.showwarning(errorTitle, errorMessage)

def openFile(num):
    if(num == 1):
        global firstFile
        root.filename = filedialog.askopenfilename( initialdir = "/", title = "Select a dataset", filetypes=(("ALL files","*.*"),("XLSX file", "*.xlsx"),("HTML files","*.html"),("XLS files","*.xls"),("JSON files","*.json"),("CSV files","*.csv")))
        firstFile = root.filename
        table1Entry.insert(0, firstFile)
        print(firstFile)
    elif(num == 2):
        global secondFile
        root.filename = filedialog.askopenfilename( initialdir = "/", title = "Select a dataset", filetypes=(("ALL files","*.*"),("XLSX file", "*.xlsx"),("HTML files","*.html"),("XLS files","*.xls"),("JSON files","*.json"),("CSV files","*.csv")))
        secondFile = root.filename
        table2Entry.insert(0, secondFile)
        print(secondFile)

def saveFile():
        global saveLocation
        root.filename = filedialog.asksaveasfilename( initialdir = "/", title = "Where to save joined data set", filetypes=(("ALL files","*.*"),("XLSX file", "*.xlsx"),("XLS files","*.xls")))
        saveLocation = root.filename
        saveLabelEntry.insert(0, firstFile)
        print(saveLocation)

def combine():
    selection = str(var.get())
    if (selection == "Left join"):
        print("Left join")

        if (firstFile == ""):
            popup("ERROR code: 47", "File 1 is empty")
            return

        if (secondFile == ""):
            popup("ERROR code: 51", "File 1 is empty")
            return

        try:
            try:
                if firstFile.endswith(".xlsx"):
                    file1 = pd.read_excel(firstFile)
                elif firstFile.endswith('.html'):
                    file1 = pd.read_html(firstFile)
                elif firstFile.endswith('.xls'):
                    file1 = pd.read_excel(firstFile)
                elif firstFile.endswith('.json'):
                    file1 = pd.read_json(firstFile)
                elif firstFile.endswith('.csv'):
                    file1 = pd.read_csv(firstFile)
            except:
                popup("ERROR code: 67", "Unsuported file type for file 1")
            
            try:
                if firstFile.endswith('.xlsx'):
                    file2 = pd.read_excel(firstFile)
                elif firstFile.endswith('.html'):
                    file2 = pd.read_html(firstFile)
                elif firstFile.endswith('.xls'):
                    file2 = pd.read_excel(firstFile)
                elif firstFile.endswith('.json'):
                    file2 = pd.read_json(firstFile)
                elif firstFile.endswith('.csv'):
                    file2 = pd.read_csv(firstFile)
            except:
                popup("ERROR code: 80", "Unsuported file type for file 2")

            pd.merge(file2, file1)

            try:
                if saveFile.endswith('.xlsx') or saveFile.endswith('.xls'):
                    pd.ExcelWriter(saveLocation)
            except:
                popup("ERROR code: 89", "error saving file")               
        except:
            popup("ERROR code: 81", "x0000")
           
    elif (selection == "Right join"):
        print("Left join")

        if (firstFile == ""):
            popup("ERROR code: 97", "File 1 is empty")
            return

        if (secondFile == ""):
            popup("ERROR code: 101", "File 1 is empty")
            return

        try:
            try:
                if firstFile.endswith('.xlsx'):
                    file1 = pd.read_excel(firstFile)
                elif firstFile.endswith('.html'):
                    file1 = pd.read_html(firstFile)
                elif firstFile.endswith('.xls'):
                    file1 = pd.read_excel(firstFile)
                elif firstFile.endswith('.json'):
                    file1 = pd.read_json(firstFile)
                elif firstFile.endswith('.csv'):
                    file1 = pd.read_csv(firstFile)
            except:
                popup("ERROR code: 117", "Unsuported file type for file 1")
            
            try:
                if firstFile.endswith('.xlsx'):
                    file2 = pd.read_excel(firstFile)
                elif firstFile.endswith('.html'):
                    file2 = pd.read_html(firstFile)
                elif firstFile.endswith('.xls'):
                    file2 = pd.read_excel(firstFile)
                elif firstFile.endswith('.json'):
                    file2 = pd.read_json(firstFile)
                elif firstFile.endswith('.csv'):
                    file2 = pd.read_csv(firstFile)
            except:
                popup("ERROR code: 131", "Unsuported file type for file 2")

            pd.merge(file1, file2)

            try:
                if saveFile.endswith('.xlsx') or saveFile.endswith('.xls'):
                    pd.ExcelWriter(saveLocation)
            except:
                popup("ERROR code: 139", "error saving file")               
        except:
            popup("ERROR code: 141", "x0000")

root = Tk()
root.title("Data Set tool")
root.iconbitmap(r"C:\Users\12034\Desktop\Summer_2021\other\favicon.ico")

title = Label(root, text="Enter in the box the path of the file or open the file explorer")
title.grid(column=1, row=1, columnspan=2)

space1 = Label(root, text="                     ")
space1.grid(column=1, row=2)

table1Label = Label(root, text="Select Table 1")
table1Label.grid(column=2, row=3)

table1FileExplore = Button(root, text="Open file explorer", padx=20, pady = 10, command= lambda: openFile(1))
table1FileExplore.grid(column=2, row=4)

table1Entry = Entry(root, borderwidth= 5)
table1Entry.grid(column=3, row=3)

space = Label(root, text="                     ")
space.grid(column=1, row=5)

table2Label = Label(root, text="Select Table 2")
table2Label.grid(column=2, row=6)

table2FileExplore = Button(root, text="Open file explorer", padx=20, pady = 10, command= lambda: openFile(2))
table2FileExplore.grid(column=2, row=7)

table2Entry = Entry(root, borderwidth= 5)
table2Entry.grid(column=3, row=6)

space = Label(root, text="                     ")
space.grid(column=1, row=8)

var = StringVar()
var.set("Right join")

title1 = Label(root, text="Select the type of join")
title1.grid(column=1, row=9)

var1 = Radiobutton(root, text="Right join", variable=var, value="Right join")
var1.grid(column=2, row=10)

var2 = Radiobutton(root, text="Left join", variable=var, value="Left join")
var2.grid(column=2, row=11)

space3 = Label(root, text="Select the save Location")
space3.grid(column=1, row=12)

saveLabel = Label(root, text="Save location")
saveLabel.grid(column=2, row=13)

saveLabelFileExplore = Button(root, text="Open file explorer", padx=20, pady = 10, command= saveFile)
saveLabelFileExplore.grid(column=2, row=14)

saveLabelEntry = Entry(root, borderwidth= 5)
saveLabelEntry.grid(column=3, row=13)

runCombine = Button(root, text="Combine", command=combine)
runCombine.grid(column=3, row=15)

root.mainloop()