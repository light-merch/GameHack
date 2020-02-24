import datetime
from random import randint
import math

import pygame
import numpy as np


SS = 2                      # Step Size
SIZE_BLOCK = 50
N_BLOCKS = 37


def build_map(screen, mapp, floors, N, SIZE):
    for i in range(SIZE[0] // SIZE_BLOCK):
        pygame.draw.line(screen, (255, 255, 255), [i * SIZE_BLOCK, 0], [i * SIZE_BLOCK, SIZE[1]], 2)

    for i in range(SIZE[1] // SIZE_BLOCK):
        pygame.draw.line(screen, (255, 255, 255), [0, i * SIZE_BLOCK], [SIZE[0], i * SIZE_BLOCK], 2)

    for y in range(SIZE[1] // SIZE_BLOCK):
        for x in range(SIZE[0] // SIZE_BLOCK):
            screen.blit(floors[mapp[y, x]], (x * SIZE_BLOCK, y * SIZE_BLOCK))

    # pygame.image.save(screen, 'screen' + str(N) + '.png')
