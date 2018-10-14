""" #############################   sentdex   ###############################
https://www.youtube.com/watch?v=Ccct5D2AyNM&index=40&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M

"""
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


root = Tk()  # root window
app = Window(root)
root.mainloop()
