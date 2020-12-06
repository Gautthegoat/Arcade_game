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
def broadcast (nicknames):
	for client in clients:
		client.send(nicknames)


#Reception messages + distribution
def receive():
	while True:
		client, address = server.accept()
		clients.append(client)

		nickname = client.recv(1024).decode('utf-8')
		nicknames = []
		nicknames.append(nickname)

		broadcast(nicknames)

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

print("Le serveur espionne...")
receive()

