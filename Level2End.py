######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (Level2End.py)                     #
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
pipe = pygame.image.load("Images/Small Pipe.png")
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
            if i == 1:
                screen.blit(pipe, (54 * i + x, 460))
            elif i == 5:
                screen.blit(big_cloud, (54 * i + x, 125))
            elif i == 10:
                screen.blit(little_cloud, (54 * i + x, 300))

            elif i== 11:
                screen.blit(flagpole, (54 * i + x - 20, 242))

            elif i == 13:
                screen.blit(final_castle, (54 * i + x, 217))


def check_Platforms(mario):
    if 1 * 54 <= mario.circlePosX <= 3 * 54 - 30:
        mario.originalplayerPosY = 403
    else:
        mario.originalplayerPosY = height - (3 * 58) + 4


class player:
    def __init__(self, height, width):
        self.stageWidth = width
        self.stagePosX = 0

        self.startScrollingPosX = width / 2

        self.circleRadius = 100
        self.circlePosX = self.circleRadius

        self.playerPosX = self.circleRadius
        self.originalplayerPosY = 403
        self.newplayerPosY = 403
        self.playerVelocityX = 0
        self.tracker = 0
        self.jump = False
        self.fall = False


FPS = 60

pygame.init()

pygame.display.set_caption("Super Python Bros.")

jump_noise = pygame.mixer.Sound('Sound Effects/smb_jump-small.wav')

width, height = 1026, 700

screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("Images/Background.jpg").convert()

mario = player(height, width)

voice = pygame.mixer.Channel(1)

pipe_noise = pygame.mixer.Sound('Sound Effects/smb_pipe.wav')

voice.play(pipe_noise)

tracker = 0

while True:
    if tracker < 8:
        tracker += 1
        if tracker == 8:
            pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
            pygame.mixer.music.play(-1)
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

    print_Back(mario.stagePosX, height)
    screen.blit(avatar, (mario.circlePosX, mario.newplayerPosY))

    pygame.display.update()
    clock.tick(FPS)

    if mario.circlePosX >= 54 * 11 - 20:
        pygame.mixer.music.pause()
        if 'nextLevel' in sys.modules:
            importlib.reload(sys.modules['nextLevel'])

        else:
            __import__('nextLevel')
        pygame.mixer.music.unpause()
        break
