##### What is socket - https://www.tutorialspoint.com/python3/python_networking.htm
#### sockets are bidirectional cuommunication channel
#  https://www.tutorialspoint.com/python3/python_networking.htm


################################### Terms & descriptions - sockets vocabulary - ##########################################

######    Domain- the family od protocols that is used as the transport mechanism
# AF_INET  , PF_INET   , PF_UNIX and so on.....

######  type - type of comunnication between two endpoints
# SOCK_STREAM  - connections-oriented protocols
#  SOCK_DGRAM - connectionless protocol

###### protocol - typically zero
# this may be used to identify a variant of protocol within a domain and type

#######  hostname - The identifier of a network interface-
# A string, wich can be a hostname, or an ipv6 address in colon
# A string "<Broadcast>" wich specifies an INADDR_BROADCAST adress
# A zero-length string wich specifies INADRR_ANY or
# AN integer, interpreted as a binary adress in host by order

#######   port - each server listens for clients calling on one or more ports
# A port may be a fixnum port number , a string containing a port number or
# or the name of a service


############################################### The socket Module ###############################################
## To create a socket, you must use the socket.socket() funtion available in socket module
# the general syntax  is -
"""
import socket
s= socket.socket(socket_family,socket_type,protocol = 0)
"""
# socket_family - This is either AF_INET or AF_UNIX
# socket_type - this is either SOCKET_STREAM or SOCKET_DGRAM
# protocol - This is usually left out, defaulting to 0 (zero)

#### Ones you have your socket object, then you can use the required functions to create your client
# or server program. Following is the list of funtions reuired

###############################################   SERVER SOCKET METHODS ###############################################
# s.bind() - This method binds address (hostname,port,number pair) to socket
# s.listen() - This method sets up and start the TCP client
# s-accept() - This passively accept TCP client connection, waiting until connection arrives(blocking)

###############################################   CLIENT SOCKET METHODS ###############################################
# s.connect() - This method actively initiates TCP server connection

###############################################   GENERAL SOCKET METHODS ###############################################
# s.recv() - This method recevies TCP message
# s.send() - This method transmit TCP message
# s.recvfrom() - This method recevies UDP message
# s.sendto() - This method transmit UDP message
# s.close() - This method closes socket
# socket_gethostname() - Returns the hostname

###############################################   A SIMPLE SERVER  ###############################################
# first create a socket using the the set up the general socket.socket()
# Then call the bind(hostname,port)
# call the accept method of the returned object, THIS method waits until a client connects to the port you specified
# and then return a connection object that represent the connection to the client


###############################################   A SIMPLE CLIENT  ###############################################
# write a simple client program wich open a conneection at given port 12345 and given host
# Once you have the socket open you can read from it like any I/O object
# remember to close then you done, as you would close a file
### Following code is a very simple client that connect to given host and port
# reads any available data from the socket and the exits


###############################################   Python INTERNET MODULES  ###############################################






