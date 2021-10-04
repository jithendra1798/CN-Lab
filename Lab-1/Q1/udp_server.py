import socket

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
host = "localhost"
port = 6789
s.bind((host, port))

while True:
    print("Server is running....")
    data, address = s.recvfrom(1024)
    print(str(data.decode()))
    message = "Greetings! Your data is received to our server.".encode('utf-8')
    s.sendto(message,address)
