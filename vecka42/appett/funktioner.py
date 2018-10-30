"""
Funktioner som är bra att använda i olika program

"""
from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel("Quit", "You wanna leave this program"):
        quit()


"""

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
"""
