'''
Jennifer Hammelman
6/2/2016
code by iDTech, Bubble Buster
'''
import pygame
import sys
from pygame.locals import *
import time
import random

pygame.init()

width = 640
height = 460
#screen stuff
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.set_caption('Avoider Game')
font = pygame.font.SysFont(None, 36)
main_clock = pygame.time.Clock()
pygame.key.set_repeat(100,50)

#initialize
lives = 3
alive = True

#player
player = pygame.Rect(300,400,60,60)
player_speed = 6
move_right = False
move_left = False


t0= time.clock()

def draw_player():
    pygame.draw.rect(screen, (0,0,0), player)
def draw_screen():
    screen.fill((255,255,255))
def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)
x_position = 320
y_position = 380
speed = [5, -5]


all_objects = []
objects_radius = 20
objects_edge = 1
fall_speed = 3

def create_falling_object():
    pos_x = random.randint(objects_radius,width)
    pos_y = -10
    obj = pygame.draw.circle((screen),(0,0,0),(pos_x,pos_y),objects_radius,0)
    all_objects.append(obj)
    
def draw_falling_objects():
    for obj in all_objects:
        obj = pygame.draw.circle((screen), (0, 0, 0), (obj.x, obj.y),
                                    objects_radius, objects_edge)
def update_falling_objects():
    for obj in all_objects:
        obj.y += fall_speed
        if obj.y >= height:
            all_objects.remove(obj)
while True:
    update_falling_objects()
    #check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a and player.left > 0:
                player.x -= player_speed
            if event.key == K_s and player.right < width:
                player.x += player_speed
            if not alive:
                if event.key == K_RETURN:
                    lives = 3
                    alive = True
                    for x in range(0,len(all_objects)):
                        all_objects.pop()
    if time.clock() - t0 > 3:
        create_falling_object()
        t0 = time.clock()
        
    #Ensure constant frames/s
    main_clock.tick(50)

        
    #Test collisions with the bubbles
    for obj in all_objects:
        if alive:
            if obj.colliderect(player):
                all_objects.remove(obj)
                lives -= 1

    if lives <= 0:
        alive = False
    
    draw_screen()
    draw_falling_objects()
    draw_player()

    if alive:
        draw_text('Lives: %s' % (lives), font, screen, 540, 5)
    else:
        draw_screen()
        draw_text('Game Over', font, screen, 255,5)
        draw_text('Press Enter to Play Again', font, screen , 180, 420)
    pygame.display.update()


