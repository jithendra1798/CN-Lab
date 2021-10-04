import socket

c = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
host = "localhost"
port = 6789

message = "date"
c.sendto(message.encode("utf-8"),(host,port))
data, addr = c.recvfrom(1024)
print("Server :",str(data.decode()))
c.close()
