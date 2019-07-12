# Super Python Bros Level One

import pygame

pygame.init()

white= (255,255,255)
backColor = (102,178,255)
width= 1000
height = 700

background = (102, 178, 255)

pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Level 1")

clock = pygame.time.Clock()


crashed = False
coinImg = pygame.image.load("Images/Coin.jpg")
pyImg = pygame.image.load("Images/mario.png")
bottom_brick = pygame.image.load("Images/Ground Block.png")
brick_block = pygame.image.load("Images/Brick Block.png")
bush = pygame.image.load("Images/Bush.png")
hill = pygame.image.load("Images/Hill.png")
pipe = pygame.image.load("Images/pipe.png")
clouds = pygame.image.load("Images/Clouds.png")
mystery = pygame.image.load("Images/Mystery Block.png")

def coins(x,y):
    screen.blit(coinImg,(x,y))

def pyMove(x,y):
    screen.blit(pyImg,(x,y))

x = width* .15
y = height - 2 * 54 -65

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
jumpCount = 0
backSpot = 0

class User(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        # self.hitbox(self.x + 49, self.y, 49, 65)
    def printUser(self, x, y):
        screen.blit(self.image, (x, y))

def print_Back(x, height):
    screen.fill(backColor)
    for i in range(0, 59):
        if i == 12 or i == 24 or i == 42:
            screen.blit(bush,(54 * i + x, height - 2 * 54 - 103))
        if i == 0 or i == 16 or i == 48:
            screen.blit(hill,(54 * i + x, height - 2 * 54 - 128))
        if i == 29 or i == 38 or i == 46 or i == 57:
            screen.blit(pipe,(54 * i + x, height - 2 * 54 - 189))
        if i == 16 or i == 20 or i == 22:
            screen.blit(mystery,(54 * i + x, height - 2 * 54 - 300))
        if i == 19 or i == 21 or i == 23:
            screen.blit(brick_block,(54 * i + x, height - 2 * 54 - 300))
        if i == 21:
            screen.blit(mystery, (54 * i + x, height - 2 * 54 - 500))
        if i == 15 or i == 33:
            screen.blit(clouds,(54 * i + x, height - 2 * 54 - 500))
        if i == 22 or i == 55:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 400))
        if i == 5 or i == 40:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 450))
        screen.blit(bottom_brick, (54 * i + x, height - 54))
        screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))


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
                    jumpCount = 10
            else:
                if jumpCount >= 0:
                    y -= jumpCount ** 2
                    jumpCount-= 1
                elif jumpCount >= -10:
                    y += jumpCount ** 2
                    jumpCount -= 1
                elif jumpCount == -11:
                    jumping = False

        if rightmove:
            backSpot -= speed
        if rightfast:
            backSpot -= speed * 2

        print_Back(backSpot, height)
        User.printUser(mario, x, y)
        rightmove = False
        rightfast = False



    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

