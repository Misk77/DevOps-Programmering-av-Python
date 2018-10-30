"""
https://www.youtube.com/watch?v=W5ZhoxtsfGA&list=PLlEgNdBJEO-komysN9pCz1WONDIjk-U4F

https://www.youtube.com/watch?v=W5ZhoxtsfGA

Python Guessing Game (GUI Version) Tutorial Pt. 1

"""

# funtion for the game
import random
from tkinter import *

computer_guess = random.randint(1, 10)


def check():
    try:
        # Get the value
        user_guess = int(text_guess.get())
        # Deteminte higher or lower
        if user_guess < computer_guess:
            msg = "Higher!"
        elif user_guess > computer_guess:
            msg = "Lower"
        elif user_guess == computer_guess:
            msg = "Correct!"
        else:
            msg = "Something went wrong"
    except:
        msg = "Must be an interger"
        # show the result
    labl_result["text"] = msg
    # clear guess
    text_guess.delete(0, 5)
    return


def reset():
    # Declare the global variable
    global computer_guess
    # Get a random number
    computer_guess = random.randint(1, 10)
    # Change the labl_result text
    labl_result["text"] = "Game reset, Guess again"


# Tkinter GUI window

# Create root window
root = Tk()
root.config(bg="black")
root.title("Guess the number")
# Create widget
lbl_title = Label(root, text="Welcom to my gueesing game", bg="white")
lbl_title.pack()

labl_result = Label(root, text="GOOD LUCK!", bg="green")
labl_result.pack()

btn_check = Button(root, text="Check", fg="green", command=check, bg="white")
btn_check.pack(side=LEFT)

btn_reset = Button(root, text="Reset", fg="red", command=reset, bg="white")
btn_reset.pack(side=RIGHT)

btn_quit = Button(root, text="QUIT", fg="black", command=quit, bg="white")
btn_quit.pack(side=BOTTOM)

text_guess = Entry(root, width=3)
text_guess.pack()

# start the main events loop
root.mainloop()
