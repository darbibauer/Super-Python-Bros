######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (level 3.py)                       #
#   CIS 4930                                         #
######################################################

import pygame
from pygame.locals import *
import importlib
import sys

pygame.init()

avatar = pygame.image.load("Images/Mario.png")
first_castle = pygame.image.load("Images/First Castle.png")
final_castle = pygame.image.load("Images/Castle.png")
bottom_brick = pygame.image.load("Images/Ground Block.png")
coin = pygame.image.load("Images/Coin.jpg")
bottom_brick = pygame.image.load("Images/Ground Block.png")
brick_block = pygame.image.load("Images/Brick Block.png")
bush = pygame.image.load("Images/Bush.png")
hill = pygame.image.load("Images/Hill.png")
pipe = pygame.image.load("Images/pipe.png")
little_cloud = pygame.image.load("Images/Little Cloud.png")
big_cloud = pygame.image.load("Images/Big Cloud.png")
mystery = pygame.image.load("Images/Mystery Block.png")
jump_block = pygame.image.load("Images/Jump Block.png")
finish_block = pygame.image.load("Images/Finish Block.png")
flagpole = pygame.image.load("Images/Flagpole.png")
mystery_block = pygame.image.load("Images/Mystery Block.png")
goomba = pygame.image.load("Images/Goombas.png")

grass3 = pygame.image.load("Images/Grass/Grass3.png")
grass4 = pygame.image.load("Images/Grass/Grass4.png")
grass5 = pygame.image.load("Images/Grass/Grass5.png")
grass6 = pygame.image.load("Images/Grass/Grass6.png")
grass7 = pygame.image.load("Images/Grass/Grass7.png")
grass8 = pygame.image.load("Images/Grass/Grass8.png")

clock = pygame.time.Clock()
pygame.display.set_caption("Super Python Bros.")


pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
pygame.mixer.music.play(-1)
mario_dies = pygame.mixer.Sound('Sound Effects/smb_mariodie.wav')


def drawBricks():
    for i in range(0, 16):
        screen.blit(bottom_brick, (54*i, height - 54))
        screen.blit(bottom_brick, (54*i, height - 2*54))

    pygame.display.flip()


