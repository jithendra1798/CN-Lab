import socket

port = 6789

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Binding server
s.bind(("localhost", port))
print "waiting on port:", port
while 1:
	data, addr = s.recvfrom(1024)
	print data

