import pygame
import time
import random


#Clock Stuff
clock = pygame.time.Clock()
fps = 60

#Screen Stuff
screen_width = 1000
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Invaders Space")

bg = pygame.image.load("invaders/img/space-bg2.png")
#bg = pygame.transform.scale(bg, (1900, 1010))
bg = pygame.transform.scale(bg, (1000, 750))

#Player Stuff
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/ship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.image = pygame.transform.scale(self.image, (50, 50))

        global moveLeft
        global moveRight

        def moveRight(self, pixels):
            self.rect.x += pixels

        def moveLeft(self, pixels):
            self.rect.x -= pixels
#Player Laser
class pLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/laser.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.image = pygame.transform.scale(self.image, (25, 25))

#What it does each tick
    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/alien.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self):
        self.kill()

#Grouping
playership_group = pygame.sprite.Group()
plaser_group = pygame.sprite.Group()

#Spawn
playership = PlayerShip(int(screen_width / 2), screen_height + 340)
playership_group.add(playership)

def draw_bg():
    screen.blit(bg, (0, 0))

running = True
while running:
    clock.tick(fps)
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    plaser_group.update()

    playership_group.draw(screen)
    plaser_group.draw(screen)

    keys = pygame.key.get_pressed()

    #Player Movement
    if keys[pygame.K_LEFT] and playership.rect.left > 0:
        moveLeft(playership, 5)

    if keys[pygame.K_RIGHT] and playership.rect.right < 1750:
        moveRight(playership, 5)

    if keys[pygame.K_SPACE]:
        glaser = pLaser(playership.rect.centerx + 252.49999999999994, playership.rect.centery + 230)
        plaser_group.add(glaser)
        

    pygame.display.update()

pygame.quit()