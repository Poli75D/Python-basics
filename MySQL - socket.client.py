#!/usr/bin/python
import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 3306
clientsocket.connect((host, port))
msg = clientsocket.recv(2048)
clientsocket.close()
print(msg.decode('ascii'))

