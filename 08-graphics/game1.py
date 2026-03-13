import pygame
import random


class Pers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300.0, 300.0)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.vx = self.vy = 0
        self.destx, self.desty = self.rect.center
    
    def update(self):
        if abs(self.destx - self.x) > abs(self.vx):
            self.x += self.vx
        else:
            self.vx = 0
        if abs(self.desty - self.y) > abs(self.vy):
            self.y += self.vy
        else:
            self.vy = 0
        self.rect.center = (self.x, self.y)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, 600), random.randrange(0, 600))
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        all_sprites.add(self)
    
    def update(self):
        self.rect.x += self.vx
        if self.rect.left < 0: self.vx *= -1
        if self.rect.right > 599: self.vx *= -1
        self.rect.y += self.vy
        if self.rect.top < 0: self.vy *= -1
        if self.rect.bottom > 599: self.vy *= -1

pygame.init()

screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Привет мир')

clock = pygame.time.Clock()

FPS = 30

all_sprites = pygame.sprite.Group()

pers = Pers()
all_sprites.add(pers)

mobs = [Mob() for i in range(20)]

game_on = True

while game_on:
    clock.tick(FPS)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pers.destx, pers.desty = pygame.mouse.get_pos()
            pers.vx = (pers.destx - pers.rect.centerx) / 50
            pers.vy = (pers.desty - pers.rect.centery) / 50

    # update
    all_sprites.update()

    # render
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()