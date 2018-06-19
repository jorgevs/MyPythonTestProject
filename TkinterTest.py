from tkinter import *
import tkinter.font

win = Tk()
win.title("Hello world!")
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")


def cmd1():
    print("hello")


def close():
    win.destroy()


button1 = Button(win, text='Turn on', font=myFont, command=cmd1)
button1.grid(row=0, column=0)

exitButton = Button(win, text='Exit', font=myFont, command=close)
exitButton.grid(row=1, column=1)

win.protocol('WM_DELETE_WINDOW', close)

win.mainloop()

