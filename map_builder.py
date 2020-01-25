import pygame
import numpy as np
import math

SIZE = (1024, 768)
BG_COLOR = (50, 50, 50)
START_X = 500
START_Y = 400
SIZE_BLOCK = 50
sc = pygame.display.set_mode((300,200))
sc.fill((255, 255, 255))
X_line = 0
Y_line = 0


class ghost():
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

    floor = pygame.image.load(r'floor.png')

    for i in range(SIZE[0] // 10):
        pygame.draw.line(screen, (255, 255, 255), [X_line, 0], [X_line, SIZE[1]], 3)
        X_line += 50

    for i in range(SIZE[1] // 10):
        pygame.draw.line(screen, (255, 255, 255), [0, Y_line], [SIZE[0], Y_line], 3)
        Y_line += 50
    pygame.display.update()

    player1 = guard(START_X, START_Y)
    fps = 240
    left, right, up, down = False, False, False, False

    bx, by = 0, 0
    done = False
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    bx = pygame.mouse.get_pos()[0] // SIZE_BLOCK * SIZE_BLOCK
                    by = pygame.mouse.get_pos()[0] // SIZE_BLOCK * SIZE_BLOCK


            elif i.type == pygame.KEYDOWN:
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
            player1.x += 1
        if up == True:
            player1.y -= 1
        if left == True:
            player1.x -= 1
        if down == True:
            player1.y += 1

        pygame.time.wait(1000 // fps)

        for i in range(SIZE[0] // 10):
            pygame.draw.line(screen, (255, 255, 255), [X_line, 0], [X_line, SIZE[1]], 3)
            X_line += 50

        for i in range(SIZE[1] // 10):
            pygame.draw.line(screen, (255, 255, 255), [0, Y_line], [SIZE[0], Y_line], 3)
            Y_line += 50

        #screen.blit(floor, (bx, by))
        pygame.display.update()

    pygame.quit()
