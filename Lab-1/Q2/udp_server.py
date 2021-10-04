import socket
from datetime import date

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
host = "localhost"
port = 6789
s.bind((host, port))
message = ''

while True:
    print("Server is running....")
    data, address = s.recvfrom(1024)
    print(str(data.decode()))
    if str(data.decode())=="date":
        today = date.today()
        message = f"Today's date : {today}".encode("utf-8")
    else:
        message = bytes("Request not found! Try again","utf-8")
    s.sendto(message,address)
