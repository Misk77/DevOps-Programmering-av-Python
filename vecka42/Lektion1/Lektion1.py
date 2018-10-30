from tkinter import *
from Lektion1.exitscript import goodbye



# connector - connect.py
def sqlconnector():
    __author__ = 'MichelSkoglund'

    import mysql.connector
    from mysql.connector import errorcode

    try:
        connect = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='person')
        print(2 * '\n', "Det Funkar!! Du har lyckats att koppla Dig till Din databas!", 2 * '\n')

    except mysql.connector.Error as e:

        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(2 * '\n', "Kopplingen fungerar inte!", 2 * '\n')

        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print(2 * '\n', "Databas namn hittades inte!!", 2 * '\n')

        else:
            print(e)

    # --------------------------------------------------------------

    # SQl insert -  insert.py

    import mysql.connector

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='person',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' INSERT INTO person                                                                                                                                                               
                                  (name) VALUES ('Michel skoglund') '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        print("Namn lagrats i person tabellen")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Lagring misslyckades {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")

"""

######################   EXIT FUNKTION
def goodbye():
    root.destroy()
    exit()
"""

###########################    SERVER FUNKTION

# !/usr/bin/python3           # This is server.py file
import socket


def server():
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
        clientsocket, addr = serversocket.accept()
        print("Got connection from %s" % str(addr))
        msg = "Thank you for connection" + "\r\n"
        clientsocket.send(msg.encode("ascii"))
        clientsocket.close()


##############################################################################


# !/usr/bin/python3           # This is client.py file


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


###########################################   TKINTER SETTING  ###########################
###########################################   TKINTER SETTING  ###########################
###########################################   TKINTER SETTING  ###########################


root = Tk()
root.configure(background="grey")
root.title("Michels menu med saker")
root.geometry("600x400")

# MIN LABEL
labelett = Label(root, text="Menu av massa saker", bg="black", fg="red")
labelett.grid(column=0, row=0)

# Button  SERVER
buttonServer = Button(text="SERVER socket", bg="black", fg="green", command=server)
buttonServer.grid(column=1, row=1)

# Button CLIENT
buttonClient = Button(text="CLIENT socket", bg="black", fg="green", command=socket_connect)
buttonClient.grid(column=2, row=2)

# Button hello
buttonConnector = Button(text="Connect SQL", bg="black", fg="green", command=sqlconnector)
buttonConnector.grid(column=3, row=3)

# Button Goodbye
buttonGoodbye = Button(text="GOODBYE", bg="black", fg="green", command=goodbye)
buttonGoodbye.grid(column=4, row=4)

# entry button 1
textentry = Entry( width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# root loop
root.mainloop()
