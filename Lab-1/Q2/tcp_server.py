import socket
from datetime import date

port = 6789

# Create IPv4 TCP server socket
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
    request = c.recv(1024).decode()
    if request=="date":
        today = date.today()
        c.send(bytes(f"Today's date : {today}","utf-8"))
        print("Sent date to",name)
    else:
        c.send(bytes("Request not found! Try again","utf-8"))
    c.close()
