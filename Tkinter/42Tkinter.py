""" #############################   sentdex   ###############################
https://www.youtube.com/watch?v=a1Y5e-aGPQ4&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=44
"""
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Michels Project')
        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

    def client_exit(self):
        exit()


root = Tk()  # root window
root.geometry("400x300")
app = Window(root)
root.mainloop()