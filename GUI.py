import tkinter

window = tkinter.Tk()

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

num = tkinter.Entry()

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

window.mainloop()
