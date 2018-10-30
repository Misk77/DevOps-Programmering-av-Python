import socket
import select

connections = []
buffer = 1024
port = 9876

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servsock.bind(("127.0.0.1", port))
servsock.listen(99)

connections.append(servsock)

print("Chat server has started on port: {}".format(port))

global addr


def broadcast(sock, msg, addr=None):
    for s in connections:
        print(addr)
        if s != sock and s != servsock:
            try:
                s.send("{}: {}".format(addr, msg).encode())
            except:
                s.close()
                connections.remove(s)


while True:
    readsock, writesock, errsock = select.select(connections, [], [])
    for sock in readsock:
        if sock == servsock:
            sockfd, addr = servsock.accept()
            print("Sockfd", sockfd)
            connections.append(sockfd)
            print("Client {} connected".format(addr))
            broadcast(sockfd, "Client {} has connected".format(addr))

        else:
            try:
                data = sock.recv(buffer)
                if data:
                    print(data.decode())
                    sock.send(data)
                    broadcast(sock, data.decode(), addr)
            except:
                broadcast(sock, "Client {} is offline".format(addr))
                print("Client {} is offline".format(addr))
                sock.close()
                connections.remove(sock)
                continue
servsock.close()
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
window.protocol("WM_DELETE_WINDOW    ", onquit)