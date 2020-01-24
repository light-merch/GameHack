import pygame
import time
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
    image = pygame.image.load(r'guard2.png')
    
    player1 = guard(START_X, START_Y)
    # player2= guard(100, 200)


    done = False
    while not done:
        screen.fill(BG_COLOR)
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    print('up')
                    player1.y -= 10

                if i.key == pygame.K_s:
                    print('down')
                    player1.y += 10

                if i.key == pygame.K_a:
                    print('left')
                    player1.x -= 10

                if i.key == pygame.K_d:
                    print('right')
                    player1.x += 10
        
        screen.blit(image, (player1.x, player1.y))
        pygame.display.update()
        print('hey')

    pygame.quit()
