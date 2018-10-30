import socket
import selectors


def server():
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

    host = socket.gethostbyname(socket.gethostname())  # '127.0.0.1'
    port = 53883

    s.bind(('', port))
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


def socket_connect():
    import socket

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostbyname(
        socket.gethostname())  # '192.168.0.19'#socket.gethostbyname(socket.gethostname())  # '127.0.0.1'
    port = 53883

    # connection to hostname on the port
    s.connect((host, port))

    # receive no more than 1024 bytes
    msg = s.recv(1024)

    s.close()
    print(msg.decode("ascii"))


"""
def run(self):
    for _ in range(10):
        print(threading.current_thread().getName())


x = socket_connect(socket_connect)
y = server(server)
x.start()
y.start()
     
"""
