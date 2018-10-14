#!/usr/bin/env python3
import socket
import tkinter

def receive():
    """Handle receiving of message"""
    while True:
        try:
            msg = client_socket.socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # possible client has left the chat
            break
    # loop infinity for able to send chatt,msg thenever


def send(event=None):  # event is passed by binders
    """Handles sending of message"""
    msg = my_msg.get()
    my_msg.set("")  # clear input field
    client_socket.send(bytes(msg, ("utf8")))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


# event kmr från Tkinter then the send button is pressed
# my-msg is the input field gui then clear the field and sending the msg to server

def on_closing(event=None):
    """This function is t0 be called then the windows closed"""
    my_msg.set("{quit}")
    send()



"""Script for Tkinter GUI chat client."""
from socket import AF_INET, SOCK_STREAM
from threading import Thread
import tkinter

top = tkinter.Tk()
top.title("Chatter")
message_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # for the message to be sent
my_msg.set("Type your messge here")
scrollbar = tkinter.Scrollbar(message_frame)  # to navigate through past msg

msg_list = tkinter.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

message_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.BOTTOM(top, text="Send", command=send())
send_button.pack()

top.protocol("Wm_DELETE_WINDOWS", on_closing())

HOST = input("Enter host: ")
PORT = input("Enter port: ")
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # start gui