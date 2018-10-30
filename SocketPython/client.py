###############################################   A SIMPLE CLIENT  ###############################################
# write a simple client program wich open a conneection at given port 12345 and given host
# Once you have the socket open you can read from it like any I/O object
# remember to close then you done, as you would close a file
### Following code is a very simple client that connect to given host and port
# reads any available data from the socket and the exits


############  FUNKTIONER   ###############
################################################################################################

# !/usr/bin/python3           # This is server.py file
from tkinter import *
import socket


def socket_server():
    # !/usr/bin/python3           # This is server.py file
    import socket

    # create the socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = '127.0.0.1'
    port = 53883

    # bind to the port
    serversocket.bind((host, port))

    # queue up to 5 request
    serversocket.listen(5)

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()
        print("Got connection from %s" % str(addr))
        msg = "Thank you for connection" + "\r\n"
        clientsocket.send(msg.encode("ascii"))
        clientsocket.close()

    ##############################################################################


# !/usr/bin/python3           # This is client.py file
from tkinter import *
import socket


def socket_connect():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()
    port = 9999

    # connection to hostname on the port
    s.connect((host, port))

    # receive no more than 1024 bytes
    msg = s.recv(1024)

    s.close()
    print(msg.decode("ascii"))


###########################################


def disconnect():
    root.destroy()
    exit()


##############################################

###########  TK STUFF

root = Tk()

# Button CLIENT
buttonClient = Button(text="Client SOCKET", bg="black", fg="blue", command=socket_connect)
buttonClient.pack(side=LEFT)

# Button SERVER
buttonServer = Button(text="Socket Server", bg="black", fg="blue", command=socket_server)
buttonServer.pack(side=LEFT)

# Button Disconnect
disconnect = Button(text="Disconnect ", bg="black", fg="green", command=disconnect)
disconnect.pack(side=LEFT)

root.mainloop()
