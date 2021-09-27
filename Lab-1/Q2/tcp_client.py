import socket

# Create Client Socket
c = socket.socket()

#Connect to server
c.connect(("localhost",6789))

name = input("Enter your name : ")

# Sends name to server
c.send(bytes(name,"utf-8"))

# Prints received greeting from server
print(c.recv(1024).decode())

# Request date and Print today's date
request = input("Enter your request : ")
c.send(bytes(request,"utf-8"))
print(c.recv(1024).decode())
