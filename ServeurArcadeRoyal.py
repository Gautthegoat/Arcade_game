### serveur test

import threading 
import socket

host = '' #adresse IP (pas indispensable de la mettre là)
port = 51900

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((host,port)) #liaison serveur/hôte 
server.listen()

clients = []

def broadcast(message) : 
 	for client in clients :
 		client.send(message)

def handle(client) : 
	while True :
		message = client.recv(1024)
		broadcast(message)
		

def receive() :
	while True :
		client, address = server.accept()

		clients.append(client)

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

print("Le serveur écoute...")
receive()