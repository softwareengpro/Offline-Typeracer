# client side program
import socket
import os
c=socket.socket()
host=socket.gethostname()
port=12345
c.connect((host, port))
print c.recv(1024)

