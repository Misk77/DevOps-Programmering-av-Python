""" #############################   sentdex   ###############################
https://www.youtube.com/watch?v=Ccct5D2AyNM&index=40&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M

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
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()


root = Tk()  # root window
root.geometry("400x300")
app = Window(root)
root.mainloop()
