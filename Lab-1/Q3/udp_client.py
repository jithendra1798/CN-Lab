import socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host='localhost'
port=9997
while True:
    message=input('Enter message : ')
    client_socket.sendto(message.encode(),(host,port))
    d=client_socket.recvfrom(1024)
    reply=d[0].decode()
    addr=d[1]
    print('Server >>',str(reply))
