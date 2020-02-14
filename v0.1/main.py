import os           # os module is required to load textures and maps
import json         # json module is required to load options
import numpy as np  # numpy is required to fast working with game map
import pygame       # pygame is required to work with game graphics
import time         # time is required to cooldowns conrol and time conrol


# class of block
class ObjectBlock():
    def __init__(self, blockName):
        # load states from json file
        states = json.load(open(f'states/blocks/{blockName}.json', 'r'))
        # will player collide this block
        self.tangibility_player = states['tangibility_player']
        # will ghosts collide this block
        self.tangibility_ghosts = states['tangibility_ghosts']
        self.texture = pygame.image.load(
            f'textures/{states["texture"]}')   # load block texture


# class of landscape element
class ObjectLandscape():
    def __init__(self, landscapeName):
        # load states from json file
        states = json.load(open(f'states/landscape/{landscapeName}.json', 'r'))
        # will player collide this landscape elem
        self.tangibility_player = states['tangibility_player']
        # will ghosts collide this landscape elem
        self.tangibility_ghosts = states['tangibility_ghosts']
        # load landscape elem texture
        self.texture = pygame.image.load(f'textures/{states["texture"]}')


# player class
class ObjectGuard():
    def __init__(self):
        # player x coordinate
        self.x = -1
        # player y coordinate
        self.y = -1
        self.texture = {"front": pygame.image.load('textures/guard/guard_front.png'), "back": pygame.image.load(
            'textures/guard/guard_back.png'), "left": pygame.image.load('textures/guard/guard_left.png'), "right": pygame.image.load('textures/guard/guard_right.png')}  # player textures
        # flashlight state
        self.flashlight = False
        # direction of player
        self.direction = "up"
        # player lives count
        self.lives = 3
        # flashlight energy count
        self.energy = 4
        # diamonds count
        self.diamonds = 0
        # player shots count
        self.shots = 4
        # damage coolldown
        self.cooldown = time.process_time()
        # flashlight cooldown
        self.flashlight_cooldown = time.process_time()
        # current texture
        self.current_image = self.texture["front"]
        self.goDirection = (0,0)

class Button():
    def __init__(self, x, y, width, height, text, textsize, bgcolor, textcolor, function, *functionargs):
        self.rect = pygame.Rect((x, y, width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_content = pygame.font.Font(
            None, textsize).render(text, 1, textcolor)
        self.text_color = textcolor
        self.text_size = textsize
        self.background_color = bgcolor
        self.onclick = function
        self.functionargs = functionargs
        self.selected = False

    def render(self):
        pygame.draw.rect(screen, self.background_color, self.rect)
        if self.selected == True:
            pygame.draw.rect(screen, self.text_color, self.rect, 8)
        screen.blit(self.text_content, (self.x + self.text_size,
                                        self.height + self.y - self.text_size))

    def click(self):
        self.onclick(self.functionargs)

def initfunc():
    pygame.init()
    global options
    options = json.load(open('options.json', 'r'))
    global FPS
    FPS = 60
    global SIZE
    SIZE = (options['width'], options['height'])
    global screen
    if options['type'] == 'std':
        screen = pygame.display.set_mode(SIZE)
    elif options['type'] == 'ful':
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    elif options['type'] == 'nof':
        screen = pygame.display.set_mode(SIZE, pygame.NOFRAME)
    screen.fill((0,0,0))
    global blocks
    blocks = {block.replace('.json', ''): ObjectBlock(
        block.replace('.json', '')) for block in os.listdir('states/blocks')}

    global landscapes
    landscapes = {landscape.replace('.json', ''): ObjectLandscape(
        landscape.replace('.json', '')) for landscape in os.listdir('states/landscape')}

    global player
    player = ObjectGuard()

    global all_maps
    all_maps = {cur_map[:cur_map.find('.')]: np.load(
        f'maps/{cur_map}') for cur_map in os.listdir('maps')}
    
    global gameState
    gameState = 'title'

    global selectedButton
    selectedButton = -1

    global buttons
    buttons = {}

    titleScreenInit()


def changeState(state):
    global gameState
    gameState = state


def titleScreenInit():
    global selectedButton
    buttons['StartGame'] = Button(options['width'] // 10, options['height'] // 20 * 2, options['width'] // 10 * 4,
                                  options['height'] // 10 * 1, 'Start game', options['height'] // 15, (0, 0, 64), (191, 191, 0), changeState,'game')
    buttons['SelectMap'] = Button(options['width'] // 10, options['height'] // 20 * 5, options['width'] // 10 * 4,
                                  options['height'] // 10 * 1, 'Select map to play', options['height'] // 15, (0, 0, 64), (191, 191, 0), changeState,'selection')
    buttons['CreateMap'] = Button(options['width'] // 10, options['height'] // 20 * 8, options['width'] // 10 * 4,
                                  options['height'] // 20 * 2, 'Create map to play', options['height'] // 15, (0, 0, 64), (191, 191, 0), changeState,'create')
    selectedButton = list(buttons.keys())[0]
    buttons[selectedButton].selected = True

def titleScreen():
    buttons['StartGame'].render()
    buttons['SelectMap'].render()
    buttons['CreateMap'].render()


def keyCheck():global options
    global selectedButton,keyCooldown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if gameState == 'title':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    buttons[selectedButton].selected = False
                    if list(buttons.keys()).index(selectedButton) + 1 < len(list(buttons.keys())):
                        selectedButton = list(buttons.keys())[list(buttons.keys()).index(selectedButton) + 1]
                    else:
                        selectedButton = list(buttons.keys())[0]
                    buttons[selectedButton].selected = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    buttons[selectedButton].selected = False
                    if list(buttons.keys()).index(selectedButton) - 1 >= 0:
                        selectedButton = list(buttons.keys())[list(buttons.keys()).index(selectedButton) - 1]
                    else:
                        selectedButton = list(buttons.keys())[-1]
                    buttons[selectedButton].selected = True
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    buttons[selectedButton].click()
initfunc()
while True:
    keyCheck()
    if gameState == 'title':
        titleScreen()
    elif gameState == 'game':
        draw_map
    pygame.display.update()
    pygame.time.wait(1000 // FPS)