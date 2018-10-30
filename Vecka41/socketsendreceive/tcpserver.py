import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)


while True:
    inp=input()
    if inp != '{quit}':
        clientsocket, addr = serversocket.accept()
        print('Connection made by %s' % str(addr))
        msg = 'Thx for HALLÅÅÅÅ DÄÄR' + '\n'
        inp=input('msg: ' )
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()
    elif inp == '{quit}':
        print('bye')
        break
