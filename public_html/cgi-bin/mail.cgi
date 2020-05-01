#!/usr/bin/python3
import sys
sys.stderr = sys.stdout
import socket
import time
import os
import mod_html

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

def html(method, toField, fromField, subject, body):
    print ('''\
<!DOCTYPE html>
<html>
<head>
    <title>Send an email!</title>
</head>
<body>

<h2>Email Form</h2>

<form action="" method = "{1}">
  To:<br>
  <input type="text" name="to" toField="{4}">
  <br>
  From:<br>
  <input type="text" name="from" fromField="{2}">
  <br>
  Subject:<br>
  <input type="text" name="subject" subject="{3}">
  <br><br>
  Body:<br>
 	<input type="text" name = "body" body = "{4}">
  <br><br>
  <input type="submit" value="Submit">
</form> 

<p>Click the "Submit" button to send an email.</p>

</body>
</html>
'''.format(toField, fromField, subject, body,  method))

def main():
    print("content-type: text/html\n")
    toField = ""
    fromField = ""
    subject = ""
    body = ""
    parsed = mod_html.parse()
    if 'to' in parsed:
        toField  = parsed['to']
    if 'from' in parsed:
        fromField  = parsed['from']
    if 'subject' in parsed:
        subject = parsed['subject']
    if 'body' in parsed:
        body  = parsed['body']
   
       
    html("GET", toField, fromField, subject, body)

    sendEmail(toField, fromField, subject, body)
 
def sendEmail(toField, fromField, subject, body):
    serverName = 'smtp.cis.fiu.edu'
    serverPort = 25
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    recv=send_recv(clientSocket, None, '220')

    clientName = 'teriq' 
    data = fromField.split()
    userName = data[0]
    userServer = data[1]
    data2 = toField.split()
    toName = data2[0]
    toServer = data2[1]
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
    send(clientSocket, "Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S -0400", time.localtime()));
    send(clientSocket, "From: <%s@%s>" % (userName, userServer));
    send(clientSocket, "Subject:" + subject);
    send(clientSocket, "To: %s@%s" % (toName, toServer));
    send(clientSocket, ""); #End of headers
    send(clientSocket, body);
   # send(clientSocket, "Hola Mundo");
    #send(clientSocket, "ocelot client");
    #Message ends with a single period.
    send_recv(clientSocket, ".", '250');
    #Send QUIT command and get server response.
    quitCommand='QUIT'
    quitRcpt = send_recv(clientSocket, quitCommand, '221')

main()
