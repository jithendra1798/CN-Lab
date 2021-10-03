import socket
import threading


host = 'localhost'
port = 6789
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
names = []


def broadcast(message,c):
    for client in clients:
        if client!=c:
            client.send(message)

# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message,client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'{name} has left the chat room!'.encode('utf-8'),client)
            names.remove(name)
            break
# Main function to receive the clients connection


def receive():
    while True:
        print('Server is running.....')
        client, address = server.accept()
        print(f'Connected with {str(address)}',end='\t')
        client.send('Enter your name : '.encode('utf-8'))
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)
        print(f'Client Name =>> {name}')
        broadcast(f'{name} has entered the chat room'.encode('utf-8'),client)
        client.send('You are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
