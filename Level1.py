# Super Python Bros Level One

import pygame

pygame.init()

white= (255,255,255)
backColor = (102,178,255)
width= 1000
height = 700

background = (102, 178, 255)

jump_noise = pygame.mixer.Sound('Sound Effects/smb_jump-small.wav')
pygame.mixer.music.load('Sound Effects/Main Theme.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Level 1")

clock = pygame.time.Clock()


crashed = False
coinImg = pygame.image.load("Images/Coin.png")
pyImg = pygame.image.load("Images/mario.png")
bottom_brick = pygame.image.load("Images/Ground Block.png")
brick_block = pygame.image.load("Images/Brick Block.png")
bush = pygame.image.load("Images/Bush.png")
hill = pygame.image.load("Images/Hill.png")
pipe = pygame.image.load("Images/pipe.png")
clouds = pygame.image.load("Images/Clouds.png")
mystery = pygame.image.load("Images/Mystery Block.png")
flag = pygame.image.load("Images/Flagpole.png")
castle = pygame.image.load("Images/Castle.png")
goombaImg = "Images/Goomba.png"

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
falling = False
onSurface = False
fallCount = 0
jumpCount = 0
backSpot = 0
direction = 1
loopCount = 0

class User(pygame.sprite.Sprite):
    height: int

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x: int = x
        self.y: int  = y
        self.height = 65
        self.width = 49
        self.hitbox = (self.x, self.y, 49, 65)
        self.bottom = self.y - 65
        self.center = self.x + 25
    def printUser(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, 49, 65)
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
    def selfMove(self, direction, x):
        self.x += 15 * direction + x



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
    def selfMove(self, direction):
        self.x += 15 * direction

def print_Back(x, height):
    screen.fill(backColor)
    for i in range(0, 79):
        if i == 12 or i == 24 or i == 42:
            screen.blit(bush,(54 * i + x, height - 2 * 54 - 103))
        if i == 0 or i == 16 or i == 48:
            screen.blit(hill,(54 * i + x, height - 2 * 54 - 128))
        if i == 29 or i == 38 or i == 46 or i == 57:
            screen.blit(pipe,(54 * i + x, height - 2 * 54 - 120))
        if i == 16 or i == 20 or i == 22:
            screen.blit(mystery,(54 * i + x, height - 2 * 54 - 150))
        if i == 19 or i == 21 or i == 23:
            screen.blit(brick_block,(54 * i + x, height - 2 * 54 - 150))
        if i == 21:
            screen.blit(mystery, (54 * i + x, height - 2 * 54 - 500))
        if i == 15 or i == 33:
            screen.blit(clouds,(54 * i + x, height - 2 * 54 - 500))
        if i == 22 or i == 55:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 400))
        if i == 5 or i == 40:
            screen.blit(clouds, (54 * i + x, height - 2 * 54 - 450))
        if i == 63:
            screen.blit(flag, (54 * i + x, height - 2 * 54 - 350))
        if i == 65:
            screen.blit(castle, (54 * i + x, height - 2 * 54 - 376))
        screen.blit(bottom_brick, (54 * i + x, height - 54))
        screen.blit(bottom_brick, (54 * i + x, height - 2 * 54))

def checkPlatforms(mario,x, jumping):
    if (54 * 19 + x) <= mario.x <= (54 * 24 + x):
        print(700 - 54 * 2 - 150, mario.bottom, 700 - 54 * 2 - 150 - 65)
        print("x", 54*19+x, mario.x, 54*25+x)
        if (442 + 65) >= mario.y > (377 + 65):
            # if hits bottom
            # FIX THIS
            mario.y += 30
        elif (442) >= mario.y >= (377):
            # if on top of platform
            print("here", mario.x)
            mario.y = 377  # 700 - 2 * 54 - 150 - 65
        elif mario.x < 377 + 54:
            #if below
            mario.y = 700 - 54 * 2 - 65
    elif (54 * 16 + x) <= mario.center <= (54 * 17 + x):
        if (442 + 65) >= mario.y > (377 + 65):
            mario.y += 30
        elif (442) >= mario.y >= (377):
            print("here", mario.x)
            mario.y = 377  # 700 - 2 * 54 - 150 - 65
        elif mario.x < 377 + 54:
            mario.y = 700 - 54 * 2 - 65
    elif 54 * 29 + x <= mario.x <= 54 * 29 + 114 + x and (442+ 54) >= mario.y >= (377 + 54):
            mario.y = 377 +54
    elif 54 * 38 + x <= mario.x <= 54 * 38 + 114 + x and (442 + 54) >= mario.y >= (377 + 54):
            mario.y = 377 + 54
    elif 54 * 46 + x <= mario.x <= 54 * 46 + 114 + x and (442 + 54) >= mario.y >= (377 + 54):
            mario.y = 377 + 54
    elif 54 * 57 + x <= mario.x <= 54 * 57 + 114 + x and (442 + 54) >= mario.y >= (377 + 54):
            mario.y = 377 + 54
    elif not jumping and mario.y < 700 - 54 * 2 - 65:
        mario.y += 30
    elif not jumping and mario.y >= 700 - 54 * 2 - 65:
        mario.y = 700 - 54 * 2 - 65
    elif not jumping:
        if mario.y == (700-54 * 2 - 65):
            mario.y = 700 - 54*2 - 65
        else:
            mario.y += 30


