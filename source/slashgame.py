# -*- coding: latin-1 -*-
import pygame,math,sys,os
from pygame.locals import *
from pygame.compat import geterror
from random import *
from Queue import *
from gameStatus import *
#functions
def check_keys(screen,game_status,k):
	check = False
	if k == pygame.K_RETURN:
		pygame.display.quit()
	elif k == pygame.K_q:
		if game_status.check("q"):
			check = True
	elif k == pygame.K_w:
		if game_status.check("w"):
			check = True
	elif k == pygame.K_e:
		if game_status.check("e"):
			check = True
	elif k == pygame.K_r:
		if game_status.check("r"):
			check = True
	elif k == pygame.K_a:
		if game_status.check("a"):
			check = True
	elif k == pygame.K_s:
		if game_status.check("s"):
			check = True
	elif k == pygame.K_d:
		if game_status.check("d"):
			check = True
	elif k == pygame.K_z:
		if game_status.check("z"):
			check = True
	elif k == pygame.K_x:
		if game_status.check("x"):
			check = True
	elif k == pygame.K_c:
		if game_status.check("c"):
			check = True
	elif k == pygame.K_f:
		if game_status.check("f"):
			check = True
	if check:
		font = pygame.font.Font(None, 68)
		text = font.render(game_status.sequence[game_status.current], 1, (50, 56, 255))
		textpos = text.get_rect(center=((1+game_status.current)*h/21,h/2))
		screen.blit(text, textpos)
		pygame.display.flip()
		game_status.increase()
	else:
		font = pygame.font.Font(None, 68)
		text = font.render(game_status.sequence[game_status.current], 1, (255, 0, 0))
		textpos = text.get_rect(center=((1+game_status.current)*h/21,h/2))
		screen.blit(text, textpos)
		pygame.display.flip()

def startGraphics(w,h):
	pygame.init()
	screen = pygame.display.set_mode((1600,900),FULLSCREEN)
	pygame.display.flip()
	return screen	
def init_game(screen,game_status):
		game_status.change_seq()
		background = pygame.image.load("../res/background.png").convert()			
		background = pygame.transform.scale(background, (w,h))
		backgroundpos = background.get_rect(center=(w/2,h/2))
		screen.blit(background,backgroundpos)		
		font = pygame.font.Font(None, 68)
		panel = pygame.image.load("../res/panel.jpg").convert()
		panel = pygame.transform.scale(panel, (w-UIStartX, h))
		screen.blit(panel,(UIStartX, 0))
		for i in range(len(game_status.sequence)):
			text = font.render(game_status.sequence[i], 1, (255, 255, 255))
			textpos = text.get_rect(center=((1+i)*h/21,h/2))
			screen.blit(text, textpos)
		game_status.done = 0;
#screen
w = 1600
h = 900
SQUARESIZE = int(h/9)
UIStartX = int(SQUARESIZE*9)
screen = startGraphics(w,h)
xSize = 9
ySize = 9
#mechanics
play = 1
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Images
#pipe_filled_vertical_image = pygame.transform.scale(pygame.image.load("../res/pipe_filled_vertical_image.png").convert(), (SQUARESIZE,SQUARESIZE))

game_status = gameStatus()
game_status.change_seq()
print(game_status.sequence)
while play:
	#eventchain
	
	if game_status.done == 1:
		init_game(screen,game_status)
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			check_keys(screen,game_status,event.key)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			(x,y) = pygame.mouse.get_pos()
			print(x,y)			
	pygame.display.flip()
	