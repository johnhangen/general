# GUI calc
#
# 6/13/2021 -  missed it by 13 mins, i dumb
# @author Jack Hangen
# Complete
# I honestly just dont know how to use the modulus operator, but im emparsed about that, I also cannot spell

from tkinter import *

root = Tk()
root.title("calc")

entry = Entry(root, width=40, borderwidth=5)
entry.grid(column=0, row=0, columnspan=4, padx=10, pady = 10)

Current = ""

def button_num(num):
    global Current
    entry.delete(0, END)
    entry.insert(0, str(Current) + str(num))
    Current = Current + str(num)

def func_equals():
    global func
    global first_num
    global Current

    entry.delete(0, END)

    if (func == "mod"):
        Current = int(first_num) % int(Current)
        entry.insert(0, Current)
        first_num = Current
    elif(func == "add"):
        Current = int(first_num) + int(Current)
        entry.insert(0, str(Current))
        first_num = Current
    elif(func == "sub"):
        Current = int(first_num) - int(Current)
        entry.insert(0, str(Current))
        first_num = Current
    elif(func == "div"):
        Current = int(first_num) / int(Current)
        entry.insert(0, str(Current))
        first_num = Current
    elif(func == "mul"):
        Current = int(first_num) * int(Current)
        entry.insert(0, str(Current))
        first_num = Current
    else:
        print("ERROR: 50")

def func_mod():
    global func
    global first_num
    global Current
    first_num = Current
    Current = ""
    func = "mod"
    entry.delete(0, END)
    entry.insert(0, "%")

def func_add():
    global func
    global first_num
    global Current
    first_num = Current
    Current = ""
    func = "add"
    entry.delete(0, END)
    entry.insert(0, "+")

def func_subtract():
    global func
    global first_num
    global Current
    first_num = Current
    Current = ""
    func = "sub"
    entry.delete(0, END)
    entry.insert(0, "-")

def func_div():
    global func
    global first_num
    global Current
    first_num = Current
    Current = ""
    func = "div"
    entry.delete(0, END)
    entry.insert(0, "/")

def func_mul():
    global func
    global first_num
    global Current
    first_num = Current
    Current = ""
    func = "mul"
    entry.delete(0, END)
    entry.insert(0, "*")

def func_clear():
    global func
    global first_num
    global Current
    first_num = Current
    Current = ""
    Current = ""
    entry.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady = 20, command= lambda: button_num(1)).grid(column = 0, row= 4)
button_2 = Button(root, text="2", padx=40, pady = 20, command= lambda: button_num(2)).grid(column = 1, row= 4)
button_3 = Button(root, text="3", padx=40, pady = 20, command= lambda: button_num(3)).grid(column = 2, row= 4)

button_4 = Button(root, text="4", padx=40, pady = 20, command= lambda: button_num(4)).grid(column = 0, row= 3)
button_5 = Button(root, text="5", padx=40, pady = 20, command= lambda: button_num(5)).grid(column = 1, row= 3)
button_6 = Button(root, text="6", padx=40, pady = 20, command= lambda: button_num(6)).grid(column = 2, row= 3)

button_7 = Button(root, text="7", padx=40, pady = 20, command= lambda: button_num(7)).grid(column = 0, row= 2)
button_8 = Button(root, text="8", padx=40, pady = 20, command= lambda: button_num(8)).grid(column = 1, row= 2)
button_9 = Button(root, text="9", padx=40, pady = 20, command= lambda: button_num(9)).grid(column = 2, row= 2)

button_0 = Button(root, text="0", padx=40, pady = 20, command= lambda: button_num(0)).grid(column = 0, row= 5)

button_mod = Button(root, text="%", padx=38, pady = 20, command= func_mod).grid(column = 0, row= 1)
button_div = Button(root, text="/", padx=40, pady = 20, command= func_div).grid(column = 1, row= 1)
button_mul = Button(root, text="*", padx=40, pady = 20, command= func_mul).grid(column = 2, row= 1)
button_sub = Button(root, text="-", padx=40, pady = 20, command= func_subtract).grid(column = 3, row= 1)

button_plus = Button(root, text="+", padx=40, pady = 52, command= func_add).grid(column = 3, row= 2, rowspan= 2)
button_equals = Button(root, text="=", padx=40, pady = 52, command= func_equals).grid(column = 3, row= 4, rowspan= 2)
button_clear = Button(root, text="clear", padx=78, pady = 20, command= func_clear).grid(column = 1, row= 5, columnspan= 2)

root.mainloop()