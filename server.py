import sys
import socket
import thread
from threading import Thread

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
client_address = []
connection = []
def send_chat():
	while True:
		i=0
		while i<2:
			data=connection[i].recv(128)
			if len(data)>0:
				if i==1:
					connection[0].sendall(data)
				else:
					connection[1].sendall(data)
			i+=1		
def accept_client():
	i=0
	while i<2:
		c, address = sock.accept()
		connection.append(c)
		client_address.append(address)
		i+=1
	t2.start()
	
	t1.join()
	t2.join()
		
# Listen for incoming connections
sock.listen(5)


try:
	t1 = Thread(target=accept_client)
	t2 = Thread(target=send_chat)
	t1.start()
	
finally:
	print >>sys.stderr, 'close'
	