def print_Back(x, height):
    for i in range(0, 162):
        if 0 <= i < 16:
            screen.blit(bottom_brick, (54 * i + x, height - 54))
            screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))
            if i == 0:
                screen.blit(first_castle, (54 * i + x, height - 408))
            elif i == 5:
                screen.blit(big_cloud, (54 * i + x, 125))
            elif i == 10:
                screen.blit(little_cloud, (54 * i + x, 300))

        elif i == 18:
            screen.blit(grass4, (54 * i + x, height - 3 * 54 + 2))

        elif i == 19 or i == 20:
            if i == 19:
                screen.blit(big_cloud, (54 * i + x, 75))
                screen.blit(jump_block, (54 * i + x, height - 54))
                screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            elif i == 20:
                screen.blit(jump_block, (54 * i + x - 1, height - 54))
                screen.blit(jump_block, (54 * i + x  -1, height - 2 * 54 + 1))

        elif i == 24:
            screen.blit(grass8, (54 * i + x, height - 6 * 54 + 5))

        elif 25 <= i <= 30:
            screen.blit(jump_block, (54 * i + x - (i - 25), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 25), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 25), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 25), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 25), height - 5 * 54 + 4))
            if i == 26:
                screen.blit(grass5, (54 * i + x, height - 10 * 54 + 11))
            if 27 <= i <= 29:
                screen.blit(jump_block, (54 * i + x - (i - 25), height - 7 * 54 + 6))
                screen.blit(jump_block, (54 * i + x - (i - 25), height - 8 * 54 + 7))
                screen.blit(jump_block, (54 * i + x - (i - 25), height - 9 * 54 + 8))

        elif i == 32:
            screen.blit(grass3, (54 * i + x - 4, height - 4 * 54 + 4))

        elif i == 33:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))

        elif i == 35:
            screen.blit(little_cloud, (54 * i + x, 250))
            screen.blit(grass5, (54 * i + x, height - 7 * 54 + 8))

        elif 36 <= i < 39:
            if i == 38:
                screen.blit(little_cloud, (54 * i + x, 200))
            screen.blit(jump_block, (54 * i + x - (i - 36), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 36), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 36), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 36), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 36), height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x - (i - 36), height - 6 * 54 + 5))

        elif i == 40:
            screen.blit(grass7, (54 * i + x, height - 11 * 54 + 11))

        elif 41 <= i < 46:
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 6 * 54 + 5))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 7 * 54 + 6))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 8 * 54 + 7))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 9 * 54 + 8))
            screen.blit(jump_block, (54 * i + x - (i - 41), height - 10 * 54 + 9))
        elif i == 47:
            screen.blit(little_cloud, (54 * i + x, 500))

        elif i == 51 or i == 52:
            screen.blit(jump_block, (54 * i + x - (i - 51), height - 54))
            if i == 51:
                screen.blit(grass4, (54 * (i - 1) + x, height - 2 * 54 + 1))
            elif i == 52:
                screen.blit(big_cloud, (54 * i + x, 100))

        elif 60 <= i <= 62:
            screen.blit(jump_block, (54 * i + x - (i - 60), height - 54))
            if i == 61 or i == 62:
                screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
                screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
                screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
                screen.blit(jump_block, (54 * i + x, height - 6 * 54 + 5))
                screen.blit(jump_block, (54 * i + x, height - 7 * 54 + 6))
                screen.blit(jump_block, (54 * i + x, height - 8 * 54 + 7))
                screen.blit(jump_block, (54 * i + x, height - 9 * 54 + 8))
                if i == 62:
                    screen.blit(grass5, (54 * (i - 3) + x, height - 2 * 54 + 2))
                    screen.blit(grass4, (54 * (i - 2) + x, height - 10 * 54 + 9))
                    screen.blit(little_cloud, (54 * (i - 5) + x, 300))

        elif i == 65:
            screen.blit(grass5, (54 * i + x - 4, height - 2 * 54 + 3))

        elif 66 <= i <= 68:
            screen.blit(jump_block, (54 * i + x - (i - 66), height - 54))
            if i == 67:
                screen.blit(big_cloud, (54 * i + x, 50))

        elif i == 70:
            screen.blit(grass3, (54 * i + x, height - 6 * 54 + 5))

        elif i == 71:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))

        elif i == 76:
            screen.blit(grass6, (54 * i + x, height - 10 * 54 + 9))

        elif 77 <= i <= 80:
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 6 * 54 + 5))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 7 * 54 + 6))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 8 * 54 + 7))
            screen.blit(jump_block, (54 * i + x - (i - 77), height - 9 * 54 + 8))

        elif i == 82:
            screen.blit(little_cloud, (54 * i + x, 300))

        elif i == 88 or i == 86 or i == 87:
            screen.blit(finish_block, (54 * i + x, 300))

        elif i == 84:
            screen.blit(little_cloud, (54 * (i + .5) + x, 250))

        elif i == 90:
            screen.blit(little_cloud, (54 * i + x, 500))

        elif i == 93:
            screen.blit(grass4, (54 * i + x, height - 4 * 54 + 3))

        elif i == 94 or i == 95:
            screen.blit(jump_block, (54 * i + x - (i - 94), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 94), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 94), height - 3 * 54 + 2))
            if i == 94:
                screen.blit(big_cloud, (54 * (i + .5) + x, 100))

        elif i == 99:
            screen.blit(grass8, (54 * i + x, height - 8 * 54 + 7))

        elif 100 <= i <= 105:
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 6 * 54 + 5))
            screen.blit(jump_block, (54 * i + x - (i - 100), height - 7 * 54 + 6))

        elif i == 108:
            screen.blit(grass3, (54 * i + x, height - 2 * 54 + 1))

        elif i == 109:
            screen.blit(big_cloud, (54 * (i + .5) + x, 100))
            screen.blit(jump_block, (54 * i + x, height - 54))

        elif i == 111 or i == 118:
            screen.blit(grass4, (54 * i + x, height - 6 * 54 + 5))

        elif i == 112 or i == 113:
            screen.blit(jump_block, (54 * i + x - (i - 112), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 112), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 112), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 112), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 112), height - 5 * 54 + 4))

        elif i == 119 or i == 120:
            screen.blit(jump_block, (54 * i + x - (i - 119), height - 54))
            screen.blit(jump_block, (54 * i + x - (i - 119), height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x - (i - 119), height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x - (i - 119), height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x - (i - 119), height - 5 * 54 + 4))

        elif 125 <= i <= 161:
            if i == 127:
                screen.blit(little_cloud, (54 * (i + .5) + x, 400))

            elif i == 129:
                screen.blit(little_cloud, (54 * (i + .5) + x, 350))

            elif i == 145:
                screen.blit(big_cloud, (54 * (i + .5) + x, 100))

            elif i == 156:
                screen.blit(final_castle, (54 * i + x, 216))

            elif i == 153:
                screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(flagpole, (54 * i + x - 20, 190))

            screen.blit(bottom_brick, (54 * i + x, height - 54))
            screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))

