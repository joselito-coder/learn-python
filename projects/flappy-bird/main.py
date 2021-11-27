import random  # used to generate randomness
import sys  # we can use sys.exit to exit
import pygame
from pygame.locals import *

# Global variables
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
GROUNDY = SCREENHEIGHT * 0.8


def welcomeScreen():
    """
    Shows the users Welcome Screen
    """
    playerX = int(SCREENWIDTH/5)
    playerY = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()))/2
    messageX = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()))/2
    messageY = int(SCREENHEIGHT * 0.13)
    baseX = 0

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button , close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses the up key then start the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            else:
                # blitting the images
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerX, playerY))
                SCREEN.blit(GAME_SPRITES['base'], (baseX, GROUNDY))
                SCREEN.blit(GAME_SPRITES['message'], (messageX, messageY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def getRandomPipe():
    """
    generate positions of two pipes (one straight one rotated) for blitting on the screen
    """

    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT -
                                   GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper Pipe
        {'x': pipeX, 'y': y2}  # lower Pipe
    ]
    return pipe


def isCollide(playerx, playery, upperPipes, lowerPipes):

    if playery > GROUNDY - 25 or playery < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if ( playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()  ):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y'] and abs(playerx - pipe['x'])  < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    return False


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0 

    # Create 2 pipes for blitting on the screen

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # My list of uper pipes
    upperPipes = [
        { 'x': SCREENWIDTH + 200, 'y':newPipe1[0]['y'] },
        { 'x': SCREENWIDTH + 200 +(SCREENWIDTH/2), 'y':newPipe2[0]['y'] }
    ]

    # My list of lower pipes
    lowerPipes = [
        { 'x': SCREENWIDTH + 200, 'y':newPipe1[1]['y'] },
        { 'x': SCREENWIDTH + 200 +(SCREENWIDTH/2), 'y':newPipe2[1]['y'] }
    ]

    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # it is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN  and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()
        
        crashTest = isCollide(playerx, playery,upperPipes,lowerPipes) # this function will return true if you crashed

        if crashTest:
            return

        # Check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() /2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY,GROUNDY - playery - playerHeight)

        #  move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe['x']  += pipeVelX
            lowerPipe['x']  += pipeVelX

        # Add a new pipe when the first pipe is about to cross leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'],upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()

        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)



if __name__ == "__main__":
    # Main point in which the game will run
    pygame.init() # init all pygame modules

    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy bird by codeWithHarry")

    GAME_SPRITES['numbers'] = (
        pygame.image.load('./gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('./gallery/sprites/9.png').convert_alpha()
    )
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =  pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
    
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.mp3')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.mp3')

    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()

    # Game loop
    while True:
        welcomeScreen()
        mainGame()
