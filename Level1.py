######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (level 1.py)                       #
#   CIS 4930                                         #
######################################################

import pygame
from pygame.locals import *
import importlib
import sys

avatar = pygame.image.load("Images/Mario.png")
first_castle = pygame.image.load("Images/First Castle.png")
castle = pygame.image.load("Images/Castle.png")
bottom_brick = pygame.image.load("Images/Ground Block.png")
coin = pygame.image.load("Images/Coin.jpg")
bottom_brick = pygame.image.load("Images/Ground Block.png")
brick_block = pygame.image.load("Images/Brick Block.png")
bush = pygame.image.load("Images/Bush.png")
hill = pygame.image.load("Images/Hill.png")
pipe = pygame.image.load("Images/pipe.png")
little_cloud = pygame.image.load("Images/Little Cloud.png")
clouds = pygame.image.load("Images/Big Cloud.png")
mystery = pygame.image.load("Images/Mystery Block.png")
jump_block = pygame.image.load("Images/Jump Block.png")
finish_block = pygame.image.load("Images/Finish Block.png")
flag = pygame.image.load("Images/Flagpole.png")
mystery_block = pygame.image.load("Images/Mystery Block.png")

grass3 = pygame.image.load("Images/Grass/Grass3.png")
grass4 = pygame.image.load("Images/Grass/Grass4.png")
grass5 = pygame.image.load("Images/Grass/Grass5.png")
grass6 = pygame.image.load("Images/Grass/Grass6.png")
grass7 = pygame.image.load("Images/Grass/Grass7.png")
grass8 = pygame.image.load("Images/Grass/Grass8.png")

backColor = (102,178,255)

clock = pygame.time.Clock()
pygame.display.set_caption("Super Python Bros.")


def drawBricks():
    for i in range(0, 16):
        screen.blit(bottom_brick, (54*i, height - 54))
        screen.blit(bottom_brick, (54*i, height - 2*54))

    pygame.display.flip()


def print_Back(x, height):
    screen.fill(backColor)
    for i in range(0, 79):
        if i == 12 or i == 24 or i == 42:
            screen.blit(bush, (54 * i + x, height - 2 * 54 - 103))
        if i == 0 or i == 16 or i == 48:
            screen.blit(hill, (54 * i + x, height - 2 * 54 - 128))
        if i == 29 or i == 38 or i == 46 or i == 57:
            screen.blit(pipe, (54 * i + x, height - 2 * 54 - 120))
        if i == 20 or i == 22:
            screen.blit(brick_block, (54 * i + x, height - 2 * 54 - 150))
        if i == 19 or i == 21 or i == 23:
            screen.blit(brick_block, (54 * i + x, height - 2 * 54 - 150))
        if i == 21:
            screen.blit(mystery, (54 * i + x, height - 2 * 54 - 500))
        if i == 15 or i == 33:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 500))
        if i == 22 or i == 55:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 400))
        if i == 5 or i == 40:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 450))
        if i == 63:
            screen.blit(flag, (54 * i + x, height - 2 * 54 - 350))
        if i == 65:
            screen.blit(castle, (54 * i + x, height - 2 * 54 - 376))
        screen.blit(bottom_brick, (54 * i + x, height - 54))
        screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))

def game_Over():
    bg = pygame.image.load("Images/Background2.jpg").convert()

    screen.blit(bg, (0, 0))

    font = pygame.font.Font('font.ttf', 26)
    text7 = font.render('GAME OVER', False, (255, 255, 255))

    screen.blit(text7, (400, 345))

    pygame.display.flip()

def check_Platforms(mario, x):
    if (54 * 18 + x) <= mario.circlePosX <= (54 * 24 + x):
        if mario.newplayerPosY < 377:
            mario.originalplayerPosY = 377
    elif 54 * 29 + x <= mario.circlePosX <= 54 * 29 + 114 + x:
        if mario.newplayerPosY < height - 2 * 54 - 120 - 65:
            mario.originalplayerPosY = height - 2 * 54 - 120 - 65
    elif 54 * 38 + x <= mario.circlePosX <= 54 * 38 + 114 + x:
        if mario.newplayerPosY < height - 2 * 54 - 120 - 65:
            mario.originalplayerPosY = height - 2 * 54 - 120 - 65
    elif 54 * 46 + x <= mario.circlePosX <= 54 * 46 + 114 + x:
        if mario.newplayerPosY < height - 2 * 54 - 120 - 65:
            mario.originalplayerPosY = height - 2 * 54 - 120 - 65
    elif 54 * 57 + x <= mario.circlePosX <= 54 * 57 + 114 + x:
        if mario.newplayerPosY < height - 2 * 54 - 120 - 65:
            mario.originalplayerPosY = height - 2 * 54 - 120 - 65
    else:
        mario.originalplayerPosY = 700 - 54*2 - 60
    if mario.newplayerPosY > 700 - 54*2 - 60:
        mario.newplayerPosY = 700 - 54 * 2 - 60

class player:
    def __init__(self, height, width):
        self.stageWidth = width * 9 - 500
        self.stagePosX = 0

        self.startScrollingPosX = width / 2

        self.circleRadius = 150
        self.circlePosX = self.circleRadius

        self.playerPosX = self.circleRadius
        self.originalplayerPosY = height - (3 * 58) + 4
        self.newplayerPosY = self.originalplayerPosY
        self.playerVelocityX = 0
        self.tracker = 0
        self.jump = False
        self.fall = False


