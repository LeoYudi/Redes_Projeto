import socket
from random import randint

class Client:
    def __init__(self, player_id):
        self.player_id = player_id

    def __str__(self):
        return self.player_id

    def client(self):
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 65432        # The port used by the server

        cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliSocket.connect((HOST, PORT))
        cliSocket.send('TESTE'.encode('UTF-8'))
        data = cliSocket.recv(1024).decode('UTF-8')
        cliSocket.close()
        return data

jogo= Client('1')
print(jogo)
pontuação = 0
tentativa = 0

while True:
    num1 = int(jogo.client())
    num2 = int(jogo.client())
    operacao = str(randint(0,4))
    if operacao == "0":
        resp = input('Quanto é: \t' + str(num1) + ' + ' + str(num2) + ': ') 
        if int(resp) == num1+num2:
            pontuação += 1
        else:
            tentativa += 1
    elif operacao == "1":
        resp = input('Quanto é: \t' + str(num1) + ' - ' + str(num2) + ': ') 
        if int(resp) == num1-num2:
            pontuação += 1
        else:
            tentativa += 1
    else:
        resp = input('Quanto é: \t' + str(num1) + ' x ' + str(num2) + ': ') 
        if int(resp) == num1*num2:
            pontuação += 1
        else:
            tentativa += 1
    
    if pontuação == 10:
        print("Parabéns vc ganhou")
        break
    else:
        continue
    if (tentativa == 5):
        print("Precisa treinar mais :(")
        break