import socket
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
host = "localhost"
port = 6789
server = (host, port)
s.bind(server)

print("Server is running....")

def new_client(data, address):
    print(data.decode())
    #\nType 'quit' to exit.
    message = f"Enter name : ".encode('utf-8')
    s.sendto(message,address)
    data, address = s.recvfrom(1024)
    name = str(data.decode())
    print(name,"started messaging")

def send():
    while True:
        message = ("Server >> "+input()).encode("utf-8")
        s.sendto(message,address)

def rec(x1):
    while True:
        data, address = s.recvfrom(1024)
        if data.decode()=="Hi Server":
            name = new_client(data, address)
        elif str(data.decode())=='quit':
            s.close()
            x1.kill()
            quit()
        else:
            print(data.decode())

data, address = s.recvfrom(1024)
name = new_client(data, address)

x1 = threading.Thread( target = send )
x2 = threading.Thread( target = rec, args=(x1,))

x1.start()
x2.start()
