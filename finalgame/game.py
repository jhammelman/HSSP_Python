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

#load a background image
background_image = pygame.image.load("space.jpg").convert_alpha()
background_image = pygame.transform.scale(background_image,(width,height))

#load a player image
player_image = pygame.image.load("spaceship.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))

# Define the player x,y,width,height
player = pygame.Rect(300,400,60,60)

#load a image for falling objects
object_image = pygame.image.load("asteroid.png").convert_alpha()
object_image = pygame.transform.scale(object_image, (50, 50))

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
    screen.blit(background_image,(0,0)) #add background on screen
                
    screen.blit(player_image,player)
    for obj in all_objects:
        if obj.colliderect(player):
            all_objects.remove(obj)
            pygame.quit()
            sys.exit()
    	obj.y += 3 # object is falling
        if obj.y >= height:
            obj.y = -10
        screen.blit(object_image,(obj.x,obj.y))
    
    #Ensure constant frames/s
    main_clock.tick(50)
    
    pygame.display.update() 
