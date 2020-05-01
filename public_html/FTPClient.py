#FTPClient.py

from socket import socket, AF_INET, SOCK_STREAM
from ast import literal_eval
import time

def read_respose(socket, code):
	result = ""
	exit_condition = False
	while not exit_condition:
		message = socket.recv(2048).lstrip()
		result += message
		exit_condition = message[0:4] == "{0} ".format(code)
	return result

def expect_code(socket, code):
	recv = read_response(socket, code)
	print("<===receive: " + recv)
	return recv

def send_expect_code(socket, msg, code):
	print("===>sending: " + msg)
	socket.send(msg + "\r\n")
	return expect_code(socket, code)

def read_data(dataSocket):
	result = ""
	msg = "non-empty string"
	while len(msg) > 0:
		msg = dataSocket.recv(2048)
		result += msg
		print(msg)
	print("Socket closed on the other end, closing on this end")
	dataSocket.shutdown(SHUT_RDWR)
	dataSocket.close()
	return result 

def send(socket, msg): 
	print ("===>sending: " + msg)
	socket.send(msg.encode() + "\r\n".encode())
	recv = socket.recv(1024).decode()
	print ("<===receive: " + recv)
	return recv
	
serverName = 'ftp.cs.fiu.edu'
serverPort = 21
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message=""
condition = True
while condition:
	line = clientSocket.recv(1024).decode().lstrip()
	message += line
	condition = line[0:4] != "220 "
print (message)
#message = send(clientSocket,"USER anonymous")
#clientSocket.send("PASS tdoug016@fiu.edu\r\n".encode())
expect_code(clientSocket, "220")
send_expect_code(clientSocket,"USER anonymous", "331")
send_expect_code(clientSocket, "PASS tdoug016@fiu.edu", "230")

message=""
condition = True
while condition:
	line = clientSocket.recv(1024).decode().lstrip()
	message += line
	print (line)
	condition = line[0:4] != "230 "
print (message)
message = send(clientSocket,"CWD pub/cnt4713")
message = send(clientSocket,"TYPE A")
#message = send(clientSocket,"PASV")
message = send_expect_code(clientSocket, "PASV", "227")
start = message.find("(")
end  = message.find(")")
tuple = message[start+1:end].split(',')
print (tuple)
#build the port from the last two numbers
port = int(tuple[4])*256 + int(tuple[5])
print (port)
dataSocket = socket(AF_INET, SOCK_STREAM)
dataSocket.connect((serverName, port))
send_expect_code(clientSocket, "LIST", "150")
read_data(dataSocket)
expect_code(clientSocket, "226")
send_expect_code(clientSocket, "QUIT", "221")
message = send(clientSocket,"LIST")
message = dataSocket.recv(2048).decode()
print (message)
message = clientSocket.recv(2048).decode()
print (message)
dataSocket.close()
message = send(clientSocket,"QUIT")
clientSocket.close()
