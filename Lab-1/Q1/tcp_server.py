import socket
port = 6789

# Create TCP server socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bound the socket
s.bind(("localhost",port))

# Listening to clients
s.listen(1)

print("Waiting for connections....")

# Server connecting with clients
while True:
    #Accept connection
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ",name)
    c.send(bytes(f"Hi {name}! Welcome to our server","utf-8"))
    c.close()
