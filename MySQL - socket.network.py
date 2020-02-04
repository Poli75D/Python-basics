#!/usr/bin/python
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 3306
serversocket.bind((host, port))
serversocket.listen(10)
while True:
    clientsocket, addr = serversocket.accept()
    print("connection from" +  "%s" %str(addr))
    msg = "thx for connecting" + " \r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
