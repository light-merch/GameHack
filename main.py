import pygame
import numpy as np
import math
import datetime
from random import randint
import 

SIZE = (1048, 1024)
BG_COLOR = (50, 50, 50)
START_X = 500
START_Y = 400
SS = 2  # Step Size

class ghost():
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side


class guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bulb = False

    def update(self, screen):
        screen.blit(image, (player1.x, player1.y))
        if player1.bulb:
            for i in range(100):
                for j in range(i):
                    screen.set_at((player1.x - i, player1.y - int(i / 2) + j), (100, 0, 0))

def add_ghosts():
    if (randint(0, 100) == 1):
        gx = player1.x
        gy = player1.y
        while math.sqrt((gx - player1.x) * (gx - player1.x) + (gy - player1.y) * (gy - player1.y)) < 200:
            gx = randint(0, SIZE[0])
            gy = randint(0, SIZE[1])

        if (gx > player1.x):
            arrGhosts.append(ghost(gx, gy, 'left'))
        else:
            arrGhosts.append(ghost(gx, gy, 'right'))

def ghosts_update(screen):
    for item in arrGhosts:
        if (item.side == 'left'):
            screen.blit(ghost_left, (item.x, item.y))
        else:
            screen.blit(ghost_right, (item.x, item.y))

def title_screen(screen):
    f2 = pygame.font.SysFont('Pixar One', 60)
    text2 = f2.render("START", 0, (0, 180, 0))
    screen.blit(text2, (395, 100))

    f4 = pygame.font.SysFont('Pixar One', 48)
    text4 = f4.render("NEW MAP", 0, (0, 180, 0))
    screen.blit(text4, (375, 250))

    f3 = pygame.font.SysFont('Pixar One', 48)
    text3 = f3.render("EXIT", 0, (0, 180, 0))
    screen.blit(text3, (420, 500))



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(BG_COLOR)
    pygame.display.update()

    image_back = pygame.image.load(r'guard0.png')
    image_right = pygame.image.load(r'guard1.png')
    image_front = pygame.image.load(r'guard2.png')
    image_left = pygame.image.load(r'guard3.png')
    ghost_right = pygame.image.load(r'ghost1.png')
    ghost_left = pygame.image.load(r'ghost2.png')
    image = image_front

    player1 = guard(START_X, START_Y)
    fps = 240
    left, right, up, down = False, False, False, False
    arrGhosts = []


    done = False
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True

            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    if player1.bulb:
                        player1.bulb = False
                    else:
                        player1.bulb = True

                if i.key == pygame.K_w:
                    up = True
                    image = image_back
                elif i.key == pygame.K_s:
                    down = True
                    image = image_front
                elif i.key == pygame.K_a:
                    left = True
                    image = image_left
                elif i.key == pygame.K_d:
                    right = True
                    image = image_right
            elif i.type == pygame.KEYUP:
                if i.key == pygame.K_w:
                    up = False
                elif i.key == pygame.K_s:
                    down = False
                elif i.key == pygame.K_a:
                    left = False
                elif i.key == pygame.K_d:
                    right = False

        if right == True:
            player1.x += SS
        if up == True:
            player1.y -= SS
        if left == True:
            player1.x -= SS
        if down == True:
            player1.y += SS


        pygame.time.wait(1000 // fps)
        screen.fill(BG_COLOR)

        title_screen(screen)
        # add_ghosts()
        # player1.update(screen)
        # ghosts_update(screen)

        pygame.display.update()

    pygame.quit()
