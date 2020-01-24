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
    
    pygame.draw.circle(screen, BG_COLOR, (player1.x, player1.y), 10, 0)
    pygame.display.update()
                        
    done = False
    while not done:
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    print('up')
                    player1.y -= 10
                    pygame.draw.circle(screen, BG_COLOR, (player1.x, player1.y), 10, 0)
                    pygame.display.update()

                elif i.key == pygame.K_s:
                    print('down')
                    player1.y += 10
                    pygame.draw.circle(screen, BG_COLOR, (player1.x, player1.y), 10, 0)
                    pygame.display.update()

                elif i.key == pygame.K_a:
                    print('left')
                    player1.x -= 10
                    pygame.draw.circle(screen, BG_COLOR, (player1.x, player1.y), 10, 0)
                    pygame.display.update()

                elif i.key == pygame.K_d:
                    print('right')
                    player1.x += 10
                    pygame.draw.circle(screen, BG_COLOR, (player1.x, player1.y), 10, 0)
                    pygame.display.update()

        

    pygame.quit()
