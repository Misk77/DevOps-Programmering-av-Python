import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket sucessfully created")
except socket.error as errormsg:
    print("Socket creation faild".format(errormsg))

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('There was error resolving the host')
    sys.exit()

s.connect((host_ip, port))
print('The socket  has successfully to the google\\ on port == {0}.'.format(host_ip))
