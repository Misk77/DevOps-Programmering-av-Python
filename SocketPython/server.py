###############################################   A SIMPLE SERVER  ###############################################
# first create a socket using the the set up the general socket.socket()
# Then call the bind(hostname,port)
# call the accept method of the returned object, THIS method waits until a client connects to the port you specified
# and then return a connection object that represent the connection to the client


# !/usr/bin/python3           # This is server.py file
import socket

# create the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 request
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr=serversocket.accept()
    print("Got connection from %s" %str(addr))
    msg="Thank you for connection"+"\r\n"
    clientsocket.send(msg.encode("ascii"))
    clientsocket.close()