def game_Over():
    bg = pygame.image.load("Images/Background2.jpg").convert()

    screen.blit(bg, (0, 0))

    font = pygame.font.Font('font.ttf', 26)
    text7 = font.render('GAME OVER', False, (255, 255, 255))

    screen.blit(text7, (400, 345))

    pygame.display.flip()

def check_Platforms(mario):
    if 0 + mario.stageLocation <= mario.mario_X < 15.5 * 54 + mario.stageLocation:
        if mario.newplayerPosY< height - 170:
            mario.originalplayerPosY = height - 170

    elif 17 * 54 + mario.stageLocation <= mario.mario_X <= 1115 + mario.stageLocation:
        if mario.newplayerPosY < height - 220:
            mario.originalplayerPosY = height - 220

    # THIS ONE
    elif 1385 + mario.stageLocation <= mario.mario_X <= 1664 + mario.stageLocation:
        if mario.newplayerPosY < height - 590:
            mario.originalplayerPosY = height - 590

    elif 1292 + mario.stageLocation <= mario.mario_X <= 1680 + mario.stageLocation:
        if 1385 + mario.stageLocation <= mario.mario_X <= 1574 + mario.stageLocation:
            if mario.newplayerPosY < height - 590:
                mario.originalplayerPosY = height - 590
            elif mario.newplayerPosY < height - 380:
                mario.originalplayerPosY = height - 380
        if mario.newplayerPosY < height - 380:
            mario.originalplayerPosY = height - 380

    elif 54 * 32 - 20 + mario.stageLocation <= mario.mario_X < 54 * 32 + mario.stageLocation + 54 * 3 - 5:
        if mario.newplayerPosY < height - 274:
            mario.originalplayerPosY = height - 274

    elif 54 * 34.5 + mario.stageLocation <= mario.mario_X <= 54 * 35 + mario.stageLocation + 54 * 5 - 9:
        if mario.newplayerPosY < height - 430:
            mario.originalplayerPosY = height - 430

    elif 54 * 40 + mario.stageLocation <= mario.mario_X <= 54 * 40 + mario.stageLocation + 54 * 7 - 8:
        if mario.newplayerPosY < 55:
            mario.originalplayerPosY = 55

    elif 54 * 50 + mario.stageLocation <= mario.mario_X <= 54 * 50 + mario.stageLocation + 54 * 4 - 7:
        if mario.newplayerPosY < 530:
            mario.originalplayerPosY = 530

    elif 54 * 58 + mario.stageLocation <= mario.mario_X <= 54 * 59 + mario.stageLocation + 54 * 5 - 8:
        if 54 * 60 + mario.stageLocation <= mario.mario_X <= 54 * 60 + mario.stageLocation + 54 * 4 - 7:
            if mario.newplayerPosY < 110:
                mario.originalplayerPosY = 110
        else:
            mario.originalplayerPosY = 530

    elif 54 * 65 - 2 + mario.stageLocation <= mario.mario_X <= 54 * 65 - 2 + mario.stageLocation + 54 * 5 - 11:
        if mario.newplayerPosY < 530:
            mario.originalplayerPosY = 530

    elif 54 * 70 + mario.stageLocation <= mario.mario_X <= 54 * 70 + mario.stageLocation + 54 * 3 + 7:
        if mario.newplayerPosY < 320:
            mario.originalplayerPosY = 320

    elif 54 * 76 + mario.stageLocation <= mario.mario_X <= 54 * 6 - 12 + 54 * 76 + mario.stageLocation:
        if mario.newplayerPosY < 110:
            mario.originalplayerPosY = 110

    elif 54 * 86 + mario.stageLocation <= mario.mario_X <= 54 * 88 + mario.stageLocation:
        if mario.newplayerPosY < 235:
            mario.originalplayerPosY = 235

    elif 54 * 93 + mario.stageLocation <= mario.mario_X <= 54 * 93 + mario.stageLocation + 54 * 4 - 7:
        if mario.newplayerPosY < 427:
            mario.originalplayerPosY = 427

    elif 54 * 99 + mario.stageLocation <= mario.mario_X <= 54 * 99 + mario.stageLocation + 54 * 8 - 15:
        if mario.newplayerPosY < 215:
            mario.originalplayerPosY = 215

    elif 54 * 107.5 + mario.stageLocation <= mario.mario_X <= 54 * 108 + mario.stageLocation + 54 * 3 + 3:
        if mario.newplayerPosY < 532:
            mario.originalplayerPosY = 532

    elif 54 * 111 + mario.stageLocation <= mario.mario_X <= 54 * 111 + mario.stageLocation + 54 * 4 - 7:
        if mario.newplayerPosY< 321:
            mario.originalplayerPosY = 321

    elif 54 * 117.5 + mario.stageLocation <= mario.mario_X <= 54 * 118 + mario.stageLocation + 54 * 4 - 7:
        if mario.newplayerPosY < 321:
            mario.originalplayerPosY = 321

    elif 54 * 125 + mario.stageLocation <= mario.mario_X:
        if mario.newplayerPosY < height - (3 * 58) + 4:
            mario.originalplayerPosY = height - (3 * 58) + 4

    else:
        mario.originalplayerPosY = 1000

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
        self.stageWidth = width * 9 - 500
        self.stageLocation = 0

        self.startMoving = width / 2

        self.marioLength = 150
        self.mario_X = self.marioLength

        self.playerPosX = self.marioLength
        self.originalplayerPosY = height - (3 * 58) + 4
        self.newplayerPosY = self.originalplayerPosY
        self.playerVelocityX = 0
        self.tracker = 0
        self.jump = False
        self.fall = False
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

