######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (level 3.py)                       #
#   CIS 4930                                         #
######################################################\

import pygame
from pygame.locals import *

pygame.init()

width, height = 1026, 700

screen = pygame.display.set_mode((width, height))

bg = pygame.image.load("Images/background.jpg").convert()

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

grass3 = pygame.image.load("Images/Grass/Grass3.png")
grass4 = pygame.image.load("Images/Grass/Grass4.png")
grass5 = pygame.image.load("Images/Grass/Grass5.png")
grass6 = pygame.image.load("Images/Grass/Grass6.png")
grass7 = pygame.image.load("Images/Grass/Grass7.png")
grass8 = pygame.image.load("Images/Grass/Grass8.png")

clock = pygame.time.Clock()
pygame.display.set_caption("Super Python Bros.")


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
            if i == 60:
                screen.blit(mystery_block, (54 * (i - 1) + x, height - 5 * 54 + 4))
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

            elif i == 136 or i == 137:
                screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(finish_block, (54 * i + x, height - 4 * 54 + 3))
                screen.blit(finish_block, (54 * i + x, height - 5 * 54 + 4))
                screen.blit(finish_block, (54 * i + x, height - 6 * 54 + 5))

            elif i == 138 or i == 139:
                screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(finish_block, (54 * i + x, height - 4 * 54 + 3))
                screen.blit(finish_block, (54 * i + x, height - 5 * 54 + 4))
                screen.blit(finish_block, (54 * i + x, height - 6 * 54 + 5))
                screen.blit(finish_block, (54 * i + x, height - 7 * 54 + 6))
                screen.blit(finish_block, (54 * i + x, height - 8 * 54 + 7))

            elif i == 140 or i == 141:
                screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(finish_block, (54 * i + x, height - 4 * 54 + 3))
                screen.blit(finish_block, (54 * i + x, height - 5 * 54 + 4))
                screen.blit(finish_block, (54 * i + x, height - 6 * 54 + 5))
                screen.blit(finish_block, (54 * i + x, height - 7 * 54 + 6))
                screen.blit(finish_block, (54 * i + x, height - 8 * 54 + 7))
                screen.blit(finish_block, (54 * i + x, height - 9 * 54 + 8))
                screen.blit(finish_block, (54 * i + x, height - 10 * 54 + 9))

            elif i == 145:
                screen.blit(big_cloud, (54 * (i + .5) + x, 100))

            elif i == 156:
                screen.blit(final_castle, (54 * i + x, 216))

            elif i == 153:
                screen.blit(finish_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(flagpole, (54 * i + x - 20, 190))

            screen.blit(bottom_brick, (54 * i + x, height - 54))
            screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))


FPS = 60

stageWidth = width * 9 - 500
stagePosX = 0

startScrollingPosX = width / 2

circleRadius = 150
circlePosX = circleRadius

playerPosX = circleRadius
originalplayerPosY = height - (3 * 58) + 4
newplayerPosY = originalplayerPosY
playerVelocityX = 0
tracker = 0
jump = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()

        k = pygame.key.get_pressed()

        if jump == True and tracker <= 5:
            if tracker <= 2:
                newplayerPosY -= 65
            elif 2 < tracker < 5:
                newplayerPosY += 65
            elif tracker == 5:
                newplayerPosY = originalplayerPosY
                tracker = 0
                jump = False
            tracker += 1
        elif k[K_l] and not jump:
                jump = True
                continue

        if k[K_s] :
            playerVelocityX = 30
        elif k[K_a]:
            playerVelocityX = -30
        else:
            playerVelocityX = 0

        if k[K_k]:
            playerVelocityX *= 2


        playerPosX += playerVelocityX

        if playerPosX > stageWidth - circleRadius:
            playerPosX = stageWidth - circleRadius
        elif playerPosX < circleRadius:
            playerPosX = circleRadius
        elif playerPosX < startScrollingPosX:
            circlePosX = playerPosX
        elif playerPosX > stageWidth - startScrollingPosX:
            circlePosX = playerPosX - stageWidth + width
        else:
            circlePosX = startScrollingPosX
            stagePosX += -playerVelocityX

        rel_x = stagePosX % width
        screen.blit(bg, (rel_x - width, 0))
        if rel_x < width:
            screen.blit(bg, (rel_x, 0))

        if playerPosX == width:
            drawBricks()

        print_Back(stagePosX, height)
        screen.blit(avatar, (circlePosX, newplayerPosY))

        pygame.display.update()
        clock.tick(FPS)

