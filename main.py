import pygame
import numpy as np
import math

SIZE = (1024, 768)
CL = (33, 33, 33)
BG_COLOR = (249, 166, 2)
START_X = 500
START_Y = 400


class agent():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class guard():
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(CL)
    pygame.display.update()

    player1 = guard(START_X, START_Y)
    # player2= guard(100, 200)
    left, right, up, down = False, False, False, False

    done = False
    while not done:
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    up = True
                elif i.key == pygame.K_s:
                    down = True
                elif i.key == pygame.K_a:
                    left = True
                elif i.key == pygame.K_d:
                    right = True
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
            player1.x += 10
        if up == True:
            player1.y -= 10
        if left == True:
            player1.x -= 10
        if down == True:
            player1.y += 10

        pygame.time.wait(1000 // 60)
        pygame.draw.circle(screen, BG_COLOR, (player1.x, player1.y), 10, 0)
        pygame.display.update()

    pygame.quit()