####################
#   LEVEL LOOP     #
####################
FPS = 60

pygame.init()

pygame.display.set_caption("Super Python Bros.")

jump_noise = pygame.mixer.Sound('Sound Effects/smb_jump-small.wav')

width, height = 1026, 700

screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("Images/Background.jpg").convert()

mario = player(height, width)

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

    k = pygame.key.get_pressed()

    check_Platforms(mario, mario.stagePosX)

    if mario.jump or mario.fall:
        if mario.tracker < 4 and mario.jump:
            mario.newplayerPosY -= 60

        else:
            if mario.newplayerPosY < mario.originalplayerPosY:
                if mario.newplayerPosY + 60 < mario.originalplayerPosY:
                    mario.newplayerPosY += 60
                else:
                    mario.newplayerPosY = mario.originalplayerPosY

            else:
                mario.newplayerPosY = mario.originalplayerPosY
                mario.tracker = 0
                mario.jump = False
                mario.fall = False
                continue

        mario.tracker += 1

    elif k[K_l] and not mario.jump:
        pygame.mixer.music.pause()
        jump_noise.play()
        pygame.mixer.music.unpause()
        mario.jump = True
        continue

    if k[K_s]:
        check_Platforms(mario, mario.stagePosX)
        if mario.originalplayerPosY > mario.newplayerPosY:
            mario.fall = True
        mario.playerVelocityX = 30

    elif k[K_a]:
        check_Platforms(mario, mario.stagePosX)
        if mario.originalplayerPosY > mario.newplayerPosY:
            mario.fall = True
        mario.playerVelocityX = -30

    else:
        mario.playerVelocityX = 0

    if k[K_k]:
        mario.playerVelocityX *= 2


    mario.playerPosX += mario.playerVelocityX

    if mario.playerPosX > mario.stageWidth - mario.circleRadius:
        mario.playerPosX = mario.stageWidth - mario.circleRadius
    elif mario.playerPosX < mario.circleRadius:
        mario.playerPosX = mario.circleRadius
    elif mario.playerPosX < mario.startScrollingPosX:
        mario.circlePosX = mario.playerPosX
    elif mario.playerPosX > mario.stageWidth - mario.startScrollingPosX:
        mario.circlePosX = mario.playerPosX - mario.stageWidth + width
    elif 54 * 29 + mario.stagePosX - 45 <= mario.circlePosX <= 54 * 29 + mario.stagePosX and not mario.jump:
        mario.circlePosX = mario.startScrollingPosX
    elif 54 * 38 + mario.stagePosX - 45 <= mario.circlePosX <= 54 * 38 + mario.stagePosX and not mario.jump:
        mario.circlePosX = mario.startScrollingPosX
    elif 54 * 46 + mario.stagePosX - 45 <= mario.circlePosX <= 54 * 46 + mario.stagePosX and not mario.jump:
        mario.circlePosX = mario.startScrollingPosX
    elif 54 * 57 + mario.stagePosX - 45 <= mario.circlePosX <= 54 * 57 + mario.stagePosX and not mario.jump:
        mario.circlePosX = mario.startScrollingPosX
    elif 54 * 29 + mario.stagePosX - 45  + 114 <= mario.circlePosX <= 54 * 29 + 114+ mario.stagePosX and (not mario.jump and not mario.fall):
        if k[K_a] and mario.newplayerPosY > height - 2 * 54 - 120 - 65:
            mario.playerVelocityX = 0
    elif 54 * 38 + mario.stagePosX - 45 + 114<= mario.circlePosX <= 54 * 38 + 114+ mario.stagePosX and (not mario.jump and not mario.fall):
        if k[K_a] and mario.newplayerPosY > height - 2 * 54 - 120 - 65:
            mario.playerVelocityX = 0
    elif 54 * 46 + mario.stagePosX - 45 + 114<= mario.circlePosX <= 54 * 46+ 114 + mario.stagePosX and (not mario.jump and not mario.fall):
        if k[K_a] and mario.newplayerPosY > height - 2 * 54 - 120 - 65:
            mario.playerVelocityX = 0
    elif 54 * 57 + mario.stagePosX - 45 + 114<= mario.circlePosX <= 54 * 57 + 114+ mario.stagePosX and (not mario.jump and not mario.fall):
        if k[K_a] and mario.newplayerPosY > height - 2 * 54 - 120 - 65:
            mario.playerVelocityX = 0
    else:
        mario.circlePosX = mario.startScrollingPosX
        mario.stagePosX += -mario.playerVelocityX

    rel_x = mario.stagePosX % width
    screen.blit(bg, (rel_x - width, 0))
    if rel_x < width:
        screen.blit(bg, (rel_x, 0))

    if mario.playerPosX == width:
        drawBricks()

    print_Back(mario.stagePosX, height)
    screen.blit(avatar, (mario.circlePosX, mario.newplayerPosY))

    pygame.display.update()
    clock.tick(FPS)

    if mario.newplayerPosY > 700:
        pygame.mixer.music.pause()
        if 'gameOver' in sys.modules:
            importlib.reload(sys.modules['gameOver'])

        else:
            __import__('gameOver')
        pygame.mixer.music.unpause()
        break

    elif mario.circlePosX >=54 * 63 + mario.stagePosX:
        pygame.mixer.music.pause()
        if 'winScreen' in sys.modules:
            importlib.reload(sys.modules['winScreen'])

        else:
            __import__('winScreen')
        pygame.mixer.music.unpause()
        break






