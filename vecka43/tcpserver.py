
# tcpserver.py

import socket

host = '127.0.0.1'  # Standard loopback interface adress(localhost)
port = 50000  # Port att lyssna på(använd gärna en port > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)