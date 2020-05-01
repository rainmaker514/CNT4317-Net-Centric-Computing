#TCPServer.py

from socket import socket, SOCK_STREAM, AF_INET
import sys
import time

#Create a TCP socket 
def openTCPSocket(serverPort):
      serverSocket = socket(AF_INET, SOCK_STREAM)
      serverSocket.bind(('', serverPort))
      serverSocket.listen(1)
      return serverSocket

def sendFile(socket, file, content):
      f = open(file, "r")
      contents = f.read()

     
      return '''\
HTTP/1.1 200 OK
Content-type: ''' + content +'''
Content-length: 314

''' + contents     

def sendFileEmail(socket, file, content):
      f = open(file, "r")
      contents = f.read()

     
      return '''\
HTTP/1.1 200 OK
Content-type: ''' + content +'''
Content-length: 400

''' + contents 

def sendError():
      return '''\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 4646

<div class="svgcontainer">
		<div class="subcont">
			<div class="topconvo">
				<span>!@#$</span><br />your portal gun must be busted...
			</div>
			<svg version="1.1" id="fourohfour" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
			    y="0px" viewBox="0 0 265.5 114" style="enable-background:new 0 0 265.5 114;" xml:space="preserve">
				<g id="bottoms">
					<g id="leftfourbottom">
						<ellipse class="st0" cx="82.4" cy="65.5" rx="11.7" ry="3.5" />
						<path class="st1" d="M98.4,78.9c-0.8-2.8-2.8-4.4-6-4.9c0.7-2.7,1.3-5.8,1.7-8.4L93.9,66c-0.8,1.7-5.7,3-11.5,3s-10.7-1.3-11.5-3l-0.1-0.5
			c0,0.8,0.1,2.1,0.1,2.7c0,2.4-0.3,4.3-1,5.9c-0.3,0.7-1.1,1.1-2.3,1.1c-1.7,0-2.8-0.7-3.2-2l0,0c-0.3-1.3,0.4-3.5,1.9-6.6
			c0.1-0.3,0.2-0.6,0.2-0.7h-0.7c0,1.7-4.5,3-10,3s-10-1.3-10-3l-0.5-0.2c-0.7,1.8-1.3,3.4-1.8,4.6c-1.7,4.2-2.5,7.8-2.5,10.8
			c0,3.8,1.4,7.2,4.1,10.1c3.8,3.1,9.6,4.7,17.5,4.7c0.5,0.5,0.7,1.4,0.7,2.9c0,1.7,0,2.6,0.1,2.7c0.9,6.2,3.5,10,7.6,11.5
			c1.7,0.6,3.6,0.9,5.6,0.9c7.5,0,12-3,13.5-8.9c0.5-1.9,0.7-5.1,0.7-9.5c0-2.1,1-3.1,3.1-3.1c3.2-1.3,4.7-3.9,4.7-7.8h0.1
			C98.8,81.6,98.7,79.7,98.4,78.9z" />
						<ellipse class="st0" cx="55.8" cy="66" rx="10.6" ry="3" />
						<ellipse class="st2" cx="82.4" cy="65.5" rx="3.5" ry="1.1" />
						<ellipse class="st2" cx="55.5" cy="65.8" rx="3.2" ry="0.9" />
					</g>
					<g id="rightfourbottom">
						<ellipse class="st0" cx="208.1" cy="65.5" rx="11.7" ry="3.5" />
						<path class="st1" d="M224.1,78.9c-0.8-2.8-2.8-4.4-6-4.9c0.7-2.7,1.3-5.8,1.7-8.4l-0.1,0.5c-0.8,1.7-5.7,3-11.5,3c-5.9,0-10.7-1.3-11.5-3
			l-0.1-0.5c0,0.8,0.1,2.1,0.1,2.7c0,2.4-0.3,4.3-1,5.9c-0.3,0.7-1.1,1.1-2.3,1.1c-1.7,0-2.8-0.7-3.2-2l0,0
			c-0.3-1.3,0.4-3.5,1.9-6.6c0.1-0.3,0.2-0.6,0.2-0.7h-0.7c0,1.7-4.5,3-10,3s-10-1.3-10-3l-0.5-0.2c-0.7,1.8-1.3,3.4-1.8,4.6
			c-1.7,4.2-2.5,7.8-2.5,10.8c0,3.8,1.4,7.2,4.1,10.1c3.8,3.1,9.6,4.7,17.5,4.7c0.5,0.5,0.7,1.4,0.7,2.9c0,1.7,0,2.6,0.1,2.7
			c0.9,6.2,3.5,10,7.6,11.5c1.7,0.6,3.6,0.9,5.6,0.9c7.5,0,12-3,13.5-8.9c0.5-1.9,0.7-5.1,0.7-9.5c0-2.1,1-3.1,3.1-3.1
			c3.2-1.3,4.7-3.9,4.7-7.8h0.1C224.5,81.6,224.3,79.7,224.1,78.9z" />
						<ellipse class="st0" cx="181.5" cy="66" rx="10.6" ry="3" />
						<ellipse class="st2" cx="208.1" cy="65.5" rx="3.5" ry="1.1" />
						<ellipse class="st2" cx="181.2" cy="65.8" rx="3.2" ry="0.9" />
					</g>
					<g id="zerobottom">
						<path class="st1" d="M135.6,65.2L135.6,65.2c0,0.6,0,1.1,0,1.7c0,4-0.8,11.1-2.5,21.5c-0.3,0.9-0.8,1.3-1.5,1.3l-0.6-0.4
			c-0.8-5.7-1.2-10.5-1.2-14.4c0-3.5,0.3-6.6,0.9-9.4h-25.4c-0.7,4.3-1,8.9-0.9,13.8c1.2,6.9,2.6,12.3,4.1,16
			c2.3,5.5,5.6,10,9.9,13.4c5.6,3.5,11.1,5.2,16.6,5.2c1.9,0,3.8-0.2,5.6-0.7c3-0.7,5.7-2.3,8.3-4.6c2.6-2.3,4.3-5,5.3-7.8
			c4.1-8.6,6.1-18.3,6.1-29.1c0-2.2-0.1-4.4-0.3-6.5H135.6z" />
						<path class="st0" d="M160,65.2c0,2.1-5.5,3.8-12.2,3.8s-12.3-1.7-12.3-3.8s5.5-3.8,12.3-3.8S160,63.2,160,65.2z" />
						<path class="st0" d="M130.6,65.6c0,1.9-5.7,3.4-12.7,3.4s-12.8-1.6-12.8-3.5s5.7-3.5,12.8-3.5S130.6,63.7,130.6,65.6z" />
						<ellipse class="st2" cx="147.8" cy="65.2" rx="3.2" ry="1" />
						<ellipse class="st2" cx="117.9" cy="65.5" rx="3.4" ry="0.9" />
					</g>
				</g>
				<g id="tops">
					<path class="st1 picklericked" id="leftfourtop" d="M82.6,70c6.5,0,11.1-1.3,11.3-3.3c0,0,0,0,0,0c0.5-3.4,1.5-6.8,1.5-10c0-5.3-0.9-9.4-2.7-12.2
		c-2.4-3.8-6.3-6.8-11.7-9c-2.5-0.7-5.1-1-8-1c-5.8,0-9.8,1.2-12,3.6c-4.2,4.5-8.8,12.1-13.8,23c-0.9,2.2-1.7,4.4-2.4,6.1
		C44.9,69,49.6,70,55.4,70c5.1,0,8.9-0.6,10.1-1.9c1.8-3.6,3.7-6.8,4.6-8.5c0.3,2.7,0.6,5.2,0.7,7.1c0,0,0,0,0,0
		C70.9,68.7,76.1,70,82.6,70z" />
					<path class="st1 picklericked" id="rightfourtop" d="M208.2,70c6.5,0,11.1-1.3,11.3-3.3c0,0,0,0,0,0c0.5-3.4,1.5-6.8,1.5-10c0-5.3-0.9-9.4-2.7-12.2
		c-2.4-3.8-6.3-6.8-11.7-9c-2.5-0.7-5.1-1-8-1c-5.8,0-9.8,1.2-12,3.6c-4.2,4.5-8.8,12.1-13.8,23c-0.9,2.2-1.7,4.4-2.4,6.1
		c0.2,1.7,4.9,2.7,10.7,2.7c5.1,0,8.9-0.6,10.1-1.9c1.8-3.6,3.7-6.8,4.6-8.5c0.3,2.7,0.6,5.2,0.6,7.1c0,0,0,0,0,0
		C196.5,68.7,201.7,70,208.2,70z" />
					<path class="st1 picklericked" id="zerotop_3_" d="M156.5,50.9c1.6,4.3,3,9,3.5,13.9l0,0.7c-0.1,2.1-5.6,3.7-12.3,3.7c-6.8,0-12.3-1.7-12.3-3.8
		c0-0.1,0-0.1,0-0.2l0,0.2l0,0c0-1.4,0.2-2.9,0-4.2l0,0c-0.2-1.1-0.4-1.7-1.5-1.7c-0.8,0-1.4,0.4-1.7,1.1c-0.7,1.5-1.2,3.1-1.6,4.9
		h0c0,0,0,0,0,0c-0.1,0.2-0.1,0.5-0.2,0.8c-1,1.7-6.2,2.9-12.6,2.9c-6.9,0-12.4-1.5-12.7-3.3c1.2-8.1,3.7-15.2,7.5-21.4
		c3.8-4.6,6.7-6.1,8.5-7.2c3.4-2.1,7-3.1,10.7-2.8c5.7,0.4,10.8,2.1,15.4,5.1s7.7,6.8,9.4,11.4" />
				</g>
			</svg>
			<div class="bottomconvo">
				Page not found.  Wubba Lubba Dub Dub.
			</div>
		</div>
	</div>'''

def main():
      serverSocket = openTCPSocket(5454)
      print ("Interrupt with CTRL-C")
      while True:
            print("Ready...")
      
            try:
                  connectionSocket, addr = serverSocket.accept()
                  print ("Connection from %s port %s" % addr)
                  headers, post_data = readHeaders(connectionSocket)
                  filename = headers["STATUS-LINE"].split()[1].partition("/")[2]
                  print("Status Line: ", headers["STATUS-LINE"])
                  filenameLanguage = acceptLanguageModifyFile(filename, headers)
                  seconds = None
                  #if filenameLanguage == filename:
                  #	seconds = ifModifiedSinceSeconds(headers)
                  #message = connectionSocket.recv(4096).decode()
                  #print(message)
                  #filename = message.split()[1].partition("/")[2]
                  connectionSocket.send(sendFile(connectionSocket, filenameLanguage,"text/html").encode())
                  

                              
                  connectionSocket.close()
            except IOError:
                  print("Not found %s" % filename)
                  connectionSocket.send(sendError().encode())
                  
                  connectionSocket.close()
            except KeyboardInterrupt:
                  print ("\nInterrupted by CTRL-C")
                  break
      serverSocket.close()
      return

main()      