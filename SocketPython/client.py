###############################################   A SIMPLE CLIENT  ###############################################
# write a simple client program wich open a conneection at given port 12345 and given host
# Once you have the socket open you can read from it like any I/O object
# remember to close then you done, as you would close a file
### Following code is a very simple client that connect to given host and port
# reads any available data from the socket and the exits


# !/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connection to hostname on the port
s.connect((host, port))

# receive no more than 1024 bytes
msg=s.recv(1024)

s.close()
print(msg.decode("ascii"))
