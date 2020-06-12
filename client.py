import socket
from random import randint


class Client:

    def __init__(self, player_id):
        self.player_id = player_id
        self.cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pontuacao = 0
        self.vidas = 5

    def __str__(self):
        return self.player_id

    def conectar(self):
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 65432  # The port used by the server

        self.cliSocket.connect((HOST, PORT))

    def fechar(self):
        self.cliSocket.close()

    def receber(self):
        data = self.cliSocket.recv(1024).decode('UTF-8')
        return data

    def enviar(self, data):
        self.cliSocket.send(data.encode('UTF-8'))


cliente = Client('1')
print(cliente)

cliente.conectar()

while True:
    ready = input('Comando (READY ou CLOSE): ')
    if ready == "READY":
        cliente.enviar(ready)
        while True:
            data = cliente.receber()
            num1 = int(data[0])
            num2 = int(data[1])
            operacao = int(data[2])
            print(num1, num2, operacao)
            if operacao == 0:
                resp = input('Quanto é: \t' + str(num1) + ' + ' + str(num2) + ': ')
                if int(resp) == num1 + num2:
                    cliente.pontuacao += 1
                else:
                    cliente.vidas -= 1
            elif operacao == 1:
                resp = input('Quanto é: \t' + str(num1) + ' - ' + str(num2) + ': ')
                if int(resp) == num1 - num2:
                    cliente.pontuacao += 1
                else:
                    cliente.vidas -= 1
            else:
                resp = input('Quanto é: \t' + str(num1) + ' x ' + str(num2) + ': ')
                if int(resp) == num1 * num2:
                    cliente.pontuacao += 1
                else:
                    cliente.vidas -= 1

            if cliente.vidas == 0:
                cliente.enviar('LOST')
                print('Precisa treinar mais :(')
                break

            if cliente.pontuacao == 10:
                cliente.enviar('WIN')
                print('Parabéns :)')
                break

            while True:
                next = input('Comando (NEXT ou VLIFES ou VPOINTS): ')
                if next == 'NEXT':
                    cliente.enviar(next)
                    break
                elif next == 'VLIFES':
                    print('Vidas: ', cliente.vidas)
                elif next == 'VPOINTS':
                    print('Pontos: ', cliente.pontuacao)
                else:
                    print('Comando inválido')

    elif ready == 'CLOSE':
        cliente.enviar(ready)
        break
    else:
        print('Comando Inválido')

cliente.fechar()
