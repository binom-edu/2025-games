import pygame
import random
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, 'playerShip.png'))
        self.rect = self.image.get_rect()
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
img_dir = os.path.join(os.path.dirname(__file__), 'img')
meteors_img = []
meteors_list = os.listdir(os.path.join(img_dir, 'meteors'))
for filename in meteors_list:
    meteors_img.append(pygame.image.load(os.path.join(img_dir, 'meteors', filename)))
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