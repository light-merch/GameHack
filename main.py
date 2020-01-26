import pygame
import numpy as np
import math
import datetime
from random import randint
import time

from map_builder import map_builder

SIZE = (1280, 1024)
BG_COLOR = (50, 50, 50)
START_X = 500
START_Y = 400
SS = 4  # Step Size
BSS = 1
SIZE_BLOCK = 50
N_BLOCKS = 33
MM = 0
TIME_TO_UPDATE = False


class bullet():
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.d = 4
        self.heading = heading

    def update(self):
        pass

class ghost():
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def update(self):
        c = 0
        dx = player1.x - self.x
        dy = player1.y - self.y
        angle = math.atan2(dy, dx)
        dx2 = math.cos(angle) * BSS
        dy2 = math.sin(angle) * BSS
        self.x += dx2
        self.y += dy2
    

class guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rot = 0
        self.bulb = False
        self.lives = 3
        self.shots = 0
        self.energy = 5
        self.diamonds = 0
        try:
            self.cdfl = time.clock()
        except:
            self.cdfl = time.process_time()

    def update(self, screen):
        pygame.draw.circle(screen, (255,255,255), (player1.x, player1.y),10)
        pygame.draw.circle(screen, (127,127,127), (player1.x + 40, player1.y),10)
        pygame.draw.circle(screen, (63,63,63), (player1.x, player1.y + 40),10)
        pygame.draw.circle(screen, (0,0,0), (player1.x + 40, player1.y + 40),10)
        if player1.bulb:
            try:
                if time.clock() - self.cdfl > 5:
                    self.cdfl = time.clock()
                    self.energy -= 1
            except:
                if time.process_time() - self.cdfl > 5:
                    self.cdfl = time.process_time()
                    self.energy -= 1
            if self.energy > 0:
                if self.rot == 1:
                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x + 50 + i, player1.y + int(i / 2) - j + 30), (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))  # down

                        for j in range(i // 2):
                            screen.set_at((player1.x + 50 + i, player1.y - j + 30), (255, 228, 0, 255/2 - (i *  j) / 255)) # up

                elif self.rot == 3:
                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x - i + 10, player1.y - int(i / 2) + j + 30), (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))

                        for j in range(i // 2):
                            screen.set_at((player1.x - i + 10, player1.y + j + 30), (255, 228, 0, 255/2 - (i *  j) / 255))

                elif self.rot == 0:
                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x + int(i / 2) - j + 18, player1.y - i), (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))  # down

                        for j in range(i // 2):
                            screen.set_at((player1.x - j + 20, player1.y - i), (255, 228, 0, 255/2 - (i *  j) / 255)) # up

                elif self.rot == 2:
                    for i in range(250):
                        for j in range(i // 2):
                            screen.set_at((player1.x + int(i / 2) - j + 18, player1.y + i + 30), (255, 228, 0, 255/2 - (i * (255/2 - j)) / 255))  # down

                        for j in range(i // 2):
                            screen.set_at((player1.x - j + 23, player1.y + i + 30), (255, 228, 0, 255/2 - (i *  j) / 255)) # up


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
        item.update()
        if (item.side == 'left'):
            screen.blit(ghost_left, (item.x, item.y))
        else:
            screen.blit(ghost_right, (item.x, item.y))


def title_screen(screen):
    if block_pos == 0:
        pygame.draw.rect(screen, (255, 255, 255), (400, 100, 410, 100))
    elif block_pos == 1:
        pygame.draw.rect(screen, (255, 255, 255), (400, 210, 415, 150))
    elif block_pos == 2:
        pygame.draw.rect(screen, (255, 255, 255), (400, 470, 410, 110))

    f2 = pygame.font.SysFont('Pixar One', 60)
    text2 = f2.render("START", 0, (0, 180, 0))
    screen.blit(text2, (515, 100))

    f4 = pygame.font.SysFont('Pixar One', 48)
    text4 = f4.render("NEW MAP", 0, (0, 180, 0))
    screen.blit(text4, (495, 250))

    f3 = pygame.font.SysFont('Pixar One', 48)
    text3 = f3.render("EXIT", 0, (0, 180, 0))
    screen.blit(text3, (540, 500))

def pick(N):
    if mapp[(player1.y) // SIZE_BLOCK, (player1.x) // SIZE_BLOCK] == N:
        mapp[(player1.y) // SIZE_BLOCK, (player1.x) // SIZE_BLOCK] = 1
        return 1
    else:
        return 0

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
            elif STATE == 'create':
                bx = pygame.mouse.get_pos()[0] // SIZE_BLOCK
                by = pygame.mouse.get_pos()[1] // SIZE_BLOCK
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
        screen.blit(heart,(10 + i * 60,10))
    
def drawenergy(energy):
    for i in range(energy):
        screen.blit(batt,(10 + i * 60,70))

if __name__ == "__main__":
    pygame.init()
    # screen_ = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    screen_ = pygame.display.set_mode(SIZE, pygame.NOFRAME)
    screen_.fill(BG_COLOR)
    
    screen = pygame.Surface(SIZE, pygame.SRCALPHA)
    
    try:
        arrMap = np.load('neww.npy')
        mapp = arrMap[0]
    except:
        mapp = np.zeros((SIZE[1] // SIZE_BLOCK, SIZE[0] // SIZE_BLOCK))

    image_back = pygame.image.load(r'guard0.png')
    image_right = pygame.image.load(r'guard1.png')
    image_front = pygame.image.load(r'guard2.png')
    image_left = pygame.image.load(r'guard3.png')
    ghost_right = pygame.image.load(r'ghost1.png')
    ghost_left = pygame.image.load(r'ghost2.png')
    image = image_front
    try:
        cool_down = time.clock()
        cdfl = time.clock()
    except:
        cool_down = time.process_time()
        cdfl = time.process_time()


    fl = []
    fl.append(pygame.image.load(r'floor.png'))
    fl.append(pygame.image.load(r'floor2.png'))
    fl.append(pygame.image.load(r'floor3.png'))
    fl.append(pygame.image.load(r'door.png'))

    for i in range(15):
        fl.append(pygame.image.load(f'block{i + 1}.png'))

    fl.append(pygame.image.load(r'gun.png'))
    fl.append(pygame.image.load(r'hp.png'))
    fl.append(pygame.image.load(r'hp2.png'))
    fl.append(pygame.image.load(r'battery.png'))
    fl.append(pygame.image.load(r'battery2.png'))
    fl.append(pygame.image.load(r'diamond2.png'))
    fl.append(pygame.image.load(r'diamond1.png'))
    fl.append(pygame.image.load(r'sculpt3.png'))
    fl.append(pygame.image.load(r'sculpt4.png'))
    fl.append(pygame.image.load(r'sculpt7.png'))
    fl.append(pygame.image.load(r'lever1.png'))
    fl.append(pygame.image.load(r'lever2.png'))
    fl.append(pygame.image.load(r'lever3.png'))
    fl.append(pygame.image.load(r'door_locked.png'))

    heart = pygame.image.load(r'heart.jpg')
    batt = pygame.image.load(r'att.png')

    player1 = guard(START_X, START_Y)
    fps = 1000
    block_pos = 0
    left, right, up, down = False, False, False, False
    powerups = [19, 20, 21, 22, 23, 24, 25]
    cango = [0, 1, 2, 3, 4] + powerups
    arrGhosts = []

    done = False
    STATE = 'title'
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            keybind()
        if up == True:
            if mapp[(player1.y - 1) // SIZE_BLOCK, (player1.x) // SIZE_BLOCK] in cango and mapp[(player1.y - 1) // SIZE_BLOCK, (player1.x + 39) // SIZE_BLOCK] in cango:
                player1.y -= SS
        if right == True: 
            if mapp[(player1.y) // SIZE_BLOCK, (player1.x + 40) // SIZE_BLOCK] in cango and mapp[(player1.y + 39) // SIZE_BLOCK, (player1.x + 40) // SIZE_BLOCK] in cango:
                if player1.x > SIZE[0] - 100 and MM != 5:
                    MM += 1
                    mapp = arrMap[MM]
                    player1.x = 10
                player1.x += SS
        if down == True:
            if mapp[(player1.y + 40) // SIZE_BLOCK, (player1.x + 39) // SIZE_BLOCK] in cango and mapp[(player1.y + 40) // SIZE_BLOCK, (player1.x) // SIZE_BLOCK] in cango:
                player1.y += SS
        if left == True:
            if mapp[(player1.y) // SIZE_BLOCK, (player1.x - 1) // SIZE_BLOCK] in cango and mapp[(player1.y + 39) // SIZE_BLOCK, (player1.x - 1) // SIZE_BLOCK] in cango:
                if player1.x < 20 and MM != 0:
                    MM -= 1
                    mapp = arrMap[MM]
                    player1.x = SIZE[0] - 10
                player1.x -= SS

        
        
        pygame.time.wait(1000 // fps)
        screen.fill(BG_COLOR)
        if STATE == 'title':
            title_screen(screen)
        elif STATE == 'game':
            cool_down = checkdamage(arrGhosts, player1, cool_down)
            if player1.lives < 1:
                STATE = 'died'
            if player1.lives < 4:
                player1.lives += pick(21)
            if player1.lives < 4:
                player1.lives += pick(22)

            if player1.shots < 20:
                player1.shots += 5 * pick(20)

            if player1.energy < 100:
                player1.energy += 10 * pick(22) + 10 * pick(23)
            
            screen_.fill
            map_builder(screen_, mapp, fl)
            map_builder(screen, mapp, fl)
            add_ghosts()
            ghosts_update(screen)
            ghosts_update(screen_)

            player1.update(screen)
            #TIME_TO_UPDATE = False

            screen.blit(image, (player1.x, player1.y))
            # screen_.blit(screen, SIZE)
            # pygame.display.flip()
            drawhearts(player1.lives)
            drawenergy(player1.energy)
        elif STATE == 'create':
            map_builder(screen, mapp, fl)
            np.save('neww', arrMap)
        elif STATE == 'died':
            arrGhosts = []
            player1.lives = 3
            try:
                mapp = np.load('main.npy')
            except:
                mapp = np.zeros((SIZE[1] // SIZE_BLOCK, SIZE[0] // SIZE_BLOCK))

            if randint(1, 100) != 1:
                f3 = pygame.font.SysFont('Pixar One', 48)
                screen.fill(BG_COLOR)
                text3 = f3.render("YOU DIED!", 0, (0, 180, 0))
                screen.blit(text3, (540, 500))
                pygame.display.update()
                pygame.time.wait(1000)
                STATE = 'title'
            else:
                screen.blit(deathpage, (0, 0))

        # screen.fill(BG_COLOR)
        screen_.blit(screen, (0, 0))
        pygame.display.flip()
        # pygame.display.update()

    pygame.quit()
