from tkinter import *
import threading
import select
import socket
import multiprocessing
from threading import Thread


def server():
    host = '127.0.0.1'  # what address is the server listening on
    port = 53883  # what port the server accepts connections on
    backlog = 5  # how many connections to accept
    maxsize = 1024  # Max receive buffer size, in bytes, per recv() call
    running = 1  # set running to zero to close the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(backlog)
    input = [server, ]

    while running:
        inputready, outputready, exceptready = select.select(input, [], [])

        for s in inputready:  # check each socket that select() said has available data

            if s == server:  # if select returns our server socket, there is a new
                # remote socket trying to connect
                client, address = server.accept()
                input.append(client)  # add it to the socket list so we can check it now
                print('new client added%s' % str(address))

            else:
                # select has indicated that these sockets have data available to recv
                data = s.recv(maxsize)
                if data:
                    print('%s received from %s' % (data, s.getsockname()))

                    # Uncomment below to echo the recv'd data back
                    # to the sender... loopback!
                    # s.send(data)
                else:  # if recv() returned NULL, that usually means the sender wants
                    # to close the socket.
                    s.close()
                    input.remove(s)
    server.close()


def serverUI():
    root = Tk()

    # now initialize the server and accept connections at localhost:50000
    host = '127.0.0.1'  # what address is the server listening on
    port = 53883  # what port the server accepts connections on
    backlog = 5  # how many connections to accept

    label = Label(root, text="Socket successfully created")
    label.pack()

    label = Label(root, text="socket binded to %s" % port)
    label.pack()

    label = Label(root, text="socket is listening")
    label.pack()
    # a list of all connections we want to check for data
    # each time we call select.select()

    # if running is ever set to zero, we will call this
    threading.Thread(target=server).start()
    root.mainloop()


def clientUI():
    # kod för gui
    root = Tk()

    HOST = '127.0.0.1'  # The remote host
    PORT = 53883  # The same port as used by the server
    s = None
    if s is None:
        label = Label(root, text='could not open socket')
        label.pack()
        sys.exit(1)
    with s:
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    label = Label(root, text='Received' + repr(data))
    label.pack()

    threading.Thread(target=client_connect).start()
    root.mainloop()


def client_connect():
    HOST = '127.0.0.1'  # The remote host
    PORT = 53883  # The same port as used by the server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        sys.exit(1)
    with s:
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    # kod för client socket


def socket_connect():
    root = Tk()
    # Echo client program

    HOST = '127.0.0.1'  # The remote host
    PORT = 53883  # The same port as used by the server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        label = Label(root, text='could not open socket')
        label.pack()
        sys.exit(1)
    with s:
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    label = Label(root, text='Received' + repr(data))
    label.pack()
    root.mainloop()


"""
def run(self):
    for _ in range(10):
        print(threading.current_thread().getName())


x = socket_connect(socket_connect)
y = server(server)
x.start()
y.start()
     
     # threading: 
    
def start():
    threading.Thread(target=server).start()
    start()
     
"""


