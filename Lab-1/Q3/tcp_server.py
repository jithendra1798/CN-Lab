import socket

port = 6789

# Create IPv4 TCP server socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bound the socket
s.bind(("localhost",port))

# Listening to clients
s.listen(1)

print("Waiting for connections....")
#Accept connection
c,addr = s.accept()
name = c.recv(1024).decode()
print("Connected with ",name)
c.send(bytes(f"Hi {name}! Welcome to our server","utf-8"))
while True:
    request = c.recv(1024).decode()
    print(f"{name} : {request}")
    if request=="bye":
        c.send(bytes(f"Server : Thank you for connecting with us!","utf-8"))
        print("Closed connection with",name)
        break
    else:
        c.send(bytes(f"Server : {input('Server : ')}","utf-8"))
c.close()
