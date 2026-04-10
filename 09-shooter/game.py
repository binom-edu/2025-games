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
        self.hp = 100
        self.lives = 3
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 2
            if self.rect.left < 0: self.rect.left = 0
        if key_pressed[pygame.K_RIGHT]:
            self.rect.right = min(WIDTH, self.rect.right + 2)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(meteors_img)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.7 / 2)
        self.rect.centerx = random.randrange(0, WIDTH)
        self.rect.centery = random.randrange(-100, 0)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 10)
        all_sprites.add(self)
        mobs.add(self)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.centerx = random.randrange(0, WIDTH)
            self.rect.centery = random.randrange(-100, 0)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(1, 10)

def draw_hp(hp, surf):
    outlined_rect = pygame.Rect(20, 20, 100, 20)
    filled_rect = pygame.Rect(20, 20, hp, 20)
    pygame.draw.rect(surf, (0, 255, 0), filled_rect)
    pygame.draw.rect(surf, (255, 255, 255), outlined_rect, 2)

def draw_lives(lives, surf):
    image = pygame.image.load(os.path.join(img_dir, 'playerShip.png'))
    image = pygame.transform.scale(image, (30, 20))
    rect = image.get_rect()
    rect.top = 20
    for i in range(lives):
        rect.right = WIDTH - 20 - 35*i
        surf.blit(image, rect)


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
mobs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5): Mob()

game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    all_sprites.update()

    # столкновение игрока с метеоритом
    for hit in pygame.sprite.spritecollide(player, mobs, 1, pygame.sprite.collide_circle):
        Mob()
        player.hp -= hit.radius
        if player.hp <= 0:
            player.hp = 0
    
    if player.hp == 0:
        if player.lives > 1:
            player.lives -= 1
            player.hp = 100
        else:
            game_on = False

    # отрисовка
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    draw_hp(player.hp, screen)
    draw_lives(player.lives, screen)
    pygame.display.flip()


pygame.quit()