# Super Python Bros Level Four

import pygame

pygame.init()

white= (255,255,255)
backColor = (0,0,0)
width= 1000
height = 700

background = (0, 0, 0)


jump_noise = pygame.mixer.Sound('Sound Effects/smb_jump-small.wav')
pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Level 4")

clock = pygame.time.Clock()

"""def coins(x,y):
    screen.blit(coinImg,(x,y))

def pyMove(x,y):
    screen.blit(pyImg,(x,y))"""


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
falling = False
fallCount = 0
backSpot = 0
x = 15
y = height - 7 * 54 - marHeight

block = pygame.image.load("Images/gray2.png")
lava = pygame.image.load("Images/lava.png")
red = pygame.image.load("Images/platform-air.png")
mystery = pygame.image.load("Images/Mystery Block.png")
mushroom = pygame.image.load("Images/Mushroom.jpg")
flag = pygame.image.load("Images/Flagpole.png")
castle = pygame.image.load("Images/Castle.png")

class User(pygame.sprite.Sprite):
    height: int

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x: int = x
        self.y: int = y
        self.height = 65
        self.width = 49
        self.hitbox = (self.x, self.y, 49, 65)
        self.bottom = self.y - 65
        self.center = self.x + 25
    def printUser(self, screen):
        screen.blit(self.image, (mario.x, mario.y))
        self.hitbox = (mario.x, mario.y, 49, 65)
    def collision(self, obs : tuple):
        if self.hitbox[0] <= obs[0] <= self.hitbox[0] + self.x or self.hitbox[0] <= obs[0] + obs[2] <= self.hitbox[0] + self.x:
            if self.hitbox[1] + self.height >= obs[1] >= self.hitbox[1] or self.hitbox[1] + self.height >= obs[1] + obs[3] >= self.hitbox[1]:
                # check if it is on top
                if self.hitbox[1] + self.height >= obs[1] >= self.hitbox[1]:
                    return 1
                return 2

        else:
            return 3
    def top(self):
        return self.y
    def bottom(self):
        return self.y + self.height
    def left(self):
        return self.x
    def right(self):
        return self.x + self.width
    def center(self):
        return self.x + 25
    def update(self, x : int,y : int ):
        self.x = x
        self.y = y
        self.bottom = y + 65
        self.center = x + 25


class obstacle():
    def __init__(self, x, y, wid, h):
        self.hitbox = (x, y, wid, h)
        self.wid : int = wid
        self.h : int= h
        self.x : int= x
        self.y : int= y
    def upObs(self, back):
        self.hitbox = (self.x + back, self.y, self.wid, self.h)
    def box(self):
        return self.hitbox
    def top(self):
        return self.y
    def bottom(self):
        return self.y + self.h
    def left(self):
        return self.x
    def right(self):
        return self.x + self.wid
    def updaate(self, x, y):
        self.x: int = x
        self.y: int = y
    def changeY(self, y):
        self.y = y

def print_Back(x, height):
    screen.fill(backColor)
    for i in range(0, 59):
        if i != 14 and i != 13 and i != 24 and i != 25 and i != 26 and i != 30 and i != 31 and i != 32:
            screen.blit(block, (54 * i + x, height - 54))
            screen.blit(block, (54 * i + x, height - 2 * 54))
            screen.blit(block, (54 * i + x, height - 3 * 54))
            screen.blit(block, (54 * i + x, height - 4 * 54))
        if i < 22 or  34 < i < 50:
            screen.blit(block, (54 * i + x, height - 10 * 54))
            screen.blit(block, (54 * i + x, height - 11 * 54))
        if i == 21 or i == 35:
            screen.blit(red, (54 * i + x, height - 8 * 54))
        if i == 21 or 34 < i < 50:
            screen.blit(block, (54 * i + x, height - 9 * 54))
        screen.blit(block, (54 * i + x, height - 12 * 54))
        if i == 14 or i == 13 or i == 24 or i == 25 or i == 26 or i == 30 or i == 31 or i == 32:
            screen.blit(lava, (54 * i + x, height - 135))
        if i == 28:
            screen.blit(mystery, (54 * i + x, height - 7 * 54 - 100))
        if 0 <= i <= 2:
            screen.blit(block, (54 * i + x, height - 7 * 54))
        if 0 <= i <= 3:
            screen.blit(block, (54 * i + x, height - 6 * 54))
        if 0 <= i <= 4:
            screen.blit(block, (54 * i + x, height - 5 * 54))
        if i == 53:
            screen.blit(flag, (54 * i + x, height - 4 * 54 - 350))
        if i == 55:
            screen.blit(castle, (54 * i + x, height - 4 * 54 - 376))

def checkPlatforms(mario,x, jumping):
    if not jumping:
        if (54* 13 + x) <= mario.x <= (54*15 + x):
            mario.y += 30
        elif (54* 24 + x) <= mario.x <= (54*27 + x):
            mario.y += 30
        elif (54* 30 + x) <= mario.x <= (54*33 + x):
            mario.y += 30
        elif mario.x > 54 * 5 + x:
            mario.y = 700 - 54 * 4 - 65


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
                if usrKey[pygame.K_k] and usrKey[pygame.K_s]:
                    if mario.x < width / 2 - speed - marWidth:
                            mario.x += speed * 2
                    else:
                            rightfast = True
                elif mario.x < width / 2 - speed - marWidth:
                        mario.x += speed

                else:
                        rightmove = True
            elif usrKey[pygame.K_a] and x > speed:
                mario.x -= speed
                if usrKey[pygame.K_k] and usrKey[pygame.K_a]:
                    mario.x -= speed
            if not jumping:
                if (usrKey[pygame.K_l] and usrKey[pygame.K_a]) or (usrKey[pygame.K_l] and usrKey[pygame.K_s]) or usrKey[pygame.K_l]:
                    jumping = True
                    jumpCount = 8
                    pygame.mixer.music.pause()
                    jump_noise.play()
                    pygame.mixer.music.unpause()
            else:
                if jumpCount >= 0:
                    mario.y -= jumpCount ** 2
                    jumpCount-= 1
                elif jumpCount >= -8:
                    mario.y += jumpCount ** 2
                    jumpCount -= 1
                elif jumpCount == -9:
                    jumping = False
            if falling:
                if fallCount >= -8:
                    mario.y += fallCount ** 2
                    fallCount -= 1
                elif fallCount == -9:
                    falling = False
                    onSurface = False
                    mario.y = height - 2 * 54 - 65

        if rightmove:
            backSpot -= speed
        if rightfast:
            backSpot -= speed * 2

        print_Back(backSpot, height)

        checkPlatforms(mario, backSpot, jumping)
        if (mario.x == 180 or mario.x == 240 or mario.x == 300) and usrKey[pygame.K_s] and backSpot == 0:
            mario.y += 54
        elif (mario.x == 180 or mario.x == 240 or mario.x == 300) and (usrKey[pygame.K_s] and usrKey[pygame.K_k]) and backSpot == 0:
            mario.y += 54
        User.printUser(mario,  screen)
        rightmove = False
        rightfast = False



    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()


