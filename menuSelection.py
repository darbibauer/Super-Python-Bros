######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (menuSelection.py)                 #
#   CIS 4930                                         #
######################################################

import pygame
import time

pygame.init()

width = 1026
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Python Bros.")

pause = pygame.mixer.Sound('Sound Effects/smb_pause.wav')
pause.play()


def build_menu():
    bg = pygame.image.load("Images/Background2.jpg").convert()

    screen.blit(bg, (0, 0))

    pygame.display.flip()


t_end = time.time() + 1

while time.time() < t_end:
    build_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
