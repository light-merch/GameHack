import math
import datetime
from random import randint

import pygame
import numpy as np


BSS = 1


class bullet():
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.d = 4
        self.heading = heading

    def update(self):
        if self.heading == 0:
            pass
        elif self.heading == 1:
            pass
        elif self.heading == 2:
            pass
        elif self.heading == 3:
            self


class ghost():
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def update(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        angle = math.atan2(dy, dx)
        dx2 = math.cos(angle) * BSS
        dy2 = math.sin(angle) * BSS
        self.x += dx2
        self.y += dy2
