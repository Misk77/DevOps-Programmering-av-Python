from tkinter import *
import socket
from threading import Thread
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 9876))
window = Tk()

def onquit():
    quit()

def sendmsg(event):
    msg = entryfield.get()
    textbox.insert(END, "You: ")
    entryfield.delete(0, END)
    sock.send(msg.encode())

def receive():
    while True:
        try:
            msg = sock.recv(1024)
            textbox.insert(END, "{}\n".format(msg.decode()))
            textbox.insert(END, "\n")
        except:
            print("Shits dead yo")
            break

textbox = Text(window)

entryfield = Entry(window)
entryfield.bind("<Return>", sendmsg)
textbox.pack()
entryfield.pack(fill=X)
receivethread = Thread(target=receive)
receivethread.start()
window.mainloop()
