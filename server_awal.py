import sys
import socket
import io
import os.path

# Create a TCP/IP socket

def get_fileName(temp):
	temp1=temp.split()
	temp2=temp1[1]
	temp3=temp2[1:]
	return temp3

def get_file(temp):
	if os.path.isfile(temp+".jpg"):
		file_name=temp+".jpg"	
	else:	
		file_name="default.jpg"
	photo=open(file_name, "r+")
	result=photo.read()
	photo.close()
	return result
	

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 1212)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    	# Wait for a connection
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
	command = ''
    	while True:
        	data = connection.recv(32)
        	command=command+data
		if command.endswith("\r\n\r\n"):
			break
	name=get_fileName(command)
	result=get_file(name)
	response="\HTTP/1.1 200 OK \n\n%s"%result	
        # Clean up the connection
	connection.sendall(response)	
	connection.close()

