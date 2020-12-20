import pygame
import time
from random import *
import socket 
import threading 


# VARIABLES

x=300
y=300
vel = 5
velbullet = 5
color = (200,0,0)
colorbullet = (0,200,0)
bullet_positionx = -10
bullet_positiony = -10
t=1
positionx = 0
positiony = 0




player = 0
nickname = input("Choisis un surnom : ")

malist = [player, nickname, x, y,bullet_positionx,bullet_positiony]
seclist = []

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('192.168.0.47', 62985))

def receive():
	while True :
		message = client.recv(1024).decode('utf-8')
		message = eval(message)
		if message[0] == 0:
			malist = message
		if message[0] == 1:
			seclist = message

def write() :
	while True :
		message = str(malist)
		client.send(message.encode('utf-8'))









# INITIALISATION

pygame.init()

screen = pygame.display.set_mode ((0, 0), pygame.RESIZABLE)

pygame.display.set_caption ("ARCADE_ROYAL")

clock = pygame.time.Clock()






#Main loop
def mainloop(x,y,vel,velbullet,color,colorbullet,bullet_positionx,bullet_positiony,t,positionx,positiony):
	run = True
	while run == True : 

		clock.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				run = False
		keys = pygame.key.get_pressed()


	#TIR

		if pygame.mouse.get_pressed() == (1,0,0):
			bullet_positionx = x
			bullet_positiony = y
			positionx = pygame.mouse.get_pos()[0]
			positiony = pygame.mouse.get_pos()[1]
			ratio = (bullet_positionx - positionx)/(bullet_positiony - positiony)
			t=0
		
		if t==0 :
			bullet_positionx += velbullet/ratio
			bullet_positiony += velbullet*ratio

	#Déplacement

		if keys[pygame.K_z] :
			y-= vel

		if keys[pygame.K_s] :
			y+=vel

		if keys[pygame.K_d] :
			x+=vel

		if keys[pygame.K_q] :
			x-=vel


	#Affichage

		screen.fill((0,0,0))
		pygame.draw.circle(screen,color,(x,y), 20)
		pygame.draw.circle(screen,colorbullet,(bullet_positionx,bullet_positiony), 5)

		pygame.display.flip()





receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

write_thread = threading.Thread(target=mainloop)
write_thread.start()