import sys
import socket
import thread
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
print >>sys.stderr, 'Start to Chat'

def send_chat(threadName, delayed):
	while True:
		# Send data
		message = raw_input("")
	
		print >>sys.stderr, 'sending "%s"' % message
		sock.sendall(message)
		print >>sys.stderr, ' '
		
def receive_chat(threadName1, delayed):
	while True:
		data = sock.recv(128)
		if len(data) > 0:
			print >>sys.stderr, 'received "%s"' %data
			


try:
	thread.start_new_thread(send_chat, ("Thread-1", 2))
	thread.start_new_thread(receive_chat, ("Thread-2", 2))
	
	#time.sleep(10)

except:
	print >>sys.stderr, 'error to start thread'
	
while 1:
	pass
