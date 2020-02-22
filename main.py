import datetime
from random import randint
import time
import math

import pygame
import numpy as np

from build_map import build_map
from npcs import bullet, ghost

# TODO finish params
SIZE = (1280, 1024)         # Canvas size
BG_COLOR = (50, 50, 50)     # Background color
START_X = 50                # Guard start coordinate
START_Y = 150               # Guard start coordinate
SS = 6                      # Step size
BSS = 1                     # Ghost step size
BLOCK_SIZE = 50
N_BLOCKS = 37               # Total amount of blocks textures
MM = 0                      # Something
FULL_SCREEN = True          # Fullscreen parameter


class guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rot = 0
        self.bulb = False
        self.lives = 3
        self.shots = 0
        self.energy = 10
        self.diamonds = 0
        try:
            self.cdfl = time.clock()
        except:
            self.cdfl = time.process_time()

    def update(self, screen):
        if player1.bulb:
            try:
                if time.clock() - self.cdfl > 5:
                    self.cdfl = time.clock()
                    self.energy -= 1
            except:
                if time.process_time() - self.cdfl > 2:
                    self.cdfl = time.process_time()
                    self.energy -= 1

            if self.energy > 0:
                if self.rot == 1:
                    px = player1.x + 130
                    py = player1.y + 25
                    for item in arrGhosts:
                        if math.sqrt((item.x - px) * (item.x - px) + (item.y - py) * (item.y - py)) < 150:
                            item.x = -10000
                            item.y = -10000

                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x + 50 + i, player1.y + int(i / 2) - j + 30),
                                          (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))  # down

                        for j in range(i // 2):
                            screen.set_at((player1.x + 50 + i, player1.y - j + 30),
                                          (255, 228, 0, 255/2 - (i * j) / 255))  # up

                elif self.rot == 3:
                    px = player1.x - 80
                    py = player1.y + 25
                    for item in arrGhosts:
                        if math.sqrt((item.x - px) * (item.x - px) + (item.y - py) * (item.y - py)) < 150:
                            item.x = -10000
                            item.y = -10000

                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x - i + 10, player1.y - int(i / 2) +
                                           j + 30), (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))

                        for j in range(i // 2):
                            screen.set_at(
                                (player1.x - i + 10, player1.y + j + 30), (255, 228, 0, 255/2 - (i * j) / 255))

                elif self.rot == 0:
                    px = player1.x + 25
                    py = player1.y - 80
                    for item in arrGhosts:
                        if math.sqrt((item.x - px) * (item.x - px) + (item.y - py) * (item.y - py)) < 150:
                            item.x = -10000
                            item.y = -10000

                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x + int(i / 2) - j + 18, player1.y - i),
                                          (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))

                        for j in range(i // 2):
                            screen.set_at(
                                (player1.x - j + 20, player1.y - i), (255, 228, 0, 255/2 - (i * j) / 255))

                elif self.rot == 2:
                    px = player1.x + 25
                    py = player1.y + 130
                    for item in arrGhosts:
                        if math.sqrt((item.x - px) * (item.x - px) + (item.y - py) * (item.y - py)) < 150:
                            item.x = -10000
                            item.y = -10000

                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x + int(i / 2) - j + 18, player1.y + i + 30),
                                          (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))

                        for j in range(i // 2):
                            screen.set_at((player1.x - j + 23, player1.y + i + 30),
                                          (255, 228, 0, 255/2 - (i * j) / 255))


def add_ghosts():
    if (randint(0, 80) == 1):
        gx = player1.x
        gy = player1.y
        while math.sqrt((gx - player1.x) * (gx - player1.x) + (gy - player1.y) * (gy - player1.y)) < 300:
            gx = randint(0, SIZE[0])
            gy = randint(0, SIZE[1])

        if (gx > player1.x):
            arrGhosts.append(ghost(gx, gy, 'left'))
        else:
            arrGhosts.append(ghost(gx, gy, 'right'))


def ghosts_update(screen):
    for item in arrGhosts:
        item.update(player1)
        if (item.side == 'left'):
            screen.blit(ghost_left, (item.x, item.y))
        else:
            screen.blit(ghost_right, (item.x, item.y))

        if (item.x > player1.x):
            item.side = 'left'
        else:
            item.side = 'right'


def title_screen(screen):
    if block_pos == 0:
        screen.blit(title0, (0, 0))
    elif block_pos == 1:
        screen.blit(title1, (0, 0))
    elif block_pos == 2:
        screen.blit(title2, (0, 0))



def pick(N, m):
    try:
        if mapp[(player1.y) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] == N:
            mapp[(player1.y) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] = m
            return 1
        else:
            return 0
    except:
        return 0


def lever():
    try:
        if mapp[(player1.y) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] == 30 or mapp[(player1.y) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] == 31 or mapp[(player1.y) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] == 32:
            for y in range(SIZE[1] // BLOCK_SIZE):
                for x in range(SIZE[0] // BLOCK_SIZE):
                    if mapp[y, x] == 33:
                        mapp[y, x] = 4
            mapp[(player1.y) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] += 4

    except:
        pass


def checkdamage(arrGhosts, player, cool_down):
    for item in arrGhosts:
        if abs(player.x - item.x) <= 20 and abs(player.y - item.y) <= 20:
            try:
                if time.clock() - cool_down >= 2:
                    player.lives -= 1
                    cool_down = time.clock()
            except:
                if time.process_time() - cool_down >= 2:
                    player.lives -= 1
                    cool_down = time.process_time()

    return cool_down


def keybind():
    global image, STATE, block_pos, i, done, left, right, up, down, mapp, MM, screen, TIME_TO_UPDATE
    if i.type == pygame.QUIT:
        done = True

    elif i.type == pygame.MOUSEBUTTONDOWN and STATE == 'create':
        if i.button == 1:
            bx = pygame.mouse.get_pos()[0] // BLOCK_SIZE
            by = pygame.mouse.get_pos()[1] // BLOCK_SIZE
            if mapp[by, bx] == N_BLOCKS:
                mapp[by, bx] = 0
            else:
                mapp[by, bx] += 1

        elif i.button == 3:
            bx = pygame.mouse.get_pos()[0] // BLOCK_SIZE
            by = pygame.mouse.get_pos()[1] // BLOCK_SIZE
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
            elif STATE == 'create':
                bx = pygame.mouse.get_pos()[0] // BLOCK_SIZE
                by = pygame.mouse.get_pos()[1] // BLOCK_SIZE
                mapp[by, bx] = 0

            else:
                if player1.bulb:
                    player1.bulb = False
                else:
                    TIME_TO_UPDATE = True
                    try:
                        player1.cdfl = time.process_time()
                    except:
                        player1.cdfl = time.clock()
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
                player1.rot = 0
                image = image_back
            elif i.key == pygame.K_s:
                down = True
                player1.rot = 2
                image = image_front
            elif i.key == pygame.K_a:
                left = True
                player1.rot = 3
                image = image_left
            elif i.key == pygame.K_d:
                right = True
                player1.rot = 1
                image = image_right
            elif i.key == pygame.K_h:
                if MM != 0:
                    MM -= 1
                mapp = arrMap[MM]
            elif i.key == pygame.K_j:
                if MM == 5:
                    MM = 0
                else:
                    MM += 1
                mapp = arrMap[MM]

    elif i.type == pygame.KEYUP:
        if i.key == pygame.K_w:
            up = False
        elif i.key == pygame.K_s:
            down = False
        elif i.key == pygame.K_a:
            left = False
        elif i.key == pygame.K_d:
            right = False


def drawhearts(lives):
    for i in range(lives):
        screen.blit(heart, (10 + i * 60, 10))


def drawenergy(energy):
    for i in range(energy):
        screen.blit(batt, (10 + i * 60, 70))


def drawcrystals(count):
    for i in range(count):
        screen.blit(crys, (10 + i * 60, 130))


if __name__ == "__main__":
    pygame.init()
    if FULL_SCREEN:
        screen_ = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    else:
        screen_ = pygame.display.set_mode(SIZE)
    screen_.fill(BG_COLOR)

    screen = pygame.Surface(SIZE, pygame.SRCALPHA)

    try:
        arrMap = np.load('map.npy')
        mapp = arrMap[0]
    except:
        mapp = np.zeros((SIZE[1] // BLOCK_SIZE, SIZE[0] // BLOCK_SIZE))

    image_back = pygame.image.load('textures/guard0.png')
    image_right = pygame.image.load('textures/guard1.png')
    image_front = pygame.image.load('textures/guard2.png')
    image_left = pygame.image.load('textures/guard3.png')
    ghost_right = pygame.image.load('textures/ghost1.png')
    ghost_left = pygame.image.load('textures/ghost2.png')
    image = image_front

    try:
        cool_down = time.clock()
        cdfl = time.clock()
    except:
        cool_down = time.process_time()
        cdfl = time.process_time()

    fl = []
    fl.append(pygame.image.load('textures/floor.png'))
    fl.append(pygame.image.load('textures/floor2.png'))
    fl.append(pygame.image.load('textures/floor3.png'))
    fl.append(pygame.image.load('textures/door.png'))
    for i in range(15):
        fl.append(pygame.image.load('textures/block' + str(i + 1) + '.png'))
    fl.append(pygame.image.load('textures/gun.png'))
    fl.append(pygame.image.load('textures/hp.png'))
    fl.append(pygame.image.load('textures/hp2.png'))
    fl.append(pygame.image.load('textures/battery.png'))
    fl.append(pygame.image.load('textures/battery2.png'))
    fl.append(pygame.image.load('textures/diamond2.png'))
    fl.append(pygame.image.load('textures/diamond1.png'))
    fl.append(pygame.image.load('textures/sculpt3.png'))
    fl.append(pygame.image.load('textures/sculpt4.png'))
    fl.append(pygame.image.load('textures/sculpt7.png'))
    fl.append(pygame.image.load('textures/lever1.png'))
    fl.append(pygame.image.load('textures/lever2.png'))
    fl.append(pygame.image.load('textures/lever3.png'))
    fl.append(pygame.image.load('textures/door_locked.png'))
    fl.append(pygame.image.load('textures/lever7.png'))
    fl.append(pygame.image.load('textures/lever6.png'))
    fl.append(pygame.image.load('textures/lever5.png'))
    fl.append(pygame.image.load('textures/chest.png'))
    heart = pygame.image.load('textures/heart.png')
    batt = pygame.image.load('textures/batticon.png')
    crys = pygame.image.load('textures/icondiamond.png')

    title0 = pygame.image.load('textures/title0.png')
    title1 = pygame.image.load('textures/title1.png')
    title2 = pygame.image.load('textures/title2.png')

    player1 = guard(START_X, START_Y)
    fps = 1000
    block_pos = 0
    left, right, up, down = False, False, False, False
    powerups = [19, 20, 21, 22, 23, 24, 25, 30, 31, 32]
    cango = [1, 2, 3, 4] + powerups
    arrGhosts = []
    done = False
    STATE = 'title'
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            keybind()
        try:
            if up == True:
                if mapp[(player1.y - 1) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] in cango and mapp[(player1.y - 1) // BLOCK_SIZE, (player1.x + 39) // BLOCK_SIZE] in cango:
                    player1.y -= SS
            if right == True:
                if mapp[(player1.y) // BLOCK_SIZE, (player1.x + 40) // BLOCK_SIZE] in cango and mapp[(player1.y + 39) // BLOCK_SIZE, (player1.x + 40) // BLOCK_SIZE] in cango:
                    if player1.x > SIZE[0] - 100 and MM != 5:
                        MM += 1
                        mapp = arrMap[MM]
                        player1.x = 10
                        arrGhosts = []
                    player1.x += SS
            if down == True:
                if mapp[(player1.y + 40) // BLOCK_SIZE, (player1.x + 39) // BLOCK_SIZE] in cango and mapp[(player1.y + 40) // BLOCK_SIZE, (player1.x) // BLOCK_SIZE] in cango:
                    player1.y += SS
            if left == True:
                if mapp[(player1.y) // BLOCK_SIZE, (player1.x - 1) // BLOCK_SIZE] in cango and mapp[(player1.y + 39) // BLOCK_SIZE, (player1.x - 1) // BLOCK_SIZE] in cango:
                    if player1.x < 20 and MM != 0:
                        MM -= 1
                        mapp = arrMap[MM]
                        player1.x = SIZE[0] - 30
                        arrGhosts = []
                    player1.x -= SS
        except:
            pass
        
        pygame.time.wait(1000 // fps)
        if STATE == 'title':
            screen.fill(BG_COLOR)
            title_screen(screen)
        elif STATE == 'game':
            cool_down = checkdamage(arrGhosts, player1, cool_down)
            if player1.lives < 1:
                STATE = 'died'
            if player1.lives < 4:
                player1.lives += pick(21, 1) + pick(22, 2)
            if player1.shots < 20:
                player1.shots += 5 * pick(20, 2)
            if player1.energy < 10:
                player1.energy += pick(24, 1) + pick(23, 2)
            player1.diamonds += pick(25, 1)
            lever()
            
            screen_.fill
            build_map(screen_, mapp, fl, MM, SIZE)
            build_map(screen, mapp, fl, MM, SIZE)
            add_ghosts()
            ghosts_update(screen)
            ghosts_update(screen_)
            player1.update(screen)
            screen.blit(image, (player1.x, player1.y))
            drawhearts(player1.lives)
            drawenergy(player1.energy)
            drawcrystals(player1.diamonds)
        elif STATE == 'create':
            build_map(screen, mapp, fl, MM)
            np.save('map', arrMap)
        elif STATE == 'died':
            arrGhosts = []
            player1.lives = 3
            try:
                mapp = np.load('map.npy')
            except:
                mapp = np.zeros((SIZE[1] // BLOCK_SIZE, SIZE[0] // BLOCK_SIZE))
            f3 = pygame.font.SysFont('Pixar One', 48)
            screen.fill(BG_COLOR)
            text3 = f3.render("YOU DIED!", 0, (0, 180, 0))
            screen.blit(text3, (540, 500))
            pygame.display.flip()
            pygame.time.wait(1000)
            STATE = 'title'

        screen_.blit(screen, (0, 0))
        pygame.display.flip()
    pygame.quit()
