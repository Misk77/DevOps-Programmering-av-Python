import random
from tkinter import *

displaytext = """|===========================================|
|------- Rolling the dice   -------|
|===========================================|"""


def dice():
    try:
        for i in range(1, 6):
            prick = random.randrange(1, 7)
            Label(text='Tärning ' + str(i) + ' visar ' + str(prick) + ' prickar').pack()
    except:
        Label(text="FEL")


root = Tk()
root.geometry("300x400")
labelett = Label(root, text=displaytext)
labelett.pack()

button2 = Button(root, text="Roll the dices", command=dice)
button2.pack()

root.mainloop()
