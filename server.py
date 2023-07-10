import threading
from socket import *

def handle_client(connectionSocket, addr):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(addr)
        print(sentence)

        if sentence.lower().startswith('rvrs'):
            sentence = sentence[::-1]
        elif sentence.lower().startswith('lwr'):
            sentence = sentence.lower()
        elif sentence.lower().startswith('dd'):
            sentence = 'hej' + sentence
        elif sentence.lower().startswith('ppr'):
            sentence = sentence.upper()
        elif sentence.lower().startswith('close'):
            connectionSocket.send(sentence.encode())
            break

        connectionSocket.send(sentence.encode())
    connectionSocket.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
    
print('Server is hella ready')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()

