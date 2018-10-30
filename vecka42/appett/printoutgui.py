from tkinter import *
import mysql
import mysql.connector
from mysql.connector import errorcode


def printSomething():
    root = Tk()
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    for x in range(9):  # 0 is unnecessary
        label = Label(root, text=str(x))
        # this creates x as a new label to the GUI
        label.pack()
    root.mainloop()
