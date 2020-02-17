import os
import json
import numpy as np
import pygame
import time


class ObjectBlock():
    def __init__(self, blockName):
        states = json.load(open(f'states/blocks/{blockName}.json', 'r'))
        self.tangibility_player = states['tangibility_player']
        self.tangibility_ghosts = states['tangibility_ghosts']
        self.texture = pygame.image.load(
            f'textures/{states["texture"]}')


class ObjectLandscape():
    def __init__(self, landscapeName):
        states = json.load(open(f'states/landscape/{landscapeName}.json', 'r'))
        self.tangibility_player = states['tangibility_player']
        self.tangibility_ghosts = states['tangibility_ghosts']
        self.texture = pygame.image.load(f'textures/{states["texture"]}')


class ObjectGuard():
    def __init__(self):
        self.x = -1
        self.y = -1
        self.texture = {"front": pygame.image.load('textures/guard/guard_front.png'), "back": pygame.image.load(
            'textures/guard/guard_back.png'), "left": pygame.image.load('textures/guard/guard_left.png'), "right": pygame.image.load('textures/guard/guard_right.png')}
        self.flashlight = False
        self.direction = "up"
        self.lives = 3
        self.energy = 4
        self.diamonds = 0
        self.shots = 4
        self.cooldown = time.process_time()
        self.flashlight_cooldown = time.process_time()
        self.current_image = self.texture["front"]
        self.goDirection = (0, 0)


class Button():
    def __init__(self, x, y, width, height, text, textsize, unselbgcolor, unseltextcolor, selbgcolor, seltextcolor, function, *functionargs):
        self.rect = pygame.Rect((x, y, width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.unselected_text_content = pygame.font.Font(
            None, textsize).render(text, 1, unseltextcolor)
        self.unselected_text_color = unseltextcolor
        self.text_size = textsize
        self.unselected_background_color = unselbgcolor
        self.selected_text_content = pygame.font.Font(
            None, textsize).render(text, 1, seltextcolor)
        self.selected_text_color = seltextcolor
        self.selected_background_color = selbgcolor
        self.onclick = function
        self.functionargs = functionargs
        self.selected = False

    def render(self):
        if self.selected == True:
            pygame.draw.rect(screen, self.selected_background_color, self.rect)
            screen.blit(self.selected_text_content, (self.x + self.text_size,
                                                     self.height + self.y - self.text_size))
        elif self.selected == False:
            pygame.draw.rect(
                screen, self.unselected_background_color, self.rect)
            screen.blit(self.unselected_text_content, (self.x + self.text_size,
                                                       self.height + self.y - self.text_size))

    def click(self):
        self.onclick(self.functionargs)


def initfunc():
    pygame.init()
    global options, FPS, SIZE, screen, blocks, landscapes, player, all_maps, gameState, selectedButton, buttons, background
    options = json.load(open('options.json', 'r'))
    FPS = 60
    SIZE = (options['width'], options['height'])
    if options['type'] == 'std':
        screen = pygame.display.set_mode(SIZE)
    elif options['type'] == 'ful':
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    elif options['type'] == 'nof':
        screen = pygame.display.set_mode(SIZE, pygame.NOFRAME)
    screen.fill((0, 0, 0))
    blocks = {block.replace('.json', ''): ObjectBlock(
        block.replace('.json', '')) for block in os.listdir('states/blocks')}
    landscapes = {landscape.replace('.json', ''): ObjectLandscape(
        landscape.replace('.json', '')) for landscape in os.listdir('states/landscape')}
    player = ObjectGuard()
    all_maps = {cur_map[:cur_map.find('.')]: np.load(
        f'maps/{cur_map}') for cur_map in os.listdir('maps')}
    gameState = 'title'
    selectedButton = -1
    buttons = {}
    titleScreenInit()
    background = (50, 50, 50)


def changeState(state):
    global gameState
    gameState = state


def titleScreenInit():
    buttons['StartGame'] = Button(options['width'] // 10, options['height'] // 20 * 2, options['width'] // 10 * 4,
                                  options['height'] // 10 * 1, 'Start game', options['height'] // 15, (50, 50, 50), (0, 180, 0), (180, 180, 180), (0, 180, 0), changeState, 'game')
    buttons['SelectMap'] = Button(options['width'] // 10, options['height'] // 20 * 5, options['width'] // 10 * 4,
                                  options['height'] // 10 * 1, 'Select map to play', options['height'] // 15, (50, 50, 50), (0, 180, 0), (180, 180, 180), (0, 180, 0), changeState, 'selection')
    buttons['CreateMap'] = Button(options['width'] // 10, options['height'] // 20 * 8, options['width'] // 10 * 4,
                                  options['height'] // 10 * 1, 'Create map to play', options['height'] // 15, (50, 50, 50), (0, 180, 0), (180, 180, 180), (0, 180, 0), changeState, 'create')


def titleScreen():
    buttons['StartGame'].render()
    buttons['SelectMap'].render()
    buttons['CreateMap'].render()


def keyCheck():
    global options
    global selectedButton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if gameState == 'title':
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_s or event.key == pygame.K_DOWN or (event.key == pygame.K_TAB and not pygame.key.get_mods() & pygame.KMOD_LSHIFT):
                    if selectedButton != -1:
                        buttons[selectedButton].selected = False
                    if selectedButton == -1:
                        selectedButton = list(buttons.keys())[0]
                    else:
                        if list(buttons.keys()).index(selectedButton) + 1 < len(list(buttons.keys())):
                            selectedButton = list(buttons.keys())[list(
                                buttons.keys()).index(selectedButton) + 1]
                        else:
                            selectedButton = list(buttons.keys())[0]
                    buttons[selectedButton].selected = True

                if event.key == pygame.K_w or event.key == pygame.K_UP or (event.key == pygame.K_TAB and pygame.key.get_mods() & pygame.KMOD_LSHIFT):
                    if selectedButton != -1:
                        buttons[selectedButton].selected = False
                    if selectedButton == -1:
                        selectedButton = list(buttons.keys())[-1]
                    else:
                        if list(buttons.keys()).index(selectedButton) - 1 >= 0:
                            selectedButton = list(buttons.keys())[list(
                                buttons.keys()).index(selectedButton) - 1]
                        else:
                            selectedButton = list(buttons.keys())[-1]
                    buttons[selectedButton].selected = True

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    buttons[selectedButton].click()


initfunc()
while True:
    screen.fill(background)
    keyCheck()
    if gameState == 'title':
        titleScreen()
    elif gameState == 'game':
        draw_map()
    pygame.display.update()
    pygame.time.wait(1000 // FPS)
