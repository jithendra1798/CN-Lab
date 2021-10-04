import socket
import threading

c = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
host = "localhost"
port = 6789
server = (host,port)

message = "Hi Server"
c.sendto(message.encode("utf-8"),server)
data, addr = c.recvfrom(1024)
print(data.decode(),end="")

name = input()
message = name.encode('utf-8')
c.sendto(message,server)

def send():
    while True:
        message = input()
        if message == "quit":
            c.close()
            break
        c.sendto(f"{name} >> {message}".encode("utf-8"), (host,port))
def rec():
    while True:
        data, address = c.recvfrom(1024)
        if str(data.decode())=='quit':
            c.close()
            break
        print(data.decode())


x1 = threading.Thread(target = send)
x2 = threading.Thread(target = rec)

x1.start()
x2.start()
