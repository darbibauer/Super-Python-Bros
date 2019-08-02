######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (level 3.py)                       #
#   CIS 4930                                         #
######################################################

import pygame
from pygame.locals import *
import importlib
import sys
import time

avatar = pygame.image.load("Images/Mario.png")
bottom_brick = pygame.image.load("Images/Blue Brick.png")
wall_brick = pygame.image.load("Images/Blue Wall.png")
mystery_block = pygame.image.load("Images/Mystery Block.png")
finish_block = pygame.image.load("Images/Underground Finish Block.png")
pipe = pygame.image.load("Images/Small Pipe.png")
big_pipe = pygame.image.load("Images/Big Pipe.png")
exit_pipe = pygame.image.load("Images/Exit Pipe.png")
goomba = pygame.image.load("Images/Goombas.png")

pygame.mixer.music.pause()
pygame.display.set_caption("Super Python Bros.")

clock = pygame.time.Clock()

mario_dies = pygame.mixer.Sound('Sound Effects/smb_mariodie.wav')

def drawBricks():
    for i in range(0, 16):
        screen.blit(bottom_brick, (54*i, height - 54))
        screen.blit(bottom_brick, (54*i, height - 2*54 + 1))

    pygame.display.flip()

def print_Back(x, height):
    for i in range(0, 181):
        if 0 <= i <= 78 or 82 <= i <= 119 or 122 <= i <= 123 or 126 <= i <= 138 or 146 <= i <= 153 or 160 <= i:
            screen.blit(bottom_brick, (54 * i + x, height - 54))
            screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))

        if i == 0:
            screen.blit(wall_brick, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(wall_brick, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(wall_brick, (54 * i + x, height - 5 * 54 + 4))
            screen.blit(wall_brick, (54 * i + x, height - 6 * 54 + 5))
            screen.blit(wall_brick, (54 * i + x, height - 7 * 54 + 6))
            screen.blit(wall_brick, (54 * i + x, height - 8 * 54 + 7))
            screen.blit(wall_brick, (54 * i + x, height - 9 * 54 + 8))
            screen.blit(wall_brick, (54 * i + x, height - 10 * 54 + 9))
            screen.blit(wall_brick, (54 * i + x, height - 11 * 54 + 10))
            screen.blit(wall_brick, (54 * i + x, height - 12 * 54 + 11))

        elif i == 18:
            screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))

        elif i == 20 or i == 34:
            screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(finish_block, (54 * i + x, height - 4 * 54 + 3))

        elif i == 22 or i == 32:
            screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(finish_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(finish_block, (54 * i + x, height - 5 * 54 + 4))

        elif i == 24 or i == 26:
            screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(finish_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(finish_block, (54 * i + x, height - 5 * 54 + 4))
            screen.blit(finish_block, (54 * i + x, height - 6 * 54 + 5))

        elif 39 <= i <= 41 or 45 <= i <= 47:
            screen.blit(wall_brick, (54 * i + x + 1, height - 6 * 54 + 5))

        elif i == 42 or i == 43 or i == 44:
            screen.blit(wall_brick, (54 * i + x + 1, height - 8 * 54 - 25))

        elif 51 <= i <= 54:
            screen.blit(wall_brick, (54 * i + x + 1, height - 7 * 54 - 25))

        elif 57 <= i <= 62:
            screen.blit(wall_brick, (54 * i + x + 1, height - 7 * 54 - 25))
            if i == 61 or i == 62:
                screen.blit(wall_brick, (54 * i + x + 1, height - 8 * 54 - 25))
                screen.blit(wall_brick, (54 * i + x + 1, height - 9 * 54 - 25))

        elif 66 <= i <= 68:
            screen.blit(wall_brick, (54 * i + x + 1, height - 5 * 54 - 25))

        elif 75 <= i <= 77:
            screen.blit(wall_brick, (54 * i + x + 1, height - 5 * 54 - 25))

        elif i == 102 or i == 114:
            screen.blit(pipe, (54 * i + x, height - 4.5 * 54 + 5))

        elif i == 108:
            screen.blit(big_pipe, (54 * i + x, height - 6.5 * 54 + 5))

        elif 122 <= i <= 123:
            screen.blit(wall_brick, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(wall_brick, (54 * i + x, height - 4 * 54 + 3))

        if 156 <= i <= 157:
            screen.blit(wall_brick, (54 * i + x, height - 4 * 54 + 3))

        elif 160 <= i:
            screen.blit(wall_brick, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(wall_brick, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(wall_brick, (54 * i + x, height - 5 * 54 + 4))
            if i == 176:
                screen.blit(exit_pipe, (54 * i + x + 20, -95))

def check_Platforms(mario):
    if 54 * 18 + mario.stageLocation - 20 <= mario.mario_X < 54 * 19 + mario.stageLocation - 40:
        if mario.newplayerPosY < height - 3 * 54 - 58:
            mario.originalplayerPosY = height - 3 * 54 - 60

    elif 54 * 20 + mario.stageLocation - 20 <= mario.mario_X < 54 * 21 + mario.stageLocation - 10:
        if mario.newplayerPosY < height - 4 * 54 - 60:
            mario.originalplayerPosY = height - 4 * 54 - 60

    elif 54 * 22 + mario.stageLocation - 20 <= mario.mario_X < 54 * 23 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 5 * 54 - 10:
            mario.originalplayerPosY = height - 5 * 54 - 60

    elif 54 * 24 + mario.stageLocation - 20 <= mario.mario_X < 54 * 25 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 6 * 54 - 10:
            mario.originalplayerPosY = height - 6 * 54 - 60

    elif 54 * 26 + mario.stageLocation - 40 <= mario.mario_X < 54 * 27 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 6 * 54 - 10:
            mario.originalplayerPosY = height - 6 * 54 - 60

    elif 54 * 32 + mario.stageLocation - 20 <= mario.mario_X < 54 * 33 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 5 * 54 - 10:
            mario.originalplayerPosY = height - 5 * 54 - 60

    elif 54 * 34 + mario.stageLocation - 20 <= mario.mario_X < 54 * 35 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 4 * 54 - 10:
            mario.originalplayerPosY = height - 4 * 54 - 60

    elif 54 * 39 + mario.stageLocation - 20 <= mario.mario_X < 54 * 42 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 6 * 54 - 58:
            mario.originalplayerPosY = height - 6 * 54 - 58

    elif 54 * 42 + mario.stageLocation - 20 <= mario.mario_X < 54 * 45 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 8 * 54 - 88:
            mario.originalplayerPosY = height - 8 * 54 - 88

    elif 54 * 45 + mario.stageLocation - 20 <= mario.mario_X < 54 * 48 + mario.stageLocation - 30:
        if mario.newplayerPosY < height - 6 * 54 - 58:
            mario.originalplayerPosY = height - 6 * 54 - 58

    elif 54 * 51 + mario.stageLocation - 20 <= mario.mario_X <= 54 * 54 + mario.stageLocation:
        if mario.newplayerPosY < height - 7 * 54 - 88:
            mario.originalplayerPosY = height - 7 * 54 - 88

    elif 54 * 57 + mario.stageLocation - 20 <= mario.mario_X <= 54 * 60 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 7 * 54 - 88:
            mario.originalplayerPosY = height - 7 * 54 - 88

    elif 54 * 61 + mario.stageLocation - 20 <= mario.mario_X <= 54 * 62 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 9 * 54 - 88:
            mario.originalplayerPosY = height - 9 * 54 - 88

    elif 54 * 66 + mario.stageLocation - 20 <= mario.mario_X <= 54 * 68 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 5 * 54 - 88:
            mario.originalplayerPosY = height - 5 * 54 - 88

    elif 54 * 75 + mario.stageLocation - 20 <= mario.mario_X <= 54 * 77 + mario.stageLocation + 20:
        if mario.newplayerPosY < height - 5 * 54 - 85:
            mario.originalplayerPosY = height - 5 * 54 - 88

    elif 54 * 79 + mario.stageLocation - 20 <= mario.mario_X <= 54 * 81 + mario.stageLocation + 20:
        if mario.newplayerPosY >= height - (3 * 58) + 4:
            mario.originalplayerPosY = 1000

    elif 54 * 102 + mario.stageLocation - 10 <= mario.mario_X < 54 * 103 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 4.5 * 54 - 55:
            mario.originalplayerPosY = height - 4.5 * 54 - 50

    elif 54 * 108 + mario.stageLocation - 10 <= mario.mario_X < 54 * 109 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 6.5 * 54 - 55:
            mario.originalplayerPosY = height - 6.5 * 54 - 50

    elif 54 * 114 + mario.stageLocation - 10 <= mario.mario_X < 54 * 115 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 4.5 * 54 - 55:
            mario.originalplayerPosY = height - 4.5 * 54 - 50

    elif 54 * 120 + mario.stageLocation - 20 <= mario.mario_X < 54 * 122 + mario.stageLocation :
        if mario.newplayerPosY >= height - (3 * 58) + 4:
            mario.originalplayerPosY = 1000

    elif 54 * 122 + mario.stageLocation - 60 <= mario.mario_X <= 54 * 123 + mario.stageLocation + 30:
        if mario.newplayerPosY < height - 4 * 54 - 60:
            mario.originalplayerPosY = height - 4 * 54 - 60

    elif 54 * 124 + mario.stageLocation - 20 <= mario.mario_X < 54 * 126 + mario.stageLocation + 30:
        if mario.newplayerPosY >= height - (3 * 58) + 4 or (mario.originalplayerPosY >= height - 4 * 54 - 58 and not mario.jump):
            mario.originalplayerPosY = 1000

    elif 54 * 139 + mario.stageLocation - 20 <= mario.mario_X < 54 * 146 + mario.stageLocation:
        if mario.newplayerPosY >= height - (3 * 58) + 4:
            mario.originalplayerPosY = 1000

    elif 54 * 154 + mario.stageLocation - 20 <= mario.mario_X < 54 * 160 + mario.stageLocation:
        if 54 * 156 + mario.stageLocation - 60 <= mario.mario_X <= 54 * 157 + mario.stageLocation + 30:
            if mario.newplayerPosY < height - 4 * 54 - 60:
                mario.originalplayerPosY = height - 4 * 54 - 60
        elif mario.newplayerPosY >= height - (3 * 58) + 4:
            mario.originalplayerPosY = 1000

    elif 54 * 160 + mario.stageLocation - 60 <= mario.mario_X:
        if mario.newplayerPosY < height - 5 * 54 - 60:
            mario.originalplayerPosY = height - 5 * 54 - 60

    else:
        mario.originalplayerPosY = height - (3 * 58) + 4

def horizontal_Check(mario):
    if 54 * 17 + mario.stageLocation - 15 < mario.mario_X < 54 * 20 + mario.stageLocation - 20:
        if mario.newplayerPosY >= height - 3 * 54 - 58:
            return False
        else:
            return True

    elif 54 * 20 + mario.stageLocation - 20 < mario.mario_X < 54 * 21 + mario.stageLocation - 10:
        if mario.newplayerPosY >= height - 4 * 54 - 60:
            return False
        else:
            return True

    elif 54 * 22 + mario.stageLocation - 20 <= mario.mario_X < 54 * 23 + mario.stageLocation - 30:
        if mario.newplayerPosY >= height - 5 * 54 - 10:
            return True
        else:
            return False

    elif 54 * 24 + mario.stageLocation - 20 <= mario.mario_X < 54 * 25 + mario.stageLocation - 30:
        if mario.newplayerPosY >= height - 6 * 54 - 10:
            return False
        else:
            return True

    elif 54 * 26 + mario.stageLocation - 40 <= mario.mario_X < 54 * 27 + mario.stageLocation - 30:
        if mario.newplayerPosY >= height - 6 * 54 - 10:
            return False
        else:
            return True

    elif 54 * 32 + mario.stageLocation - 20 <= mario.mario_X < 54 * 33 + mario.stageLocation - 30:
        if mario.newplayerPosY >= height - 5 * 54 - 10:
            return False
        else:
            return True

    elif 54 * 34 + mario.stageLocation - 20 <= mario.mario_X < 54 * 35 + mario.stageLocation - 30:
        if mario.newplayerPosY >= height - 4 * 54 - 10:
            return False
        else:
            return True

    elif 54 * 61 + mario.stageLocation - 80 <= mario.mario_X <= 54 * 62 + mario.stageLocation + 30:
        if mario.newplayerPosY > 126 and mario.newplayerPosY <= 234:
            return False
        else:
            return True

    elif 54 * 102 + mario.stageLocation - 80 <= mario.mario_X <= 54 * 104 + mario.stageLocation + 30:
        if mario.newplayerPosY > height - 4.5 * 54:
            return False
        else:
            return True

    elif 54 * 108 + mario.stageLocation - 80 <= mario.mario_X <= 54 * 110 + mario.stageLocation + 30:
        if mario.newplayerPosY > height - 6.5 * 54:
            return False
        else:
            return True

    elif 54 * 114 + mario.stageLocation - 80 <= mario.mario_X <= 54 * 116 + mario.stageLocation + 10:
        if mario.newplayerPosY > height - 4.5 * 54:
            return False
        else:
            return True

    return True

def move_Enemies(enemies_array, mario):
    for i in enemies_array:
        if i.mario_X >= i.x_right and i.playerVelocityX > 0:
            i.playerVelocityX *= -1
        elif i.mario_X <= i.x_left and i.playerVelocityX < 0:
            i.playerVelocityX *= -1

        i.mario_X += i.playerVelocityX


def check_Collision(enemies_array, mario):
    for i in enemies_array:
        if i.mario_X + mario.stageLocation - 10 <= mario.mario_X <= i.mario_X + mario.stageLocation + 50:
            if i.originalplayerPosY <= mario.newplayerPosY <= i.originalplayerPosY + 30:
                pygame.mixer.music.pause()
                mario_dies.play()
                mario.dead = True


class player:
    def __init__(self, height, width):
        self.stageWidth = width * 10 - 500
        self.stageLocation = 0

        self.startMoving = width / 2

        self.marioLength = 150
        self.mario_X = self.marioLength

        self.playerPosX = self.marioLength
        self.originalplayerPosY = height - (3 * 58) + 4
        self.newplayerPosY = 100
        self.playerVelocityX = 0
        self.tracker = 0
        self.jump = False
        self.fall = True
        self.dead = False


class goombas:
    def __init__(self, x, y, left_lim, right_lim):
        self.marioLength = 150
        self.mario_X = x
        self.x_left = left_lim
        self.x_right = right_lim

        self.originalplayerPosY = y
        self.playerVelocityX = -5



####################
#   LEVEL LOOP     #
####################
FPS = 60

pygame.init()

pygame.display.set_caption("Super Python Bros.")

jump_noise = pygame.mixer.Sound('Sound Effects/smb_jump-small.wav')

width, height = 1026, 700

screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("Images/Background2.jpg").convert()

mario = player(height, width)

voice = pygame.mixer.Channel(1)

pipe_noise = pygame.mixer.Sound('Sound Effects/smb_pipe.wav')

voice.play(pipe_noise)

enemies_array = []
enemies_array.append(goombas(700, 500, 50, 650))
enemies_array.append(goombas(54 * 29, 500, 54 * 27, 54 * 31 - 40))
enemies_array.append(goombas(54 * 38, 500, 54 * 35, 54 * 42 - 40))
enemies_array.append(goombas(54 * 53, 500, 54 * 45, 54 * 55 - 40))
enemies_array.append(goombas(54 * 69, 500, 54 * 61, 54 * 70 - 40))
enemies_array.append(goombas(54 * 94, 500, 54 * 83, 54 * 95 - 40))
enemies_array.append(goombas(54 * 136, 500, 54 * 130, 54 * 137 - 40))
enemies_array.append(goombas(54 * 151, 500, 54 * 147, 54 * 152 - 40))
enemies_array.append(goombas(54 * 169, 350, 54 * 160, 54 * 170 - 40))

tracker = 0

while True:
    if tracker < 8:
        tracker += 1
        if tracker == 6:
            pygame.mixer.music.load('Sound Effects/Underground Theme.mp3')
            pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

    k = pygame.key.get_pressed()

    check_Platforms(mario)

    if mario.jump or mario.fall:
        if mario.tracker < 5 and mario.jump:
            mario.newplayerPosY -= 60

        else:
            if mario.newplayerPosY < mario.originalplayerPosY or mario.dead:
                if mario.newplayerPosY + 60 <= mario.originalplayerPosY:
                    mario.newplayerPosY += 60
                else:
                    mario.newplayerPosY = mario.originalplayerPosY

            else:
                mario.newplayerPosY = mario.originalplayerPosY
                mario.tracker = 0
                mario.jump = False
                mario.fall = False

        mario.tracker += 1

    elif k[K_l] and not mario.jump:
        pygame.mixer.music.pause()
        jump_noise.play()
        pygame.mixer.music.unpause()
        mario.jump = True
        continue

    if k[K_s] and (horizontal_Check(mario) or mario.jump):
        check_Platforms(mario)
        if mario.originalplayerPosY > mario.newplayerPosY:
            mario.fall = True
        mario.playerVelocityX = 30

    elif k[K_a] and (horizontal_Check(mario) or mario.jump):
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

    screen.blit(avatar, (mario.mario_X, mario.newplayerPosY))
    for i in enemies_array:
        screen.blit(goomba, (i.mario_X + mario.stageLocation, i.originalplayerPosY))

    print_Back(mario.stageLocation, height)
    move_Enemies(enemies_array, mario)

    pygame.display.update()

    check_Collision(enemies_array, mario)

    clock.tick(FPS)

    if mario.mario_X >= 54 * 176 + mario.stageLocation + 20:
        pygame.mixer.music.pause()
        if 'Level2End' in sys.modules:
            importlib.reload(sys.modules['Level2End'])

        else:
            __import__('Level2End')
        pygame.mixer.music.unpause()
        break

    if mario.newplayerPosY > 700 or mario.dead:
        if mario.dead:
            pygame.time.delay(3000)

        pygame.mixer.music.pause()
        if 'gameOver' in sys.modules:
            importlib.reload(sys.modules['gameOver'])

        else:
            __import__('gameOver')
        pygame.mixer.music.unpause()
        break
