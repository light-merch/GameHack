import pygame
import numpy as np
import math
import datetime
from random import randint

from map_builder import map_builder

SIZE = (1280, 1024)
BG_COLOR = (50, 50, 50)
START_X = 500
START_Y = 400
SS = 2  # Step Size
BSS = 1
SIZE_BLOCK = 50
N_BLOCKS = 18

class ghost():
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def update(self):
        c = 0
        dx = abs(player1.x - self.x)
        dy = abs(player1.y - self.y)
        # с = math.sqrt(dx * dx - dy * dy)
        # k = c / BSS
        # new_dx = dx // k
        # new_dy = dy // k
        self.x += 10 # new_dx
        self.y += 10 # new_dy


class guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bulb = False

    def update(self, screen):
        screen.blit(image, (player1.x, player1.y))
        if player1.bulb:
            for i in range(200):
                for j in range(i):
                    screen.set_at((player1.x - i, player1.y - int(i / 2) + j + 50), (100, 0, 0, 0))


def add_ghosts():
    if (randint(0, 10) == 1):
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
        item.update()
        if (item.side == 'left'):
            screen.blit(ghost_left, (item.x, item.y))
        else:
            screen.blit(ghost_right, (item.x, item.y))


def title_screen(screen):
    if block_pos == 0:
        pygame.draw.rect(screen, (255, 255, 255), (200, 100, 500, 100))
    elif block_pos == 1:
        pygame.draw.rect(screen, (255, 255, 255), (200, 200, 500, 100))
    elif block_pos == 2:
        pygame.draw.rect(screen, (255, 255, 255), (200, 450, 500, 110))

    f2 = pygame.font.SysFont('Pixar One', 60)
    text2 = f2.render("START", 0, (0, 180, 0))
    screen.blit(text2, (395, 100))

    f4 = pygame.font.SysFont('Pixar One', 48)
    text4 = f4.render("NEW MAP", 0, (0, 180, 0))
    screen.blit(text4, (375, 250))

    f3 = pygame.font.SysFont('Pixar One', 48)
    text3 = f3.render("EXIT", 0, (0, 180, 0))
    screen.blit(text3, (420, 500))



def keybind(STATE, block_pos, i, done, left, right, up, down):
    global image
    if i.type == pygame.QUIT:
        done = True

    elif i.type == pygame.MOUSEBUTTONDOWN and STATE == 'create':
        if i.button == 1:
            bx = pygame.mouse.get_pos()[0] // SIZE_BLOCK
            by = pygame.mouse.get_pos()[1] // SIZE_BLOCK
            if mapp[by, bx] == N_BLOCKS:
                mapp[by, bx] = 0
            else:
                mapp[by, bx] += 1

        elif i.button == 3:
            bx = pygame.mouse.get_pos()[0] // SIZE_BLOCK
            by = pygame.mouse.get_pos()[1] // SIZE_BLOCK
            if mapp[by, bx] == 0:
                mapp[by, bx] = N_BLOCKS
            else:
                mapp[by, bx] -= 1
    
    elif i.type == pygame.KEYDOWN:
        if i.key == pygame.K_ESCAPE:
            if STATE == 'title':
                done = True
            else:
                STATE = 'title'

        if i.key == pygame.K_SPACE:
            if STATE == 'title':
                if block_pos == 0:
                    STATE = 'game'

                elif block_pos == 1:
                    STATE = 'create'

                elif block_pos == 2:
                    done = True
            else:
                if player1.bulb:
                    player1.bulb = False
                else:
                    player1.bulb = True

        if STATE == 'title':
            if i.key == pygame.K_w:
                if block_pos == 0:
                    block_pos = 2
                else:
                    block_pos -= 1
            elif i.key == pygame.K_s:
                if block_pos == 2:
                    block_pos = 0
                else:
                    block_pos += 1

        else:
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

    return STATE, block_pos, done, left, right, up, down



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(BG_COLOR)
    pygame.display.update()
    try:
        mapp = np.load('main.npy')
    except:
        mapp = np.zeros((SIZE[1] // SIZE_BLOCK, SIZE[0] // SIZE_BLOCK))

    image_back = pygame.image.load(r'guard0.png')
    image_right = pygame.image.load(r'guard1.png')
    image_front = pygame.image.load(r'guard2.png')
    image_left = pygame.image.load(r'guard3.png')
    ghost_right = pygame.image.load(r'ghost1.png')
    ghost_left = pygame.image.load(r'ghost2.png')
    image = image_front


    fl = []
    fl.append(pygame.image.load(r'floor.png'))
    fl.append(pygame.image.load(r'floor2.png'))
    fl.append(pygame.image.load(r'door.png'))

    for i in range(15):
        fl.append(pygame.image.load(f'block{i + 1}.png'))

    player1 = guard(START_X, START_Y)
    fps = 480
    block_pos = 0
    left, right, up, down = False, False, False, False
    arrGhosts = []


    done = False
    STATE = 'title'
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            STATE, block_pos, done, left, right, up, down = keybind(STATE, block_pos, i, done, left, right, up, down)

        if right == True:
            bx = (player1.x + SS + 50) // SIZE_BLOCK
            by = (player1.y + 25) // SIZE_BLOCK
            if mapp[by, bx] in [1,3]:
                player1.x += SS

        if up == True:
            bx = (player1.y - SS) // SIZE_BLOCK
            by = (player1.x + 25) // SIZE_BLOCK
            if mapp[by, bx] in [1,3]:
                player1.y -= SS
        if left == True:
            bx = (player1.x - SS) // SIZE_BLOCK
            by = (player1.y + 25) // SIZE_BLOCK
            if mapp[by, bx] in [1,3]:
                player1.x -= SS
        if down == True:
            bx = (player1.y + SS + 50) // SIZE_BLOCK
            by = (player1.x + 25) // SIZE_BLOCK
            if mapp[by, bx] in [1,3]:
                player1.y += SS


        pygame.time.wait(1000 // fps)
        screen.fill(BG_COLOR)

        if STATE == 'title':
            title_screen(screen)
        elif STATE == 'game':
            map_builder(screen, mapp, fl)
            add_ghosts()
            ghosts_update(screen)
            player1.update(screen)
        elif STATE == 'create':
            map_builder(screen, mapp, fl)
            np.save('main',mapp)
        pygame.display.update()

    pygame.quit()
