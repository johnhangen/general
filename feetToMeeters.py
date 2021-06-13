# GUI to convert Meters to feet
#
# 6/12/2021
# @author Jack Hangen
# imcomplete
# GUI using tkinter trying to make this in 16 mins

from tkinter import *

root = Tk()
root.title("Convsions")

def convert():
    given_foot = int(feet.get())
    meter.insert(0, given_foot *0.3048)

feet = Entry(root, width=10, borderwidth=5)
feet.grid(row=0, column=1)

feet_label = Label(root, text= "Enter feet")
feet_label.grid(row=0, column=0)

meter = Entry(root, width= 10, borderwidth=5)
meter.grid(row=1, column=1)

convert_label = Label(root, text= "Converts to ")
convert_label.grid(row=1,column=0)

meter_label = Label(root, text= "meters")
meter_label.grid(row=1,column=2)

button = Button(root, text= "Convert", command=convert)
button.grid(row = 2, column=0)

root.mainloop()
