import socket
import selectors


# seb slack

def accept(sock, mask):
    conn, addr = s.accept()
    print(f'Connection accepted {conn} from {addr}')
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


s = socket.socket()
print("Socket successfully created")
sel = selectors.DefaultSelector()

host = socket.gethostname()
port = 53883

s.bind((host, port))
print("socket binded to %s" % port)
s.listen(100)
print("socket is listening")
s.setblocking(False)
sel.register(s, selectors.EVENT_READ, accept)



while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

