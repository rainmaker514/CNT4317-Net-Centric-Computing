#TCPClient.py

from socket import socket, AF_INET, SOCK_STREAM
serverName = 'localhost'
serverPort = 1968
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('What is your request?')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(4096).decode()
print ('From Server: ', modifiedMessage)
clientSocket.close()