pygame.display.set_caption("Super Python Bros.")

jump_noise = pygame.mixer.Sound('Sound Effects/smb_jump-small.wav')

width, height = 1026, 700

screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("Images/Background.jpg").convert()

mario = player(height, width)

enemies_array = []
enemies_array.append(goombas(54 * 29, 80, 54 * 26, 54 * 30 - 40))
enemies_array.append(goombas(54 * 46, 30, 54 * 40, 54 * 45 - 40))
enemies_array.append(goombas(54 * 106, 184, 54 * 99, 54 * 106 - 40))
enemies_array.append(goombas(54 * 135, 500, 54 * 126, 54 * 135 - 40))
enemies_array.append(goombas(54 * 150, 500, 54 * 137, 54 * 150 - 40))


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
        jump_noise.play()
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
    for i in enemies_array:
        screen.blit(goomba, (i.mario_X + mario.stageLocation, i.originalplayerPosY))

    move_Enemies(enemies_array, mario)

    check_Collision(enemies_array, mario)

    pygame.display.update()
    clock.tick(FPS)

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

    elif mario.mario_X >= 54 * 152.5 + mario.stageLocation:
        pygame.mixer.music.pause()
        if 'nextLevel' in sys.modules:
            importlib.reload(sys.modules['nextLevel'])

        else:
            __import__('nextLevel')
        pygame.mixer.music.unpause()
        break






