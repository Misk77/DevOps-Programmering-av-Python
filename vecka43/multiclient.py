#!/usr/bin/python
import sys
import os
import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = '192.168.1.5'  # socket.gethostbyname(socket.gethostname())  # '192.168.0.19'#socket.gethostbyname(socket.gethostname())  # '127.0.0.1'
port = 53883

# connection to hostname on the port
s.connect((host, port))

# receive no more than 1024 bytes
msg = s.recv(1024)

msg.decode("ascii")

s.close()
