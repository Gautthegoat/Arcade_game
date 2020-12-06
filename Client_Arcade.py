##Client

import socket
import threading
import pygame

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('78.193.131.98', 51900))

#Variables liste
nickname = input("Choose a nickname: ")
x=10
y=10
nickname = [nickname,x,y]
nicknames =[]

#LANCEMENT PYGAME


def receive():
	while True:
#		nicknames = client.recv(1024).decode('utf-8')
		nicknames = client.recv(1024)
		nicknames = [x.decode('UTF8') for x in nicknames]

def write():
	while True:
		client.send([x.encode('utf-8') for x in nickname])

def affichage():
	#AFFICHER TOUTES LES VARIABLES
	print(nicknames)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

affichage_thread = threading.Thread(target=affichage)
affichage_thread.start()