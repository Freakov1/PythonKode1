import requests
from socket import *



api_url = "https://localhost:7076/api/P2P"
response = requests.get(api_url, verify=False)
files = response.json()
print(files)
print(files[0])
filename = files[0]["fileName"]
fileport = files[0]["port"]
fileip = files[0]["ip"]
print(filename)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((fileip, fileport))

clientSocket.send(filename.encode())

file = open('c:/temp/' + filename, 'wb')
file_data = clientSocket.recv(1024)
while (file_data):
    print("Receiving...")
    file.write(file_data)
    file_data = clientSocket.recv(1024)
file.close()

print("Done Sending")
clientSocket.close()
