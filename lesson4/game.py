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
    #Ensure constant frames/s
    main_clock.tick(50)
    
    pygame.display.update() 
