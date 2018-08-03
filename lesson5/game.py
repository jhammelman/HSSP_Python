import pygame
import sys
from pygame.locals import *

pygame.init()

# Define the screen
width = 640
height = 460
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
main_clock = pygame.time.Clock()

# Define the player x,y,width,height
player = pygame.Rect(300,400,60,60)
all_objects = [] #empty objects list
pos_x = 100
pos_y = -10 #make the circle off screen
obj = pygame.draw.circle((screen),(0,0,0),(pos_x,pos_y),20,0)
all_objects.append(obj) 

player_speed=20
while True:
    # We will write anything we want to happen in game code here
    
    # Commands from keyboard
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #check for pressing down on a key
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.x -= player_speed
            if event.key == K_RIGHT:
                player.x += player_speed
    screen.fill((255,255,255)) #draw screen
    pygame.draw.rect(screen, (0,0,0), player) #draw player
    for obj in all_objects:
        if obj.colliderect(player):
            all_objects.remove(obj)
            pygame.quit()
            sys.exit()
    	obj.y += 3 # object is falling
        if obj.y >= height:
            obj.y = -10
        obj = pygame.draw.circle((screen), (0, 0, 0),
				 (obj.x, obj.y),
				 20, 1)
        
    #Ensure constant frames/s
    main_clock.tick(50)
    
    pygame.display.update() 
