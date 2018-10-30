from tkinter import *
from tkinter import messagebox
import threading
import select
import socket
import multiprocessing
from threading import Thread


def server():
    host = '127.0.0.1'  # vilket ip som servern har
    port = 53883  # vilken port som server lyssnar
    backlog = 5  # hur många som är tillåtna , listen, hur många som server "lyssnar" till
    maxsize = 1024  # Max receive buffer size, in bytes, data  mängd som den hanterar
    running = 1  # 1 så är server "vaken" TRUE
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(backlog)
    input = [server, ]
    print("Chat server has started on port: {}".format(port))

    while running:
        inputready, outputready, exceptready = select.select(input, [], [])

        for s in inputready:  # kollar data från socket

            if s == server:  # returnerar client ip vid accept tillåtet

                client, address = server.accept()
                input.append(client)  # lägger till i lista, se ovan innehållet server
                print('new client added%s' % str(address))

            else:
                # tillåtna socket med data maxsize se 1024
                data = s.recv(maxsize)
                if data:
                    print('%s received from %s' % (data, s.getsockname()))  # se data

                    s.send(data)
                else:  # inget mottaget, troligen avsluta
                    s.close()
                    input.remove(s)
    server.close()


def serverUI():
    root = Tk()

    host = '127.0.0.1'  # server ip
    port = 53883  # server port som väntar på connection
    backlog = 5  # listen, antal connect som är tillåten

    label = Label(root, text="Socket successfully created")
    label.pack()

    label = Label(root, text="socket binded to %s" % port)
    label.pack()

    label = Label(root, text="socket is listening")
    label.pack()
    label = Label(root, text="Chat server has started on port: {}".format(port))
    label.pack()

    threading.Thread(target=server).start()
    root.mainloop()


"""
def clientUI():
    
    # kod för gui
    root = Tk()

    HOST = '127.0.0.1'  # ip
    PORT = 53883  # port till server
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


"""


def client_connect():
    """HOST = '127.0.0.1'  # The remote host
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
"""


def socket_connect():
    import socket
    from threading import Thread
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 53883))
    root = Tk()

    def on_closing():
        if messagebox.askokcancel("Quit", "leave the chatt?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

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
                label = Label(root, text="Some problems with recieve data")
                label.pack()
                break

    textbox = Text(root)

    entryfield = Entry(root)
    entryfield.bind("<Return>", sendmsg)
    textbox.pack()
    entryfield.pack(fill=X)
    receivethread = Thread(target=receive)
    receivethread.start()
    root.mainloop()
    root.protocol("WM_DELETE_WINDOW    ", on_closing)


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
