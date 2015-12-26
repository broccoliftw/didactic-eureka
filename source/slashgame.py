# -*- coding: latin-1 -*-
import pygame,math,sys,os
from pygame.locals import *
from pygame.compat import geterror
from random import *
#functions

def startGraphics(w,h):
	pygame.init()
	screen = pygame.display.set_mode((1600,900),FULLSCREEN)
	
	pygame.display.flip()
	running = 1
	background = pygame.image.load("../res/background.png").convert()			
	background = pygame.transform.scale(background, (w,h))
	backgroundpos = background.get_rect(center=(w/2,h/2))
	screen.blit(background,backgroundpos)		
	pygame.display.flip()
	return screen	
	
#screen
w = 1600
h = 900
SQUARESIZE = int(h/9)
UIStartX = int(SQUARESIZE*9)
screen = startGraphics(w,h)
xSize = 9
ySize = 9
panel = pygame.image.load("../res/panel.jpg").convert()
panel = pygame.transform.scale(panel, (w-UIStartX, h))
screen.blit(panel,(UIStartX, 0))
	
#mechanics
play = 1
water_flow_constant = 200
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Images
#pipe_filled_vertical_image = pygame.transform.scale(pygame.image.load("../res/pipe_filled_vertical_image.png").convert(), (SQUARESIZE,SQUARESIZE))


counter = 0
while play:
	#eventchain
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				pygame.display.quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			(x,y) = pygame.mouse.get_pos()
			(newX,newY) = (int(x/SQUARESIZE),int(y/SQUARESIZE))
			print(newX,newY)

	pygame.display.flip()