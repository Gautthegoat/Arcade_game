#Serveur

import threading
import socket

host = ''
port = 51964
#port publique 51900 privé 51964

# init server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

#Distribuer
def broadcast (message):
    for client in clients:
        client.send(message)

#Introduire client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client) #numéro dans liste
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f' {nickname} a quitte le tchat !'.encode('utf-8'))
            nickname.remove(nickame)
            break

#Reception messages + distribution
def receive():
    while True:
        client, address = server.accept()
        print (f"Connecte with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Le nom du client est {nickname}!')
        broadcast(f'{nickname} a rejoint le tchat!'.encode('utf-8'))
        client.send('Connecte au server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Le serveur espionne...")
receive()

