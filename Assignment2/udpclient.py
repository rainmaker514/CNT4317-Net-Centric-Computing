#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET
from time import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
x = 0
message = "Are you there?"
print(message)
while x in range(0, 10):
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    timeout = clientSocket.settimeout(1)
    try:
        modifiedMessage, addr = clientSocket.recvfrom(2048)
        print(modifiedMessage, addr)
    except:
        print("timeout")

clientSocket.close()