#UDPServer.py

from socket import socket, SOCK_DGRAM, AF_INET
import random

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Waiting for connections")
while True:
    r = random.randint(0, 20)
    
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    # Capitalize the message from the client
    print (message, address)
    message = message.decode()
    if r < 10:
        continue
    if message == 'Are you there?':
        message = 'Yes, I am here'
        serverSocket.sendto(message.encode(), address)
        print("Message sent.")
serverSocket.close()