#!/usr/bin/env python3

import socket
from random import randint


def server():
    HOST = '127.0.0.1'
    PORT = 65432

    next = 'NEXT'

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(2)
    print('Server rodando')
    while True:
        (cliSocket, addr) = serverSocket.accept()
        print(f'Connected by', addr)
        while True:
            ready = cliSocket.recv(1024).decode('UTF-8')
            if not ready:
                continue
            print('Recebido: ', ready)
            if ready == 'READY':
                while True:
                    if next == 'NEXT':
                        num1 = str(randint(0, 9))
                        num2 = str(randint(0, 9))
                        operacao = str(randint(0, 2))
                        print('Enviando ', num1, num2, operacao)
                        cliSocket.send((num1 + num2 + operacao).encode('UTF-8'))
                    elif next == 'GIVEUP':
                        cliSocket.send('Precisa treinar mais :('.encode('UTF-8'))
                        break
                    elif next == 'LOST' or next == 'WIN':
                        break
                    next = cliSocket.recv(1024).decode('UTF-8')
            elif ready == 'CLOSE':
                break

        # msg = str(randint(0, 9))
        # print('Enviando', msg)
        # cliSocket.send(msg.encode('UTF-8'))
        cliSocket.close()


server()
