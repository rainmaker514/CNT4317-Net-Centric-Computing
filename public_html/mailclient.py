#!/usr/bin/python

import socket
import time

def send_recv(socket, msg, code):
    if msg != None:
        print ("Sending==> ", msg)
        socket.send(msg.encode() + '\r\n'.encode())

    recv = socket.recv(1024).decode()
    print ("<==Received:\n", recv)
    if recv[:3]!=code:
        print ('%s reply not received from server.' % code)
    return recv

def send(socket, msg):
    print ("Sending ==> ", msg)
    socket.send(msg.encode() + '\r\n'.encode())

serverName = 'smtp.cis.fiu.edu'
serverPort = 25

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
recv=send_recv(clientSocket, None, '220')

clientName = 'teriq'
userName="teriq0514"
userServer="outlook.com"
toName="tdoug016"
toServer="fiu.edu"
#Send HELO command and print (server response.)
heloCommand='EHLO %s' % clientName
recvFrom = send_recv(clientSocket, heloCommand, '250')
#Send MAIL FROM command and print (server response.)
fromCommand='MAIL FROM: <%s@%s>' % (userName, userServer)
recvFrom = send_recv(clientSocket, fromCommand, '250')
#Send RCPT TO command and print (server response.)
rcptCommand='RCPT TO: <%s@%s>' % (toName, toServer)
recvRcpt = send_recv(clientSocket, rcptCommand, '250')
#Send DATA command and print (server response.)
dataCommand='DATA'
dataRcpt = send_recv(clientSocket, dataCommand, '354')
#Send message data.
send(clientSocket, "Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S -0400", time.localtime()))
send(clientSocket, "From: Teriq Douglas <%s@%s>" % (userName, userServer))
send(clientSocket, "Subject: Simple Mail Message")
send(clientSocket, "To: %s@%s" % (toName, toServer))
send(clientSocket, ""); #End of headers
send(clientSocket, "Hello World")
send(clientSocket, "Hola Mundo")
send(clientSocket, "ocelot client")
#Message ends with a single period.
send_recv(clientSocket, ".", '250')
#Send QUIT command and get server response.
quitCommand='QUIT'
quitRcpt = send_recv(clientSocket, quitCommand, '221')
