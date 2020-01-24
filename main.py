import pygame
import numpy as np
import math

SIZE = (600, 600)
CL = (33, 33, 33)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(CL)
    pygame.display.update()
    
    done = False
    while not done:
        for i in pygame.event.get():  # events
            if i.type == pygame.QUIT:
                done = True
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    pass
    
    pygame.quit()
