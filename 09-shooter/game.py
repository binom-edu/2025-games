import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((50, 30))
        self.rect = self.image.get_rect()
        self.image.fill((128, 128, 128))
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 2
            if self.rect.left < 0: self.rect.left = 0
        if key_pressed[pygame.K_RIGHT]:
            self.rect.right = min(WIDTH, self.rect.right + 2)

WIDTH = 400
HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Shooter 26')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    all_sprites.update()
    # отрисовка
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()