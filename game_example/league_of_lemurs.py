#Expand for complete, simplified game code.
import pygame
import random
import math
import sys
from pygame.locals import *
 
pygame.init()
WHITE = (255,255,255)

alive = True
started = False
score = 0
background = pygame.image.load('images/forest.png')
background = pygame.transform.scale(background, (900,600))
w,h = background.get_size()
screen = pygame.display.set_mode((w, h))
font = pygame.font.SysFont(None, 36)
pygame.display.set_caption('League of Lemurs')

#Text
title = font.render('League of Lemurs', True, WHITE)
instruction = font.render('Use the Space Bar to Jump and Avoid Falling',
                          True, WHITE)
start_mode = font.render('Press Enter to Start', True, WHITE)
game_over = font.render('Game Over', True, WHITE)
play_again = font.render('Press Enter to Play Again', True, WHITE)
#Creates list to hold platforms.
platforms = []

#Creates a rect and adds it to the platform
#list. Add your own new platforms, or move
#these ones around!
platform = pygame.Rect((10, 400, 300, 20))
platforms.append(platform)
platform5 = pygame.Rect((350, 400, 300, 20))
platforms.append(platform5)
platform6 = pygame.Rect((575, 300, 300, 20))
platforms.append(platform6)
platform7 = pygame.Rect((50, 300, 300, 20))
platforms.append(platform7)
platform8 = pygame.Rect((400, 200, 300, 20))
platforms.append(platform8)
 
#Variables that will control the player's x
#and y position.
x = 50
y = 50
 
#The rect for the player's square. Try and
#add an image, and animation.
player = pygame.image.load("images/lemur.png").convert_alpha()
player = pygame.transform.scale(player, (150, 100))
player_rect = player.get_rect()

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))
 
main_clock = pygame.time.Clock()
 
#Variables that control the players jumping.
jump_state = 0
jump_timer = 0
grounded = False
 
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
                player_rect.y = 50
                player_rect.x = 50
                jump_state = 0
                jump_timer = 0
                grounded = True
                
    main_clock.tick(50)
    #Check for falling off screen
    if player_rect.y >= h:
        alive = False
    #For better understanding of this code, go
    #through the "Jumping" module.
    else:
        #Sets the player's position to be above the
        #platform they collided with.
        if grounded:
            y = platforms[player_rect.collidelist(platforms)].top

        if jump_state == 0:
            if jump_timer == 0:
                if player_rect.collidelist(platforms) >= 0:
                    grounded = True
                else:
                    grounded = False
                    y += 30
        elif jump_state == 1:
            jump_timer += main_clock.get_time()
            grounded = False
            y -= 20
            if jump_timer >= 275:
                jump_state = 2
        elif jump_state == 2:
            jump_timer = 0
            jump_state = 0
    player_rect.y = y - 45
    if alive:
        score += main_clock.get_time()/500
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    for platform in platforms:
        #Draws each of the platforms in the platforms
        #list to the screen.
        pygame.draw.rect(screen, (139,82,40), (platform.x, platform.y, platform.width, platform.height))
        #Shrinks the platform, increasing difficulty
        #over time.
        if platform.width >= 125:
            platform.width -= 0.5
        #Sets the platform to the right side of the
        #screen when it hits the left.
        if platform.x <= 0 - 250:
            platform.x = 640
            continue
        #Moves the platform to the left.
        else:
            platform.x -= 6
            continue
 

    screen.blit(player, player_rect)
    if not started:
        screen.blit(title, [w/2 - title.get_width()/2,
                            h/2 - title.get_height()/2])
        screen.blit(instruction, [w/2 - instruction.get_width()/2,
                                  h/2 - instruction.get_height()/2+50])
        screen.blit(start_mode, [w/2 - start_mode.get_width()/2,
                                 h/2 - start_mode.get_height()/2+100])
    else:
        if alive:
            draw_text('Score: %s' % (int(score)), font, screen, 5,5)
        else:
             score_text = font.render('Score %s' % (int(score)), True, WHITE)
             screen.blit(score_text, [w/2 - score_text.get_width()/2,
                                      h/2 - score_text.get_height()/2+50])
             screen.blit(game_over, [w/2 - game_over.get_width()/2,
                                     h/2 - game_over.get_height()/2])
             screen.blit(play_again, [w/2 - play_again.get_width()/2,
                                      h/2 - play_again.get_height()/2+100])
    pygame.display.update()
