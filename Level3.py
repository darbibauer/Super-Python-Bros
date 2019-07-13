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

clock = pygame.time.Clock()
pygame.display.set_caption("Super Python Bros.")


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

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
        elif i == 19 or i == 20:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            if i == 19:
                screen.blit(big_cloud, (54 * i + x, 75))
        elif 25 <= i <= 30:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
            if 27 <= i <= 29:
                screen.blit(jump_block, (54 * i + x, height - 7 * 54 + 6))
                screen.blit(jump_block, (54 * i + x, height - 8 * 54 + 7))
                screen.blit(jump_block, (54 * i + x, height - 9 * 54 + 8))
        elif i == 33:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
        elif 36 <= i < 39:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x, height - 6 * 54 + 5))
        elif 41 <= i < 46:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x, height - 6 * 54 + 5))
            screen.blit(jump_block, (54 * i + x, height - 7 * 54 + 6))
            screen.blit(jump_block, (54 * i + x, height - 8 * 54 + 7))
            screen.blit(jump_block, (54 * i + x, height - 9 * 54 + 8))
            screen.blit(jump_block, (54 * i + x, height - 10 * 54 + 9))
        elif i == 51 or i == 52:
            screen.blit(jump_block, (54 * i + x, height - 54))
        elif 60 <= i <= 62:
            screen.blit(jump_block, (54 * i + x, height - 54))
            if i == 61 or i == 62:
                screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
                screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
                screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
                screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
                screen.blit(jump_block, (54 * i + x, height - 6 * 54 + 5))
                screen.blit(jump_block, (54 * i + x, height - 7 * 54 + 6))
                screen.blit(jump_block, (54 * i + x, height - 8 * 54 + 7))
                screen.blit(jump_block, (54 * i + x, height - 9 * 54 + 8))
        elif 66 <= i <= 68:
            screen.blit(jump_block, (54 * i + x, height - 54))
        elif i == 71:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
        elif 77 <= i <= 80:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x, height - 6 * 54 + 5))
            screen.blit(jump_block, (54 * i + x, height - 7 * 54 + 6))
            screen.blit(jump_block, (54 * i + x, height - 8 * 54 + 7))
            screen.blit(jump_block, (54 * i + x, height - 9 * 54 + 8))
        elif i == 94 or i == 95:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
        elif 100 <= i <= 105:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
            screen.blit(jump_block, (54 * i + x, height - 6 * 54 + 5))
            screen.blit(jump_block, (54 * i + x, height - 7 * 54 + 6))
        elif i == 109:
            screen.blit(jump_block, (54 * i + x, height - 54))
        elif i == 112 or i == 113 or i == 119 or i == 120:
            screen.blit(jump_block, (54 * i + x, height - 54))
            screen.blit(jump_block, (54 * i + x, height - 2 * 54 + 1))
            screen.blit(jump_block, (54 * i + x, height - 3 * 54 + 2))
            screen.blit(jump_block, (54 * i + x, height - 4 * 54 + 3))
            screen.blit(jump_block, (54 * i + x, height - 5 * 54 + 4))
        elif 125 <= i <= 161:
            screen.blit(bottom_brick, (54 * i + x, height - 54))
            screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))
            if i == 156:
                screen.blit(final_castle, (54 * i + x, 216))


FPS = 60

stageWidth = width * 9 - 500
stagePosX = 0

startScrollingPosX = width / 2

circleRadius = 150
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = height - (3 * 58) + 4
playerVelocityX = 0

if __name__ == "__main__":
    while True:
        events()

        k = pygame.key.get_pressed()

        if k[K_s]:
            playerVelocityX = 100
        elif k[K_a]:
            playerVelocityX = -100
        else:
            playerVelocityX = 0

        playerPosX += playerVelocityX

        if playerPosX > stageWidth - circleRadius:
            playerPosX = stageWidth - circleRadius
        if playerPosX < circleRadius:
            playerPosX = circleRadius
        if playerPosX < startScrollingPosX:
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
        screen.blit(avatar, (circlePosX, playerPosY))

        pygame.display.update()
        clock.tick(FPS)

