import pygame
import time
import random

# initialize game
pygame.init()

# declaration of colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# creation of display
dis_width = 500
dis_height  = 500
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Task 1')

clock = pygame.time.Clock()

def task1():

	over = False

	while not over:

		dis.fill(white)

		key = -1
		rand = random.randint(0, 2)

		if (rand==0):
			#triangulo para cima
			pygame.draw.polygon(dis, black, [[190, 290], [250, 210], [310, 290]], 0)	

		elif (rand==1):
			#triangulo para baixo
			pygame.draw.polygon(dis, black, [[190, 210], [250, 290], [310, 210]], 0)

		elif (rand==2):
			#losango
			pygame.draw.polygon(dis, black, [[210, 250], [250, 210], [290, 250], [250, 290]], 0)
		
		pygame.display.update()

		while (key == -1):	
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					over=True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						key = 0
					elif event.key == pygame.K_RIGHT:
						key = 1
					else:
						key = 2
		
		if (key == 0 and rand == 0):
			print("Acertou")
		elif (key == 1 and (rand == 1 or rand == 2)):
			print("Acertou")
		else:
			print("Errou")

		clock.tick(20)
		

	pygame.quit()
	quit()

task1()