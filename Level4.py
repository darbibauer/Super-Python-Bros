######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (level 4.py)                       #
#   CIS 4930                                         #
######################################################

import pygame
from pygame.locals import *
import importlib
import sys

lose = False
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

block = pygame.image.load("Images/gray2.png")
lava = pygame.image.load("Images/lava.png")
red = pygame.image.load("Images/platform-air.png")
mystery = pygame.image.load("Images/Mystery Block.png")
mushroom = pygame.image.load("Images/Mushroom.jpg")
flag = pygame.image.load("Images/Flagpole.png")
castle = pygame.image.load("Images/Castle.png")
goombaImg = "Images/Goomba.png"


backColor = l(0,0,0)

clock = pygame.time.Clock()
pygame.display.set_caption("Super Python Bros.")


def drawBricks():
    for i in range(0, 16):
        screen.blit(bottom_brick, (54*i, height - 54))
        screen.blit(bottom_brick, (54*i, height - 2*54))

    pygame.display.flip()


def print_Back(x, height):
    screen.fill(backColor)
    for i in range(0, 65):
        if i != 14 and i != 13 and i != 24 and i != 25 and i != 26 and i != 30 and i != 31 and i != 32:
            screen.blit(block, (54 * i + x, height - 54))
            screen.blit(block, (54 * i + x, height - 2 * 54))
            screen.blit(block, (54 * i + x, height - 3 * 54))
            screen.blit(block, (54 * i + x, height - 4 * 54))
            screen.blit(block, (54 * i + x, height - 5 * 54))
        if i < 22 or 34 < i < 50:
            #screen.blit(block, (54 * i + x, height - 10 * 54))
            screen.blit(block, (54 * i + x, height - 11 * 54))
        # if i == 21 or i == 35:
        #     #screen.blit(red, (54 * i + x, height - 8 * 54))
        # if i == 21 or 34 < i < 50:
        #     #screen.blit(block, (54 * i + x, height - 9 * 54))
        screen.blit(block, (54 * i + x, height - 12 * 54))
        if i == 14 or i == 13 or i == 24 or i == 25 or i == 26 or i == 30 or i == 31 or i == 32:
            screen.blit(lava, (54 * i + x, height - 135))
        if i == 28:
            screen.blit(mystery, (54 * i + x, height - 7 * 54 - 100))
        if 0 <= i <= 2:
            screen.blit(block, (54 * i + x, height - 7 * 54))
        if 0 <= i <= 3:
            screen.blit(block, (54 * i + x, height - 6 * 54))
        if 0 <= i <= 12:
            screen.blit(block, (54 * i + x, height - 5 * 54))
        if i == 53:
            screen.blit(flag, (54 * i + x, height - 4 * 54 - 350 - 54))
        if i == 55:
            screen.blit(castle, (54 * i + x, height - 4 * 54 - 376 - 54))


def game_Over():
    bg = pygame.image.load("Images/Background2.jpg").convert()

    screen.blit(bg, (0, 0))

    font = pygame.font.Font('font.ttf', 26)
    text7 = font.render('GAME OVER', False, (255, 255, 255))

    screen.blit(text7, (400, 345))

    pygame.display.flip()

def check_Platforms(mario, x):
    if not mario.jump:
        if (54* 13 + x) <= mario.playerPosX <= (54*14 + x):
            mario.originalplayerPosY = 1000# 700 - 54 * 4 - 65
            mario.lose = True
            pass
        elif (54* 35 + x) <= mario.playerPosX <= (54*36 + x):
            mario.originalplayerPosY = 1000# 700 - 54 * 4 - 65
            mario.lose = True
        elif (54* 37 + x + 45) <= mario.playerPosX <= (54*39 + x):
            mario.originalplayerPosY = 1000# s700 - 54 * 4 - 65
            mario.lose = True
    else:
        mario.originalplayerPos = 700 - 54 * 5 - 65
    if mario.playerPosX >= 54 * 4 + x:
        mario.originalplayerPos = 700 - 54 * 5 - 65
    elif (0 + x) <= mario.playerPosX <= (54 * 2 + x):
        mario.originalplayerPosY = 700 - 54 * 7 - 65
    elif (54 * 2 + x) <= mario.playerPosX <= (54 * 3 + x):
        mario.originalplayerPosY = 700 - 54 * 6 - 65
    elif (54 * 3 + x) <= mario.playerPosX <= (54 * 4 + x):
        mario.originalplayerPosY = 700 - 54 * 5 - 65


class player:
    def __init__(self, height, width):
        self.stageWidth = width * 9 - 500
        self.stagePosX = 0

        self.startScrollingPosX = width / 2

        self.circleRadius = 100
        self.circlePosX = self.circleRadius

        self.playerPosX = self.circleRadius
        self.originalplayerPosY = height - (8 * 54) - 8
        self.newplayerPosY = self.originalplayerPosY
        self.playerVelocityX = 0
        self.tracker = 0
        self.jump = False
        self.fall = False
        self.lose = False


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

    if mario.lose:
        pygame.mixer.music.pause()
        if 'gameOver' in sys.modules:
         importlib.reload(sys.modules['gameOver'])

        else:
            __import__('gameOver')
            pass
        pygame.mixer.music.unpause()
        break

    elif mario.circlePosX >= 54 * 152.5 + mario.stagePosX:
        pygame.mixer.music.pause()
        if 'winScreen' in sys.modules:
            importlib.reload(sys.modules['winScreen'])

        else:
            __import__('winScreen')
        pygame.mixer.music.unpause()
        break






