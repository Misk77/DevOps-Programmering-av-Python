import socket

# server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4444
host = '127.0.0.1'
server.bind((port, host))
server.listen(3)
