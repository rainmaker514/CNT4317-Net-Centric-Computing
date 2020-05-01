#TCPServer.py

from socket import socket, SOCK_STREAM, AF_INET

#Create a TCP socket 
def openTCPSocket(serverPort):
      serverSocket = socket(AF_INET, SOCK_STREAM)
      serverSocket.bind(('', serverPort))
      serverSocket.listen(1)
      return serverSocket

def sendFile(socket, file, content):
      #socket.send()
      socket.close()
      return 

def staticpage():
      return '''\
HTTP/1.1 200 OK
Content-type: text/plain
Content-length: 18

under construction'''                         

def main():
      serverSocket = openTCPSocket(1968)
      print ("Interrupt with CTRL-C")
      while True:
            print("Ready...")
      
            try:
                  connectionSocket, addr = serverSocket.accept()
                  print ("Connection from %s port %s" % addr)
                  message = connectionSocket.recv(4096).decode()
                  print(message)
                  filename = message.split()[1].partition("/")[2]
                  connectionSocket.send(staticpage().encode())
                  #sendFile(connectionSocket, filename,"image/jpg")                
                  connectionSocket.close()
            except IOError:
                  print("Not found %s" % filename)
                  #sendError(connectionSocket, '404', 'Not Found')
                  connectionSocket.close()
            except KeyboardInterrupt:
                  print ("\nInterrupted by CTRL-C")
                  break
      serverSocket.close()
      return

main()      