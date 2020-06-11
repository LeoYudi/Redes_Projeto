#!/usr/bin/env python3

import socket
from random import randint

def server():
    HOST = '127.0.0.1'  
    PORT = 65432        


    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(2)
    while True:
        (cliSocket, addr) = serverSocket.accept()  
        print(f'Connected by', addr)   
        while True:
            data = cliSocket.recv(1024).decode('UTF-8')
            print('Recebido: ', data)
            if not data:
                break
            msg = str(randint(0,9))
            print('Enviando', msg)
            cliSocket.send(msg.encode('UTF-8'))
        cliSocket.close()

server()