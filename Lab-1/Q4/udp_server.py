import socket
import threading

serverPort = 6789
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
clientAddresses = []

def sendToAllClients(message, senderClientAddress):
    for clientAddress in clientAddresses:
        if str(clientAddress) != str(senderClientAddress):
            serverSocket.sendto(message, clientAddress)

def receiveMsgFromClient():
    while True:
        msgFromClient, clientAddress = serverSocket.recvfrom(2048)
        if clientAddress not in clientAddresses:
            print(str(clientAddress), 'sent first message. Address saved.')
            clientAddresses.append(clientAddress)
            msgForAll = (str(clientAddress) + ' entered the chatroom.')
            for address in clientAddresses:
                if str(address) != str(clientAddress):
                    serverSocket.sendto(msgForAll.encode(), address)
        else:
            msgForAll = str(clientAddress) + ': ' + msgFromClient.decode()
            for address in clientAddresses:
                if str(address) != str(clientAddress):
                    serverSocket.sendto(msgForAll.encode(), address)

print('Server is ready to welcome clients.')
receiveMsgFromClient()