marioImg = "Images/mario.png"
mario = User(0, 700 - 54*2 - 65, marioImg)
platform = obstacle(54 * 20 + x, height - 2 * 54 - 150, 54 * 6 , 54)
box = obstacle(54 * 18 + x, height - 2 * 54 - 150, 54, 54)
ground = obstacle(0, height - 54*2, 54*60, 54*2)
goomba1 = User(54 * 38, 700 - 54 * 2 - 34, goombaImg)
goomba2 = User(54 * 54, 700 - 54 * 2 - 34, goombaImg)

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
                        if 54 * 29 + backSpot - 45 <= mario.x <= 54 * 29 + backSpot and not jumping:
                            pass
                        elif 54 * 38 + backSpot - 45 <= mario.x <= 54 * 38 + backSpot and not jumping:
                            pass
                        elif 54 * 46 + backSpot - 45 <= mario.x <= 54 * 46 + backSpot and not jumping:
                            pass
                        elif 54 * 57 + backSpot - 45 <= mario.x <= 54 * 57 + backSpot and not jumping:
                            pass
                        else:
                            mario.x += speed * 2
                    else:
                        if 54 * 29 + backSpot - 45 <= mario.x <= 54 * 29 + backSpot and not jumping:
                            pass
                        elif 54 * 38 + backSpot - 45 <= mario.x <= 54 * 38 + backSpot and not jumping:
                            pass
                        elif 54 * 46 + backSpot - 45 <= mario.x <= 54 * 46 + backSpot and not jumping:
                            pass
                        elif 54 * 57 + backSpot - 45 <= mario.x <= 54 * 57 + backSpot and not jumping:
                            pass
                        else:
                            rightfast = True
                elif mario.x < width / 2 - speed - marWidth:
                    if 54 * 29 + backSpot - 45 <= mario.x <= 54 * 29 + backSpot and not jumping:
                        pass
                    elif 54 * 38 + backSpot - 45 <= mario.x <= 54 * 38 + backSpot and not jumping:
                        pass
                    elif 54 * 46 + backSpot - 45 <= mario.x <= 54 * 46 + backSpot and not jumping:
                        pass
                    elif 54 * 57 + backSpot - 45 <= mario.x <= 54 * 57 + backSpot and not jumping:
                            pass
                    else:
                        mario.x += speed

                else:
                    if 54 * 29 + backSpot - 45 <= mario.x <= 54 * 29 + backSpot and not jumping:
                        pass
                    elif 54 * 38 + backSpot - 45 <= mario.x <= 54 * 38 + backSpot and not jumping:
                        pass
                    elif 54 * 46 + backSpot - 45 <= mario.x <= 54 * 46 + backSpot and not jumping:
                        pass
                    elif 54 * 57 + backSpot - 45 <= mario.x <= 54 * 57 + backSpot and not jumping:
                        pass
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

        print(loopCount % 5, loopCount % 5)
        if loopCount % 5 == 0 or loopCount % 11 == 0:
            print("change dir")
            direction *= -1

        print_Back(backSpot, height)
        platform.upObs(backSpot)
        #mario.update(mario.x, mario.y)
        goomba1.update(54*38 + backSpot, 700 - 54*2 - 34)
        goomba1.selfMove(direction, backSpot)
        goomba2.update(54 * 54 + backSpot, 700 - 54 * 2 - 34)
        goomba2.selfMove(direction*2, backSpot)

        checkPlatforms(mario, backSpot, jumping)

    #goomba1.printUser(screen)
    mario.printUser(screen)
    goomba1.printUser(screen)
    goomba2.printUser(screen)
    rightmove = False
    rightfast = False

    for goomba in (goomba1, goomba2):
        if goomba.x <= mario.x <= goomba.x + 30 and mario.y == 700 - 54*2 - 65:
            crashed = True
    pygame.display.update()
    clock.tick(60)

    loopCount += 1


pygame.quit()
quit()
