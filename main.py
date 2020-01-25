import pygame
import numpy as np
import math

SIZE = (1024, 768)
BG_COLOR = (100, 100, 100)
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
    screen.fill(BG_COLOR)
    pygame.display.update()

    image_back = pygame.image.load(r'guard0.png')
    image_right = pygame.image.load(r'guard1.png')
    image_front = pygame.image.load(r'guard2.png')
    image = image_front

    player1 = guard(START_X, START_Y)
    fps = 240
    left, right, up, down = False, False, False, False

    done = False
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    up = True
                    image = image_back
                elif i.key == pygame.K_s:
                    down = True
                    image = image_front
                elif i.key == pygame.K_a:
                    left = True
                    image = image_right
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
            player1.x += 1
        if up == True:
            player1.y -= 1
        if left == True:
            player1.x -= 1
        if down == True:
            player1.y += 1

        pygame.time.wait(1000 // fps)
        screen.fill(BG_COLOR)
        screen.blit(image, (player1.x, player1.y))
        pygame.display.update()                                                                                                                                                                                                                                                                                                                                                                         

    pygame.quit()
