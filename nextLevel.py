######################################################
#   Darbi Bauer (dkb17) & Sarah Rosenfeld (smr15)    #
#   Group Project (winScreen.py)                     #
#   CIS 4930                                         #
######################################################

import pygame
import time

pygame.init()

width = 1026
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Super Python Bros.")

winning = pygame.mixer.Sound('Sound Effects/smb_stage_clear.wav')
winning.play()


def build_menu():
    bg = pygame.image.load("Images/Background2.jpg").convert()

    screen.blit(bg, (0, 0))

    font = pygame.font.Font('font.ttf', 26)
    text7 = font.render('NEXT LEVEL!', False, (50, 205, 50))

    screen.blit(text7, (400, 345))

    pygame.display.flip()


t_end = time.time() + 6

while time.time() < t_end:
    build_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
