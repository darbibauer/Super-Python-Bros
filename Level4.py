# Super Python Bros Level Four

import pygame

pygame.init()

white= (255,255,255)
backColor = (0,0,0)
width= 1000
height = 700

background = (0, 0, 0)

pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Level 4")

clock = pygame.time.Clock()

"""def coins(x,y):
    screen.blit(coinImg,(x,y))

def pyMove(x,y):
    screen.blit(pyImg,(x,y))"""

x = 15
y = height - 7 * 54 -65

screen.fill(backColor)

# BUILDING BRICKS

pygame.key.set_repeat(10,10)
speed = 15
marWidth = 49
marHeight = 65
xMove = 0
yMove = 0
rightmove = False
rightfast = False
jumping = False
crashed = False
jumpCount = 0
backSpot = 0

block = pygame.image.load("Images/gray2.png")
lava = pygame.image.load("Images/lava.png")
red = pygame.image.load("Images/platform-air.png")
mystery = pygame.image.load("Images/Mystery Block.png")
mushroom = pygame.image.load("Images/Mushroom.jpg")

class User(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 49, 65)
    def printUser(self, x, y, screen):
        screen.blit(self.image, (x, y))
        self.hitbox = (x, y, 49, 65)
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

class obstacle():
    def __init__(self, x, y, wid, h):
        self.hitbox = (x, y, wid, h)
        self.wid = wid
        self.h = h
    def printObs(self,image, x, y):
        screen.blit(image, (x, y))
        self.hitbox = (x, y, self.wid, self.h)

def print_Back(x, height):
    screen.fill(backColor)
    for i in range(0, 59):
        if i != 14 and i != 13 and i != 24 and i != 25 and i != 26 and i != 30 and i != 31 and i != 32:
            screen.blit(block, (54 * i + x, height - 54))
            screen.blit(block, (54 * i + x, height - 2 * 54))
            screen.blit(block, (54 * i + x, height - 3 * 54))
            screen.blit(block, (54 * i + x, height - 4 * 54))
        if i < 22 or i > 34:
            screen.blit(block, (54 * i + x, height - 10 * 54))
            screen.blit(block, (54 * i + x, height - 11 * 54))
        if i == 21 or i == 35:
            screen.blit(red, (54 * i + x, height - 8 * 54))
        if i == 21 or i >= 35:
            screen.blit(block, (54 * i + x, height - 9 * 54))
        screen.blit(block, (54 * i + x, height - 12 * 54))
        if i == 14 or i == 13 or i == 24 or i == 25 or i == 26 or i == 30 or i == 31 or i == 32:
            screen.blit(lava, (54 * i + x, height - 135))
        if 0 <= i <= 2:
            screen.blit(block, (54 * i + x, height - 7 * 54))
        if 0 <= i <= 3:
            screen.blit(block, (54 * i + x, height - 6 * 54))
        if 0 <= i <= 4:
            screen.blit(block, (54 * i + x, height - 5 * 54))



marioImg = "Images/mario.png"
mario = User(x, y, marioImg)


while not crashed:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        usrKey = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if usrKey[pygame.K_s]:
                if usrKey[pygame.K_l] and usrKey[pygame.K_s]:
                    if x < width / 2 - speed - marWidth:
                        x += speed * 2
                    else:
                        rightfast = True
                elif x < width / 2 - speed - marWidth:
                    x += speed
                else:
                    rightmove = True
            elif usrKey[pygame.K_a] and x > speed:
                x -= speed
                if usrKey[pygame.K_l] and usrKey[pygame.K_a]:
                    x -= speed
            if not jumping:
                if (usrKey[pygame.K_k] and usrKey[pygame.K_a]) or (usrKey[pygame.K_k] and usrKey[pygame.K_s]) or usrKey[pygame.K_k]:
                    jumping = True
                    jumpCount = 7
            else:
                if jumpCount >= 0:
                    y -= jumpCount ** 2
                    jumpCount-= 1
                elif jumpCount >= -7:
                    y += jumpCount ** 2
                    jumpCount -= 1
                elif jumpCount == -8:
                    jumping = False

        if rightmove:
            backSpot -= speed
        if rightfast:
            backSpot -= speed * 2
        if (x == 180 or x == 240 or x == 300) and usrKey[pygame.K_s]:
            y += 54
        print_Back(backSpot, height)
        User.printUser(mario, x, y, screen)
        rightmove = False
        rightfast = False



    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()


