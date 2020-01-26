import pygame
import numpy as np
import math
import datetime
from random import randint

SIZE = (1280, 1024)
BG_COLOR = (50, 50, 50)
START_X = 500
START_Y = 400
SS = 2  # Step Size
SIZE_BLOCK = 50
N_BLOCKS = 32

def map_builder(screen, mapp, floors):
    for i in range(SIZE[0] // SIZE_BLOCK):
        pygame.draw.line(screen, (255, 255, 255), [i * SIZE_BLOCK, 0], [i * SIZE_BLOCK, SIZE[1]], 2)

    for i in range(SIZE[1] // SIZE_BLOCK):
        pygame.draw.line(screen, (255, 255, 255), [0, i * SIZE_BLOCK], [SIZE[0], i * SIZE_BLOCK], 2)

    for y in range(SIZE[1] // SIZE_BLOCK):
        for x in range(SIZE[0] // SIZE_BLOCK):
            for i in range(N_BLOCKS):
                if mapp[y, x] == i + 1:
                    screen.blit(floors[i], (x * SIZE_BLOCK, y * SIZE_BLOCK))
