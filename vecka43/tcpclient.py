# tcpclient.py

import socket

host = '127.0.0.1'  # Servern hostnamn or IP adress
port = 53883  # Port som används av servern

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))  # Accepterar en tuple
    s.sendall(b'Hello, world')  # Omvandlar sträng till byte code
    data = s.recv(1024)  # Tar emot data från servern

print('Received', repr(data.decode('utf-8')))
