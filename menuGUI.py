######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (menuGUI.py)                       #
#   CIS 4930                                         #
######################################################

import pygame
import importlib
import sys

pygame.init()

width = 1026
height = 700

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Python Bros.")

pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
pygame.mixer.music.play(-1)


def build_menu():
    # screen.fill((102, 178, 255))
    bg = pygame.image.load("Images/Background.jpg").convert()

    screen.blit(bg, (0, 0))

    logo = pygame.image.load("Images/Logo.png")
    bottom_brick = pygame.image.load("Images/Ground Block.png")
    avatar = pygame.image.load("Images/Mario.png")
    hill = pygame.image.load("Images/Hill.png")
    bush = pygame.image.load("Images/Big Bush.png")
    mushroom = pygame.image.load("Images/Yellow Mushroom.png")

    font = pygame.font.Font('font.ttf', 26)
    text1 = font.render('MARIO', False, (251, 251, 251))
    text2 = font.render('000000', False, (251, 251, 251))
    text3 = font.render('TIME', False, (251, 251, 251))
    text4 = font.render('x00', False, (251, 251, 251))
    text5 = font.render('WORLD', False, (251, 251, 251))
    text6 = font.render('1-1', False, (251, 251, 251))
    text7 = font.render('D.B. & S.R.', False, (255, 208, 160))
    text8 = font.render('START GAME', False, (251, 251, 251))

    screen.blit(logo, (225, 100))
    screen.blit(hill, (30, height - 280))
    screen.blit(bush, (700, height - 322))
    screen.blit(avatar, (5.25*54, height - 3*54 - 11))
    screen.blit(text1, (150, 30))
    screen.blit(text2, (150, 56))
    screen.blit(text3, (825, 30))
    screen.blit(text4, (425, 56))
    screen.blit(text5, (600, 30))
    screen.blit(text6, (630, 56))
    screen.blit(text7, (520, 332))
    screen.blit(text8, (400, 430))
    screen.blit(mushroom, (355, 418))

    # BUILDING BRICKS
    for i in range(0, 19):
        screen.blit(bottom_brick, (54*i, height - 54))
        screen.blit(bottom_brick, (54*i, height - 2*54))

    pygame.display.flip()

# MAIN GAME LOOP
if __name__ == "__main__":
    game_running = True
    while game_running:
        build_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                elif event.key == pygame.K_RETURN:
                    if 'menuSelection' in sys.modules:
                        importlib.reload(sys.modules['menuSelection'])
                    else:
                        __import__('menuSelection')

                    if 'Level1' in sys.modules:
                        importlib.reload(sys.modules['Level1'])
                    else:
                        __import__('Level1')

                    if 'gameOver' not in sys.modules:
                        if 'Level2Beginning' in sys.modules:
                            importlib.reload(sys.modules['Level2Beginning'])
                        else:
                            __import__('Level2Beginning')

                    if 'gameOver' not in sys.modules:
                        if 'Level3' in sys.modules:
                            importlib.reload(sys.modules['Level3'])
                        else:
                            __import__('Level3')

                    if 'gameOver' not in sys.modules:
                        if 'Level4' in sys.modules:
                            importlib.reload(sys.modules['Level4'])
                        else:
                            __import__('Level4')

                    pygame.quit()

