######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (Level2Beginning.py)               #
#   CIS 4930                                         #
######################################################

import pygame
import time
from pygame.locals import *
import importlib
import sys

avatar = pygame.image.load("Images/Mario.png")
first_castle = pygame.image.load("Images/First Castle.png")
final_castle = pygame.image.load("Images/Castle.png")
bottom_brick = pygame.image.load("Images/Ground Block.png")
coin = pygame.image.load("Images/Coin.jpg")
bottom_brick = pygame.image.load("Images/Ground Block.png")
brick_block = pygame.image.load("Images/Brick Block.png")
bush = pygame.image.load("Images/Bush.png")
hill = pygame.image.load("Images/Hill.png")
pipe = pygame.image.load("Images/Pipe Combination.png")
little_cloud = pygame.image.load("Images/Little Cloud.png")
big_cloud = pygame.image.load("Images/Big Cloud.png")
mystery = pygame.image.load("Images/Mystery Block.png")
jump_block = pygame.image.load("Images/Jump Block.png")
finish_block = pygame.image.load("Images/Finish Block.png")
flagpole = pygame.image.load("Images/Flagpole.png")
mystery_block = pygame.image.load("Images/Mystery Block.png")

clock = pygame.time.Clock()
pygame.display.set_caption("Super Python Bros.")


def print_Back(x, height):
    for i in range(0, 24):
        if 0 <= i < 24:
            screen.blit(bottom_brick, (54 * i + x, height - 54))
            screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))
            if i == 0:
                screen.blit(first_castle, (54 * i + x, height - 408))
            elif i == 5:
                screen.blit(big_cloud, (54 * i + x, 125))
            elif i == 10:
                screen.blit(little_cloud, (54 * i + x, 300))
            elif i == 15:
                screen.blit(pipe, (54 * i + x, height - 3 * 54 - 160))


def check_Platforms(mario):
    if mario.stageLocation <= mario.mario_X <= 54 * 15 + mario.stageLocation :
        if mario.newplayerPosY< height - 170:
            mario.originalplayerPosY = height - 170
    elif 54 * 15 + mario.stageLocation <= mario.mario_X < 54 * 16 + mario.stageLocation:
        if mario.newplayerPosY < 420:
            mario.originalplayerPosY = 420
    elif mario.mario_X > 54 * 16 + mario.stageLocation:
        if mario.newplayerPosY < 325:
            mario.originalplayerPosY = 325


class player:
    def __init__(self, height, width):
        self.stageWidth = width
        self.stageLocation = 0

        self.startMoving = width / 2

        self.marioLength = 50
        self.mario_X = self.marioLength

        self.playerPosX = self.marioLength
        self.originalplayerPosY = height - (3 * 58) + 4
        self.newplayerPosY = self.originalplayerPosY
        self.playerVelocityX = 0
        self.tracker = 0
        self.jump = False
        self.fall = False


FPS = 60

pygame.init()

pygame.display.set_caption("Super Python Bros.")

pipe_noise = pygame.mixer.Sound('Sound Effects/smb_pipe.wav')
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

    check_Platforms(mario)

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
        check_Platforms(mario)
        if mario.originalplayerPosY > mario.newplayerPosY:
            mario.fall = True
        mario.playerVelocityX = 30

    elif k[K_a]:
        check_Platforms(mario)
        if mario.originalplayerPosY > mario.newplayerPosY:
            mario.fall = True
        mario.playerVelocityX = -30
    else:
        mario.playerVelocityX = 0

    if k[K_k]:
        mario.playerVelocityX *= 2


    mario.playerPosX += mario.playerVelocityX

    if mario.playerPosX > mario.stageWidth - mario.marioLength:
        mario.playerPosX = mario.stageWidth - mario.marioLength
    elif mario.playerPosX < mario.marioLength:
        mario.playerPosX = mario.marioLength
    elif mario.playerPosX < mario.startMoving:
        mario.mario_X = mario.playerPosX
    elif mario.playerPosX > mario.stageWidth - mario.startMoving:
        mario.mario_X = mario.playerPosX - mario.stageWidth + width
    else:
        mario.mario_X = mario.startMoving
        mario.stageLocation += -mario.playerVelocityX

    rel_x = mario.stageLocation % width
    screen.blit(bg, (rel_x - width, 0))
    if rel_x < width:
        screen.blit(bg, (rel_x, 0))

    if mario.playerPosX == width:
        drawBricks()

    print_Back(mario.stageLocation, height)
    screen.blit(avatar, (mario.mario_X, mario.newplayerPosY))

    pygame.display.update()
    clock.tick(FPS)

    if 760 < mario.mario_X < 780:
        if 'Level2' in sys.modules:
            importlib.reload(sys.modules['Level2'])

        else:
            __import__('Level2')
        pygame.mixer.music.pause()
        break
