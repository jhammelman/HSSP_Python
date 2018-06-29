#Expand for complete, simplified game code.
import pygame
import random
import math
import sys
import time
from pygame.locals import *
 
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
width = 640
height = 460

alive = True
started = False
score = 0
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 36)
pygame.display.set_caption('Jumper')

t0= time.clock()

#Text
title = font.render('Jumper', True, BLACK)
instruction = font.render('Use the Space Bar to Jump and Avoid Falling',
                          True, BLACK)
start_mode = font.render('Press Enter to Start', True, BLACK)
game_over = font.render('Game Over', True, BLACK)
play_again = font.render('Press Enter to Play Again', True, BLACK)
#Creates list to hold platforms.
platforms = []

def draw_player():
    pygame.draw.rect(screen,BLACK, player)
    
def draw_screen():
    screen.fill(WHITE)

#Creates a rect and adds it to the platform
#list. Add your own new platforms, or move
#these ones around!
platform = pygame.Rect((10, 400, 200, 20))
platforms.append(platform)
platform5 = pygame.Rect((50, 140, 200, 20))
platforms.append(platform5)
platform6 = pygame.Rect((575, 300, 200, 20))
platforms.append(platform6)
platform7 = pygame.Rect((300, 100, 200, 20))
platforms.append(platform7)
platform8 = pygame.Rect((400, 200, 200, 20))
platforms.append(platform8)
 
#Variables that will control the player's x
#and y position.
x = 50
y = 50
 
#The rect for the player's square. Try and
#add an image, and animation.
player = pygame.Rect(300,400,60,60)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))
 
main_clock = pygame.time.Clock()
 
#Variables that control the players jumping.
jump_state = 0
jump_timer = 0
grounded = False
shrunk = False
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Let's the player jump, only if they're
        #on the ground and press space.
        if not started and event.type == KEYUP:
            if event.key == K_RETURN:
                started = True
        if started and event.type == KEYDOWN:
            if event.key == K_SPACE:
                if jump_state == 0 and grounded:
                    jump_state = 1
        if not alive and event.type == KEYUP:
            if event.key == K_RETURN:
                score = 0
                alive = True
                player.y = 50
                player.x = 50
                jump_state = 0
                jump_timer = 0
                grounded = True
                
    main_clock.tick(50)
    #Check for falling off screen
    if player.y >= height:
        alive = False
        for platform in platforms:
            platform.width = 200
    else:
        #Sets the player's position to be above the
        #platform they collided with.
        if grounded:
            y = platforms[player.collidelist(platforms)].top

        if started and jump_state == 0:
            if jump_timer == 0:
                if player.collidelist(platforms) >= 0:
                    grounded = True
                else:
                    grounded = False
                    y += 30
        elif started and jump_state == 1:
            jump_timer += main_clock.get_time()
            grounded = False
            y -= 20
            if jump_timer >= 275:
                jump_state = 2
        elif started and jump_state == 2:
            jump_timer = 0
            jump_state = 0
    if started:
        player.y = y - 45
    if alive and started:
        score += float(main_clock.get_time())/1000
    draw_screen()
    
    for platform in platforms:
        #Draws each of the platforms in the platforms
        #list to the screen.
        pygame.draw.rect(screen, BLACK, (platform.x, platform.y, platform.width, platform.height))
        #Shrinks the platform, increasing difficulty
        #over time.
        if platform.width >= 125 and (time.clock() - t0) > 3:
            platform.width -= 0.5
            shrunk = True
        #Sets the platform to the right side of the
        #screen when it hits the left.
        if platform.x <= 0 - 250:
            platform.x = 640
            continue
        #Moves the platform to the left.
        else:
            if alive and started:
                platform.x -= 6
            continue
    if shrunk:
        t0 = time.clock()
        shrunk = False
    draw_player() 
    
    if not started:
        screen.blit(title, [width/2 - title.get_width()/2,
                            height/2 - title.get_height()/2])
        screen.blit(instruction, [width/2 - instruction.get_width()/2,
                                  height/2 - instruction.get_height()/2+50])
        screen.blit(start_mode, [width/2 - start_mode.get_width()/2,
                                 height/2 - start_mode.get_height()/2+100])
    else:
        if alive:
            draw_text('Score: %s' % (int(score)), font, screen, 5,5)
        else:
            score_text = font.render('Score %s' % (int(score)), True, WHITE)
            screen.blit(score_text, [width/2 - score_text.get_width()/2,
                                     height/2 - score_text.get_height()/2+50])
            screen.blit(game_over, [width/2 - game_over.get_width()/2,
                                    height/2 - game_over.get_height()/2])
            screen.blit(play_again, [width/2 - play_again.get_width()/2,
                                     height/2 - play_again.get_height()/2+100])
    pygame.display.update()
